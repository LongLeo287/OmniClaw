# OmniClaw Repo Plow: FETCHED_hermes-agent_123035



================================================
FILE: functioncall.py
================================================
import argparse
import torch
import json

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig
)

import functions
from prompter import PromptManager
from validator import validate_function_call_schema

from utils import (
    print_nous_text_art,
    inference_logger,
    get_assistant_message,
    get_chat_template,
    validate_and_extract_tool_calls
)

class ModelInference:
    def __init__(self, model_path, chat_template, load_in_4bit):
        inference_logger.info(print_nous_text_art())
        self.prompter = PromptManager()
        self.bnb_config = None

        if load_in_4bit == "True":
            self.bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
            )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            return_dict=True,
            quantization_config=self.bnb_config,
            torch_dtype=torch.float16,
            attn_implementation="flash_attention_2",
            device_map="auto",
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "left"

        if self.tokenizer.chat_template is None:
            print("No chat template defined, getting chat_template...")
            self.tokenizer.chat_template = get_chat_template(chat_template)
        
        inference_logger.info(self.model.config)
        inference_logger.info(self.model.generation_config)
        inference_logger.info(self.tokenizer.special_tokens_map)

    def process_completion_and_validate(self, completion, chat_template):

        assistant_message = get_assistant_message(completion, chat_template, self.tokenizer.eos_token)

        if assistant_message:
            validation, tool_calls, error_message = validate_and_extract_tool_calls(assistant_message)

            if validation:
                inference_logger.info(f"parsed tool calls:\n{json.dumps(tool_calls, indent=2)}")
                return tool_calls, assistant_message, error_message
            else:
                tool_calls = None
                return tool_calls, assistant_message, error_message
        else:
            inference_logger.warning("Assistant message is None")
            raise ValueError("Assistant message is None")
        
    def execute_function_call(self, tool_call):
        function_name = tool_call.get("name")
        function_to_call = getattr(functions, function_name, None)
        function_args = tool_call.get("arguments", {})

        inference_logger.info(f"Invoking function call {function_name} ...")
        function_response = function_to_call(*function_args.values())
        results_dict = f'{{"name": "{function_name}", "content": {function_response}}}'
        return results_dict
    
    def run_inference(self, prompt):
        inputs = self.tokenizer.apply_chat_template(
            prompt,
            add_generation_prompt=True,
            return_tensors='pt'
        )

        tokens = self.model.generate(
            inputs.to(self.model.device),
            max_new_tokens=1500,
            temperature=0.8,
            repetition_penalty=1.1,
            do_sample=True,
            eos_token_id=self.tokenizer.eos_token_id
        )
        completion = self.tokenizer.decode(tokens[0], skip_special_tokens=False, clean_up_tokenization_space=True)
        return completion

    def generate_function_call(self, query, chat_template, num_fewshot, max_depth=5):
        try:
            depth = 0
            user_message = f"{query}\nThis is the first turn and you don't have <tool_results> to analyze yet"
            chat = [{"role": "user", "content": user_message}]
            tools = functions.get_openai_tools()
            prompt = self.prompter.generate_prompt(chat, tools, num_fewshot)
            completion = self.run_inference(prompt)

            def recursive_loop(prompt, completion, depth):
                nonlocal max_depth
                tool_calls, assistant_message, error_message = self.process_completion_and_validate(completion, chat_template)
                prompt.append({"role": "assistant", "content": assistant_message})

                tool_message = f"Agent iteration {depth} to assist with user query: {query}\n"
                if tool_calls:
                    inference_logger.info(f"Assistant Message:\n{assistant_message}")

                    for tool_call in tool_calls:
                        validation, message = validate_function_call_schema(tool_call, tools)
                        if validation:
                            try:
                                function_response = self.execute_function_call(tool_call)
                                tool_message += f"<tool_response>\n{function_response}\n</tool

================================================
FILE: functions.py
================================================
import re
import inspect
import requests
import pandas as pd
import yfinance as yf
import concurrent.futures

from typing import List
from bs4 import BeautifulSoup
from utils import inference_logger
from langchain.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool

@tool
def code_interpreter(code_markdown: str) -> dict | str:
    """
    Execute the provided Python code string on the terminal using exec.

    The string should contain valid, executable and pure Python code in markdown syntax.
    Code should also import any required Python packages.

    Args:
        code_markdown (str): The Python code with markdown syntax to be executed.
            For example: ```python\n<code-string>\n```

    Returns:
        dict | str: A dictionary containing variables declared and values returned by function calls,
            or an error message if an exception occurred.

    Note:
        Use this function with caution, as executing arbitrary code can pose security risks.
    """
    try:
        # Extracting code from Markdown code block
        code_lines = code_markdown.split('\n')[1:-1]
        code_without_markdown = '\n'.join(code_lines)

        # Create a new namespace for code execution
        exec_namespace = {}

        # Execute the code in the new namespace
        exec(code_without_markdown, exec_namespace)

        # Collect variables and function call results
        result_dict = {}
        for name, value in exec_namespace.items():
            if callable(value):
                try:
                    result_dict[name] = value()
                except TypeError:
                    # If the function requires arguments, attempt to call it with arguments from the namespace
                    arg_names = inspect.getfullargspec(value).args
                    args = {arg_name: exec_namespace.get(arg_name) for arg_name in arg_names}
                    result_dict[name] = value(**args)
            elif not name.startswith('_'):  # Exclude variables starting with '_'
                result_dict[name] = value

        return result_dict

    except Exception as e:
        error_message = f"An error occurred: {e}"
        inference_logger.error(error_message)
        return error_message

@tool
def google_search_and_scrape(query: str) -> dict:
    """
    Performs a Google search for the given query, retrieves the top search result URLs,
    and scrapes the text content and table data from those pages in parallel.

    Args:
        query (str): The search query.
    Returns:
        list: A list of dictionaries containing the URL, text content, and table data for each scraped page.
    """
    num_results = 2
    url = 'https://www.google.com/search'
    params = {'q': query, 'num': num_results}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.3'}
    
    inference_logger.info(f"Performing google search with query: {query}\nplease wait...")
    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = [result.find('a')['href'] for result in soup.find_all('div', class_='tF2Cxc')]
    
    inference_logger.info(f"Scraping text from urls, please wait...") 
    [inference_logger.info(url) for url in urls]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(lambda url: (url, requests.get(url, headers=headers).text if isinstance(url, str) else None), url) for url in urls[:num_results] if isinstance(url, str)]
        results = []
        for future in concurrent.futures.as_completed(futures):
            url, html = future.result()
            soup = BeautifulSoup(html, 'html.parser')
            paragraphs = [p.text.strip() for p in soup.find_all('p') if p.text.strip()]
            text_content = ' '.join(paragraphs)
            text_content = re.sub(r'\s+', ' ', text_content)
            table_data = [[cell.get_text(strip=True) for cell in row.find_all('td')] for table in soup.find_all('table') for row in table.find_all('tr')]
            if text_content or table_data:
                results.append({'url': url, 'content': text_content, 'tables': table_data})
    return results

@tool
def get_current_stock_price(symbol: str) -> float:
  """
  Get the current stock price for a given symbol.

  Args:
    symbol (str): The stock symbol.

  Returns:
    float: The current stock price, or None if an error occurs.
  """
  try:
    stock = yf.Ticker(symbol)
    # Use "regularMarketPrice" for regular market hours, or "currentPrice" for pre/post market
    current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"))
    return current_price if current_price else None
  except Exception as e:
    print(f"Error fetching current price for {symbol}: {e}")
    return None

@tool
def get_stock_fundamentals(symbol: str) -> dict:
    """


================================================
FILE: jsonmode.py
================================================
import argparse
import torch
import json

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig
)

from validator import validate_json_data

from utils import (
    print_nous_text_art,
    inference_logger,
    get_assistant_message,
    get_chat_template,
    validate_and_extract_tool_calls
)

# create your pydantic model for json object here
from typing import List, Optional
from pydantic import BaseModel

class Character(BaseModel):
    name: str
    species: str
    role: str
    personality_traits: Optional[List[str]]
    special_attacks: Optional[List[str]]

    class Config:
        schema_extra = {
            "additionalProperties": False
        }

# serialize pydantic model into json schema
pydantic_schema = Character.schema_json()

class ModelInference:
    def __init__(self, model_path, chat_template, load_in_4bit):
        inference_logger.info(print_nous_text_art())
        self.bnb_config = None

        if load_in_4bit == "True":
            self.bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
            )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            return_dict=True,
            quantization_config=self.bnb_config,
            torch_dtype=torch.float16,
            attn_implementation="flash_attention_2",
            device_map="auto",
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "left"

        if self.tokenizer.chat_template is None:
            print("No chat template defined, getting chat_template...")
            self.tokenizer.chat_template = get_chat_template(chat_template)
        
        inference_logger.info(self.model.config)
        inference_logger.info(self.model.generation_config)
        inference_logger.info(self.tokenizer.special_tokens_map)
    
    def run_inference(self, prompt):
        inputs = self.tokenizer.apply_chat_template(
            prompt,
            add_generation_prompt=True,
            return_tensors='pt'
        )

        tokens = self.model.generate(
            inputs.to(self.model.device),
            max_new_tokens=1500,
            temperature=0.8,
            repetition_penalty=1.1,
            do_sample=True,
            eos_token_id=self.tokenizer.eos_token_id
        )
        completion = self.tokenizer.decode(tokens[0], skip_special_tokens=False, clean_up_tokenization_space=True)
        return completion

    def generate_json_completion(self, query, chat_template, max_depth=5):
        try:
            depth = 0
            sys_prompt = f"You are a helpful assistant that answers in JSON. Here's the json schema you must adhere to:\n<schema>\n{pydantic_schema}\n</schema>"
            prompt = [{"role": "system", "content": sys_prompt}]
            prompt.append({"role": "user", "content": query})

            inference_logger.info(f"Running inference to generate json object for pydantic schema:\n{json.dumps(json.loads(pydantic_schema), indent=2)}")
            completion = self.run_inference(prompt)

            def recursive_loop(prompt, completion, depth):
                nonlocal max_depth

                assistant_message = get_assistant_message(completion, chat_template, self.tokenizer.eos_token)

                tool_message = f"Agent iteration {depth} to assist with user query: {query}\n"
                if assistant_message is not None:
                    validation, json_object, error_message = validate_json_data(assistant_message, json.loads(pydantic_schema))
                    if validation:
                        inference_logger.info(f"Assistant Message:\n{assistant_message}")
                        inference_logger.info(f"json schema validation passed")
                        inference_logger.info(f"parsed json object:\n{json.dumps(json_object, indent=2)}")
                    elif error_message:
                        inference_logger.info(f"Assistant Message:\n{assistant_message}")
                        inference_logger.info(f"json schema validation failed")
                        tool_message += f"<tool_response>\nJson schema validation failed\nHere's the error stacktrace: {error_message}\nPlease return corrrect json object\n<tool_response>"
                        
                        depth += 1
                        if depth >= max_depth:
                            print(f"Maximum recursion depth reached ({max_depth}). Stopping recursion.")
                            return
                        
                        prompt.append({"role": "tool", "content": tool_message})
                        completion = self.run_inference(prompt)
                        recursive_loop(prompt, completion, depth)
         

================================================
FILE: prompter.py
================================================
import datetime
from pydantic import BaseModel
from typing import Dict
from schema import FunctionCall
from utils import (
    get_fewshot_examples
)
import yaml
import json
import os

class PromptSchema(BaseModel):
    Role: str
    Objective: str
    Tools: str
    Examples: str
    Schema: str
    Instructions: str 

class PromptManager:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
    def format_yaml_prompt(self, prompt_schema: PromptSchema, variables: Dict) -> str:
        formatted_prompt = ""
        for field, value in prompt_schema.dict().items():
            if field == "Examples" and variables.get("examples") is None:
                continue
            formatted_value = value.format(**variables)
            if field == "Instructions":
                formatted_prompt += f"{formatted_value}"
            else:
                formatted_value = formatted_value.replace("\n", " ")
                formatted_prompt += f"{formatted_value}"
        return formatted_prompt

    def read_yaml_file(self, file_path: str) -> PromptSchema:
        with open(file_path, 'r') as file:
            yaml_content = yaml.safe_load(file)
        
        prompt_schema = PromptSchema(
            Role=yaml_content.get('Role', ''),
            Objective=yaml_content.get('Objective', ''),
            Tools=yaml_content.get('Tools', ''),
            Examples=yaml_content.get('Examples', ''),
            Schema=yaml_content.get('Schema', ''),
            Instructions=yaml_content.get('Instructions', ''),
        )
        return prompt_schema
    
    def generate_prompt(self, user_prompt, tools, num_fewshot=None):
        prompt_path = os.path.join(self.script_dir, 'prompt_assets', 'sys_prompt.yml')
        prompt_schema = self.read_yaml_file(prompt_path)

        if num_fewshot is not None:
            examples = get_fewshot_examples(num_fewshot)
        else:
            examples = None

        schema_json = json.loads(FunctionCall.schema_json())
        #schema = schema_json.get("properties", {})

        variables = {
            "date": datetime.date.today(),
            "tools": tools,
            "examples": examples,
            "schema": schema_json
        }
        sys_prompt = self.format_yaml_prompt(prompt_schema, variables)

        prompt = [
                {'content': sys_prompt, 'role': 'system'}
            ]
        prompt.extend(user_prompt)
        return prompt
        
        


================================================
FILE: README.md
================================================
# Hermes-Function-Calling

This repository contains code for the Hermes Pro Large Language Model to perform function calling based on the provided schema. It allows users to query the model and retrieve information related to stock prices, company fundamentals, financial statements, and more.

## Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage
### Function calling

To run the function call inference with a query, use the following command:

```bash
python functioncall.py --query "I need the current stock price of Tesla (TSLA)"
```

### Json mode

To run the json mode inference with a query, use the following command:

```bash
python jsonmode.py --query "Please return a json object to represent Goku from the anime Dragon Ball Z?"

```

#### Command Line Arguments

- `--model_path`: Path to the model folder (default: "NousResearch/Hermes-2-Pro-Llama-3-8B").
- `--chat_template`: Chat template for prompt formatting (default: "chatml").
- `--num_fewshot`: Option to include few-shot examples (default: None).
- `--load_in_4bit`: Option to load in 4bit with bitsandbytes (default: "False").
- `--query`: Query to be used for function call inference (default: "I need the current stock price of Tesla (TSLA)").
- `--max_depth`: Maximum number of recursive iterations (default: 5).

## Adding Custom Functions

To add your own functions for the model to use, you can modify the `functions.py` script. This script contains various functions that retrieve stock-related information using the `yfinance` library.

Here's an example of how to add a new function:

```python
@tool
def get_new_function(symbol: str) -> dict:
    """
    Description of the new function.
    Args:
        symbol (str): The stock symbol.
    Returns:
        dict: Dictionary containing the desired information.
    """
    try:
        # Implement the logic to retrieve the desired information
        # using the yfinance library or any other relevant libraries
        # Example:
        stock = yf.Ticker(symbol)
        new_info = stock.new_method()
        return new_info
    except Exception as e:
        print(f"Error fetching new information for {symbol}: {e}")
        return {}
```

After defining your new function, make sure to add it to the `get_openai_tools()` function in the `functions.py` script:

```python
def get_openai_tools() -> List[dict]:
    functions = [
        # ...
        get_new_function,
        # ...
    ]
    tools = [convert_to_openai_tool(f) for f in functions]
    return tools
```

This will ensure that your new function is included in the list of available tools for the model to use.

## Adding Custom Pydantic Model

To add your own pydantic models to create json schema for the model to use, you can replace the pydantic models in the `jsonmode.py` script. 

Here's an example of how to add a new pydantic model:

```python
from typing import List, Optional
from pydantic import BaseModel

class Character(BaseModel):
    name: str
    species: str
    role: str
    personality_traits: Optional[List[str]]
    special_attacks: Optional[List[str]]

    class Config:
        schema_extra = {
            "additionalProperties": False
        }
```
You need to serialize the pydantic model into json schema as follows:

```python
pydantic_schema = Character.schema_json()
```
## Key Scripts

The repository contains several key scripts that work together to enable function calling with the Hermes Pro Large Language Model:

- `functions.py`: This script is where all the functions/tools you want the model to have access to are made available.

- `functioncall.py`: This script is the main entry point for running the function call inference. It initializes the model, tokenizer, and other necessary components, and handles the recursive loop for generating function calls and executing them.

- `jsonmode.py`: This script can be used for running json mode inference. It has similar functionality as functioncall.py but for generating json object adhering to the json schema and validating it.

- `prompter.py`: This script manages the prompt generation process. It reads the system prompt from a YAML file, formats it with the necessary variables (e.g., tools, examples, schema), and generates the final prompt for the model.

- `schema.py`: This script defines the Pydantic models used for representing function calls and function definitions. It provides a structured way to define and validate the function call schema.

## Inference Example Output

Here's an example of the inference output:

```
<|im_start|>user
Fetch the stock fundamentals data for Tesla (TSLA)<|im_end|>
<|im_start|>assistant
<tool_call>
{"name": "get_stock_fundamentals", "arguments": {"symbol": "TSLA"}}
</tool_call><|im_end|>
<|im_start|>tool
<tool_response>
{"name": "get_stock_fundamentals", "content": {"symbol": "TSLA", "company_name": "Tesla, Inc.", "sector": "Consumer Cyclical", "industry": "Auto Manuf

================================================
FILE: requirements.txt
================================================
torch==2.1.2
transformers>=4.38.1
bitsandbytes>=0.41.1
accelerate==0.27.2
langchain==0.1.9
pydantic==2.6.2
jsonschema==4.21.1
yfinance==0.2.36
pandas==2.2.0
ninja==1.11.1.1
flash-attn==2.5.5
protobuf
sentencepiece
art


================================================
FILE: schema.py
================================================
from pydantic import BaseModel
from typing import List, Dict, Literal, Optional

class FunctionCall(BaseModel):
    arguments: dict
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: str
    """The name of the function to call."""

class FunctionDefinition(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, object]] = None

class FunctionSignature(BaseModel):
    function: FunctionDefinition
    type: Literal["function"]


================================================
FILE: utils.py
================================================
import ast
import os
import re
import json
import logging
import datetime
import xml.etree.ElementTree as ET

from art import text2art
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)
script_dir = os.path.dirname(os.path.abspath(__file__))
now = datetime.datetime.now()
log_folder = os.path.join(script_dir, "inference_logs")
os.makedirs(log_folder, exist_ok=True)
log_file_path = os.path.join(
    log_folder, f"function-calling-inference_{now.strftime('%Y-%m-%d_%H-%M-%S')}.log"
)
# Use RotatingFileHandler from the logging.handlers module
file_handler = RotatingFileHandler(log_file_path, maxBytes=0, backupCount=0)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", datefmt="%Y-%m-%d:%H:%M:%S")
file_handler.setFormatter(formatter)

inference_logger = logging.getLogger("function-calling-inference")
inference_logger.addHandler(file_handler)

def print_nous_text_art(suffix=None):
    font = "nancyj"
    ascii_text = "  nousresearch"
    if suffix:
        ascii_text += f"  x  {suffix}"
    ascii_art = text2art(ascii_text, font=font)
    print(ascii_art)

def get_fewshot_examples(num_fewshot):
    """return a list of few shot examples"""
    example_path = os.path.join(script_dir, 'prompt_assets', 'few_shot.json')
    with open(example_path, 'r') as file:
        examples = json.load(file)  # Use json.load with the file object, not the file path
    if num_fewshot > len(examples):
        raise ValueError(f"Not enough examples (got {num_fewshot}, but there are only {len(examples)} examples).")
    return examples[:num_fewshot]

def get_chat_template(chat_template):
    """read chat template from jinja file"""
    template_path = os.path.join(script_dir, 'chat_templates', f"{chat_template}.j2")

    if not os.path.exists(template_path):
        print
        inference_logger.error(f"Template file not found: {chat_template}")
        return None
    try:
        with open(template_path, 'r') as file:
            template = file.read()
        return template
    except Exception as e:
        print(f"Error loading template: {e}")
        return None

def get_assistant_message(completion, chat_template, eos_token):
    """define and match pattern to find the assistant message"""
    completion = completion.strip()

    if chat_template == "zephyr":
        assistant_pattern = re.compile(r'<\|assistant\|>((?:(?!<\|assistant\|>).)*)$', re.DOTALL)
    elif chat_template == "chatml":
        assistant_pattern = re.compile(r'<\|im_start\|>\s*assistant((?:(?!<\|im_start\|>\s*assistant).)*)$', re.DOTALL)

    elif chat_template == "vicuna":
        assistant_pattern = re.compile(r'ASSISTANT:\s*((?:(?!ASSISTANT:).)*)$', re.DOTALL)
    else:
        raise NotImplementedError(f"Handling for chat_template '{chat_template}' is not implemented.")
    
    assistant_match = assistant_pattern.search(completion)
    if assistant_match:
        assistant_content = assistant_match.group(1).strip()
        if chat_template == "vicuna":
            eos_token = f"</s>{eos_token}"
        return assistant_content.replace(eos_token, "")
    else:
        assistant_content = None
        inference_logger.info("No match found for the assistant pattern")
        return assistant_content

def validate_and_extract_tool_calls(assistant_content):
    validation_result = False
    tool_calls = []
    error_message = None

    try:
        # wrap content in root element
        xml_root_element = f"<root>{assistant_content}</root>"
        root = ET.fromstring(xml_root_element)

        # extract JSON data
        for element in root.findall(".//tool_call"):
            json_data = None
            try:
                json_text = element.text.strip()

                try:
                    # Prioritize json.loads for better error handling
                    json_data = json.loads(json_text)
                except json.JSONDecodeError as json_err:
                    try:
                        # Fallback to ast.literal_eval if json.loads fails
                        json_data = ast.literal_eval(json_text)
                    except (SyntaxError, ValueError) as eval_err:
                        error_message = f"JSON parsing failed with both json.loads and ast.literal_eval:\n"\
                                        f"- JSON Decode Error: {json_err}\n"\
                                        f"- Fallback Syntax/Value Error: {eval_err}\n"\
                                        f"- Problematic JSON text: {json_text}"
                        inference_logger.error(error_message)
                        continue
            except Exception as e:
                error_message = f"Cannot strip text: {e}"
                inference_logger.error(error_message)

            if json_dat

================================================
FILE: validator.py
================================================
import ast
import json
from jsonschema import validate
from pydantic import ValidationError
from utils import inference_logger, extract_json_from_markdown
from schema import FunctionCall, FunctionSignature

def validate_function_call_schema(call, signatures):
    try:
        call_data = FunctionCall(**call)
    except ValidationError as e:
        return False, str(e)

    for signature in signatures:
        try:
            signature_data = FunctionSignature(**signature)
            if signature_data.function.name == call_data.name:
                # Validate types in function arguments
                for arg_name, arg_schema in signature_data.function.parameters.get('properties', {}).items():
                    if arg_name in call_data.arguments:
                        call_arg_value = call_data.arguments[arg_name]
                        if call_arg_value:
                            try:
                                validate_argument_type(arg_name, call_arg_value, arg_schema)
                            except Exception as arg_validation_error:
                                return False, str(arg_validation_error)

                # Check if all required arguments are present
                required_arguments = signature_data.function.parameters.get('required', [])
                result, missing_arguments = check_required_arguments(call_data.arguments, required_arguments)
                if not result:
                    return False, f"Missing required arguments: {missing_arguments}"

                return True, None
        except Exception as e:
            # Handle validation errors for the function signature
            return False, str(e)

    # No matching function signature found
    return False, f"No matching function signature found for function: {call_data.name}"

def check_required_arguments(call_arguments, required_arguments):
    missing_arguments = [arg for arg in required_arguments if arg not in call_arguments]
    return not bool(missing_arguments), missing_arguments

def validate_enum_value(arg_name, arg_value, enum_values):
    if arg_value not in enum_values:
        raise Exception(
            f"Invalid value '{arg_value}' for parameter {arg_name}. Expected one of {', '.join(map(str, enum_values))}"
        )

def validate_argument_type(arg_name, arg_value, arg_schema):
    arg_type = arg_schema.get('type', None)
    if arg_type:
        if arg_type == 'string' and 'enum' in arg_schema:
            enum_values = arg_schema['enum']
            if None not in enum_values and enum_values != []:
                try:
                    validate_enum_value(arg_name, arg_value, enum_values)
                except Exception as e:
                    # Propagate the validation error message
                    raise Exception(f"Error validating function call: {e}")

        python_type = get_python_type(arg_type)
        if not isinstance(arg_value, python_type):
            raise Exception(f"Type mismatch for parameter {arg_name}. Expected: {arg_type}, Got: {type(arg_value)}")

def get_python_type(json_type):
    type_mapping = {
        'string': str,
        'number': (int, float),
        'integer': int,
        'boolean': bool,
        'array': list,
        'object': dict,
        'null': type(None),
    }
    return type_mapping[json_type]

def validate_json_data(json_object, json_schema):
    valid = False
    error_message = None
    result_json = None

    try:
        # Attempt to load JSON using json.loads
        try:
            result_json = json.loads(json_object)
        except json.decoder.JSONDecodeError:
            # If json.loads fails, try ast.literal_eval
            try:
                result_json = ast.literal_eval(json_object)
            except (SyntaxError, ValueError) as e:
                try:
                    result_json = extract_json_from_markdown(json_object)
                except Exception as e:
                    error_message = f"JSON decoding error: {e}"
                    inference_logger.info(f"Validation failed for JSON data: {error_message}")
                    return valid, result_json, error_message

        # Return early if both json.loads and ast.literal_eval fail
        if result_json is None:
            error_message = "Failed to decode JSON data"
            inference_logger.info(f"Validation failed for JSON data: {error_message}")
            return valid, result_json, error_message

        # Validate each item in the list against schema if it's a list
        if isinstance(result_json, list):
            for index, item in enumerate(result_json):
                try:
                    validate(instance=item, schema=json_schema)
                    inference_logger.info(f"Item {index+1} is valid against the schema.")
                except ValidationError as e:
                    error_message = f"Validation failed for item {index+1}: {e}"
                    break
        else:
            # Default to valida

================================================
FILE: examples\__init__.py
================================================


================================================
FILE: prompt_assets\few_shot.json
================================================
[
    {
        "example": "```\nSYSTEM: You are a helpful assistant who has access to functions. Use them if required\n<tools>[\n {\n \"name\": \"calculate_distance\",\n \"description\": \"Calculate the distance between two locations\",\n \"parameters\": {\n \"type\": \"object\",\n \"properties\": {\n \"origin\": {\n \"type\": \"string\",\n \"description\": \"The starting location\"\n },\n \"destination\": {\n \"type\": \"string\",\n \"description\": \"The destination location\"\n },\n \"mode\": {\n \"type\": \"string\",\n \"description\": \"The mode of transportation\"\n }\n },\n \"required\": [\n \"origin\",\n \"destination\",\n \"mode\"\n ]\n }\n },\n {\n \"name\": \"generate_password\",\n \"description\": \"Generate a random password\",\n \"parameters\": {\n \"type\": \"object\",\n \"properties\": {\n \"length\": {\n \"type\": \"integer\",\n \"description\": \"The length of the password\"\n }\n },\n \"required\": [\n \"length\"\n ]\n }\n }\n]\n\n</tools>\nUSER: Hi, I need to know the distance from New York to Los Angeles by car.\nASSISTANT:\n<tool_call>\n{\"arguments\": {\"origin\": \"New York\",\n \"destination\": \"Los Angeles\", \"mode\": \"car\"}, \"name\": \"calculate_distance\"}\n</tool_call>\n```\n"
    },
    {
        "example": "```\nSYSTEM: You are a helpful assistant with access to functions. Use them if required\n<tools>[\n {\n \"name\": \"calculate_distance\",\n \"description\": \"Calculate the distance between two locations\",\n \"parameters\": {\n \"type\": \"object\",\n \"properties\": {\n \"origin\": {\n \"type\": \"string\",\n \"description\": \"The starting location\"\n },\n \"destination\": {\n \"type\": \"string\",\n \"description\": \"The destination location\"\n },\n \"mode\": {\n \"type\": \"string\",\n \"description\": \"The mode of transportation\"\n }\n },\n \"required\": [\n \"origin\",\n \"destination\",\n \"mode\"\n ]\n }\n },\n {\n \"name\": \"generate_password\",\n \"description\": \"Generate a random password\",\n \"parameters\": {\n \"type\": \"object\",\n \"properties\": {\n \"length\": {\n \"type\": \"integer\",\n \"description\": \"The length of the password\"\n }\n },\n \"required\": [\n \"length\"\n ]\n }\n }\n]\n\n</tools>\nUSER: Can you help me generate a random password with a length of 8 characters?\nASSISTANT:\n<tool_call>\n{\"arguments\": {\"length\": 8}, \"name\": \"generate_password\"}\n</tool_call>\n```"
    }
]

================================================
FILE: template_tests\ollama_template.go
================================================
package main

import (
    "fmt"
    "text/template"
    "os"
)


type Function struct {
    Name       string `json:"name"`
    Description string `json:"description"`
    Parameters map[string]interface{} `json:"parameters"`
}

type Tool struct {
    Function Function `json:"function"`
}

type ToolCall struct {
    Function struct {
        Name       string `json:"name"`
        Arguments  string `json:"arguments"`
    } `json:"function"`
}

type Message struct {
    Role       string      `json:"role"`
    Content    string      `json:"content"`
    ToolCalls  []ToolCall  `json:"tool_calls"`
}

type Data struct {
    Messages  []Message   `json:"messages"`
    Tools     []Tool      `json:"tools"`
    System    string      `json:"system"`
    Prompt    string      `json:"prompt"`
    Response  string      `json:"response"`
}

func main() {
	const tpl = `
{{- if .Messages }}
{{- if or .System .Tools }}<|im_start|>system
{{ .System }}
{{- if .Tools }}
You are a function calling AI model. You are provided with function signatures within <tools> </tools> XML tags. You may call one or more functions to assist with the user query. If available tools are not relevant in assisting with user query, just respond in natural conversational language. Don't make assumptions about what values to plug into functions. After calling & executing the functions, you will be provided with function results within <tool_response> </tool_response> XML tags.
<tools>
{{- range .Tools }}
{{ .Function.Name }}: {{ .Function.Description }}
Parameters: {{ .Function.Parameters }}
{{- end }}
</tools>
For each function call return a JSON object, with the following pydantic model json schema for each:
{'title': 'FunctionCall', 'type': 'object', 'properties': {'arguments': {'title': 'Arguments', 'type': 'object'}, 'name': {'title': 'Name', 'type': 'string'}}, 'required': ['arguments', 'name']}
Each function call should be enclosed within <tool_call> </tool_call> XML tags. You must use <scratch_pad> </scratch_pad> XML tags to record your reasoning and planning before you call the functions as follows.
Example:
<scratch_pad>
Goal: <state task assigned by user>
Actions:
<if tool calls need to be generated:>
- {result_var_name1} = functions.{function_name1}({param1}={value1},...)
- {result_var_name2, result_var_name3} = ...
<if no tool call needs to be generated:> None
Observation: <set observation 'None' with tool calls; plan final tools results summary when provided>
Reflection: <evaluate query-tool relevance and required parameters when tools called; analyze overall task status when observations made>
</scratch_pad>
<tool_call>
{'name': <function-name>, 'arguments': <args-dict>}
</tool_call>
{{- end }}<|im_end|>
{{- end }}

{{- $hasToolResponses := false }}
{{- range .Messages }}
{{- if eq .Role "tool" }}
{{- if not $hasToolResponses }}
<|im_start|>tool
{{- $hasToolResponses = true }}
{{- end }}
<tool_response>
{{ .Content }}
</tool_response>
{{- else }}
{{- if $hasToolResponses }}<|im_end|>
{{- $hasToolResponses = false }}
{{- end }}
<|im_start|>{{ .Role }}
{{- if and (eq .Role "assistant") .ToolCalls }}
{{- range .ToolCalls }}
<tool_call>
{"name": "{{ .Function.Name }}", "arguments": {{ .Function.Arguments }}}
</tool_call>
{{- end }}
{{- else }}
{{ .Content }}
{{- end }}<|im_end|>
{{- end }}
{{- end }}
{{- if $hasToolResponses }}<|im_end|>
{{- end }}

{{- else }}
{{- if .System }}
<|im_start|>system
{{ .System }}<|im_end|>
{{- end }}

{{- if .Prompt }}
<|im_start|>user
{{ .Prompt }}<|im_end|>
{{- end }}

<|im_start|>assistant
{{ .Response }}<|im_end|>
{{- end }}
`

 // Create sample data with multiple tool calls
 data := Data{
	Messages: []Message{
		{
			Role:    "user",
			Content: "What's the weather like in New York and LA today?",
		},
		{
			Role:    "assistant",
			Content: "To provide you with accurate information about the weather in New York and Los Angeles today, I'll need to check the current weather data for both cities.",
			ToolCalls: []ToolCall{
				{
					Function: struct {
						Name       string `json:"name"`
						Arguments  string `json:"arguments"`
					}{
						Name: "get_weather",
						Arguments: `{"location": "New York", "date": "today"}`,
					},
				},
				{
					Function: struct {
						Name       string `json:"name"`
						Arguments  string `json:"arguments"`
					}{
						Name: "get_weather",
						Arguments: `{"location": "Los Angeles", "date": "today"}`,
					},
				},
			},
		},
		{
			Role:    "tool",
			Content: `{"temperature": 72, "condition": "Partly cloudy", "humidity": 65}`,
		},
		{
			Role:    "tool",
			Content: `{"temperature": 85, "condition": "Sunny", "humidity": 30}`,
		},
		{
			Role:    "assistant",
			Content: "Based on the current weather data, the weather in New York today is partly cloudy with a temperature of 72°F and humidity at 65%. In Los Angeles, it's sunny with a temperature of 85°F and humidity at 30%.",
		},
	},
	Tools: []Tool{
		{
			Function: Function{
				Name: "get_weather",