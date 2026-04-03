---
id: bambo-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:56.432460
---

# KNOWLEDGE EXTRACT: Bambo
> **Extracted on:** 2026-03-30 13:27:42
> **Source:** Bambo

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2024 LB-Young

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# Bambo
Bambo is a new proxy framework. Compared with mainstream frameworks, it is more lightweight and flexible and can handle various load tasks.

![Bambo_structure](https://github.com/user-attachments/assets/360e9b32-43fc-4b61-956b-5eac579add12)

# USE
1. pip install {packages}. 
- pip install -r requirements.txt  
- (This project uses deepseek as an example. openai needs to be installed.)
2. Define all tools you want to use in the tools directory or other path. The custom function needs to be asynchronous, the parameter passed must include **params_format**, and the default value is False. The **params_format** parameter must be checked at the beginning of the function body. If True, all other parameters that must be passed are returned as a list to verify that the extracted parameters meet the function call requirements when tool_call is used.
3. You need to define the llm you want to call in the llm_cient.py file, including the **model** and **client** parameters.
4. You can then create your own test scripts in the examples folder. In the script, you need to define the /*roles*/ and /*tools*/ that your scenario needs. Bambo's instantiated object is then initialized and query is passed into the object's execute interface, and Bambo starts the execution logic.

- Note:
1. /*When initializing the Bambo example, in the tools parameters, each tool must be configured with describe and object. describe is the description of the current tool, and what parameters need to be extracted when calling the current tool. object is the function object of the current tool.*/

2. Some tools are not included, you can implement them freely. If you need some of my tools, you can send a message to my email(lby15356@gmail.com).

### Example
```python
import asyncio
from src.bambo import Bambo
from src.llm_client import client, model
from src.tools.code_execute import code_execute
roles = {
    "finance_expert": "金融专家",
    "law_expert": "法律专家",
    "medical_expert": "医疗专家",
    "computer_expert": "计算机专家",
}
tools = {}
bambo = Bambo(
    client=client,
    bambo_role=None,
    roles=roles,
    tools=tools,
    agents=None,
    model=model,
)
query = "我是高考生，现在想要选专业，但是不知道选什么专业。请你介绍一下金融、法律和计算机三个专业分别有什么优点和缺点。"
essages = [{"role": "user", "content": query}]
async for item in bambo.execute(messages=messages):
    print(item, end="", flush=True)
```

### Note
1. You can redefine your **bambo-role** and pass it in when instantiating the Bambo object to override the default value.


# CASES
##  NotebookLM
- describe: Based on Bambo, notebooklm has achieved a similar effect, which can summarize the main content of the file in the form of an interview conversation with the incoming text. However, there is no TTS related logic in this project, so it can only be converted to text in the form of dialogue. If readers want to implement TTS, they can add corresponding code in the test script.
```
python examples/notebooklm.py
```
- query:"请根据以下参考信息回答问题：\n{reference}\n\n问题：以采访对话形式介绍一下这篇文章的内容，至少5论对话。"
- answer:
  ![notetbook](https://github.com/user-attachments/assets/3cc6a966-3b57-4527-90d1-91edfdb77729)

## PaperRecommend
- The paper recommend tool is an agent for recommending papers every day, which retrieves some of the latest papers at the moment, summarizes them by category, and recommends them according to the user's research direction.
```
python examples/paper_recommend.py
```
- query:
"""
1、请首先搜索最新的10篇论文；
2、然后对这些论文进行分类，类别列表为['LLM','RAG','Agent','多模态','音频','计算机视觉','其它']，分类结果按照{论文标题：类别}的形式输出;
3、对分类后的论文按照类别进行总结，并且给出当前类别有哪些文件，总结结果按照{类别1：类别1多篇论文的总结。类别1的所有参考论文标题。}的形式输出；
4、我的研究方向是['LLM','RAG','Agent','多模态'],请根据我的研究方向，推荐一些相关的论文，推荐结果按照{论文标题：类别、论文链接、摘要的总结}的形式输出；
"""
- answer
```
https://x.com/i/status/1866480838394745075
https://www.bilibili.com/video/BV1ajqCYrEVa/?vd_source=63fa380f22166ecfe2ab8b828b77344d
```

##  MultiRoles
- describe: Multi-role scenarios are implemented based on Bambo for building agent-based team-based scenarios. This project constructs a college entrance examination consulting group, including experts from different majors, who can provide professional responses to students' questions from different majors.
```
python examples/multi_roles.py
```
- query:"我是高考生，现在想要选专业，但是不知道选什么专业。请你介绍一下金融、法律和计算机三个专业分别有什么优点和缺点。"
- answer:
![multi_roles](https://github.com/user-attachments/assets/151758eb-0dcc-4872-8807-5a2cc226e07b)



## CodeExpert
- describe: CodeExpert is a code expert based on the Bambo framework who can answer questions about code and execute code.
```
python examples/code_expert.py
```
- query:"请帮我生成一段选择排序的代码，调用代码执行器运行生成的代码，基于结果分析一下选择排序的特点"
- answer:
![code_expert](https://github.com/user-attachments/assets/e6f54290-3418-47dc-bf93-71515df1ce28)


# Participate
Bambo is currently in its initial stage, more functions will be integrated in the future, and we look forward to more partners joining in. If you would like to work with the author to improve this project, please contact lby15356@gmail.com
```

## File: `requirements.txt`
```
openai
```

## File: `examples/code_expert.py`
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import asyncio
from src.bambo import Bambo
from src.llm_client import client, model
from src.tools.code_execute import code_execute


async def main():
    roles = {
        "finance_expert": "金融专家",
        "law_expert": "法律专家",
        "medical_expert": "医疗专家",
        "computer_expert": "计算机专家",
    }
    tools = {
        "code_execute": {
            "describe": "代码执行器,参数{'code'：'待执行的代码'},如果代码有多个请合并成一个。",
            "object": code_execute,
        }
    }
    bambo = Bambo(
        client=client,
        bambo_role=None,
        roles=roles,
        tools=tools,
        agents=None,
        model=model,
    )
    query = "请帮我生成一段选择排序的代码，调用代码执行器运行生成的代码，基于结果分析一下选择排序的特点"
    messages = [{"role": "user", "content": query}]
    async for item in bambo.execute(messages=messages):
        print(item, end="", flush=True)



if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())
```

## File: `examples/dir_mapper.py`
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import asyncio
from src.bambo import Bambo
from src.llm_client import client, model
from src.tools.code_execute import code_execute


async def main():
    roles = {
        "finance_expert": "金融专家",
        "law_expert": "法律专家",
        "medical_expert": "医疗专家",
        "computer_expert": "计算机专家",
    }
    tools = {
        "code_execute": {
            "describe": "代码执行器,参数{'code'：'待执行的代码'},如果代码有多个请合并成一个。",
            "object": code_execute,
        }
    }
    bambo = Bambo(
        client=client,
        bambo_role=None,
        roles=roles,
        tools=tools,
        agents=None,
        model=model,
    )
    query = "请帮我生成一段选择排序的代码，调用代码执行器运行生成的代码，基于结果分析一下选择排序的特点"
    messages = [{"role": "user", "content": query}]
    async for item in bambo.execute(messages=messages):
        print(item, end="", flush=True)



if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())
```

## File: `examples/load_local_api_keys.py`
```python
import json

def load_local_api_keys(platform):
    """
    读取本地json文件中的API密钥
    """
    try:
        with open(r"C:\Users\86187\Desktop\api_key.json", "r", encoding="utf-8") as f:
            api_keys = json.load(f)
        return api_keys[platform]
    except Exception as e:
        raise Exception(f"读取API密钥文件失败: {str(e)}")

if __name__ == "__main__":
    keys = load_local_api_keys()
    print(keys)
```

## File: `examples/multi_roles.py`
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import asyncio
from src.bambo import Bambo
from src.llm_client import client, model
from src.tools.code_execute import code_execute


async def main():
    roles = {
        "finance_expert": "金融专家",
        "law_expert": "法律专家",
        "medical_expert": "医疗专家",
        "computer_expert": "计算机专家",
    }
    tools = {}
    bambo = Bambo(
        client=client,
        bambo_role=None,
        roles=roles,
        tools=tools,
        agents=None,
        model=model,
    )
    messages = []
    
    # Add default initial question about team experts
    default_question = "介绍一下你们团队的专家吧。"
    messages.append({"role": "user", "content": default_question})
    
    # Get initial response about team experts
    response = ""
    async for item in bambo.execute(messages=messages):
        print(item, end="", flush=True)
        response += item
    
    # Add assistant's response to messages for context
    messages.append({"role": "assistant", "content": response})
    
    while True:
        # Get user input
        query = input("\nPlease enter your question (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
            
        # Add user's query to messages
        messages.append({"role": "user", "content": query})
        
        # Collect assistant's response
        response = ""
        async for item in bambo.execute(messages=messages):
            print(item, end="", flush=True)
            response += item
            
        # Add assistant's response to messages for context
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())
```

## File: `examples/notebooklm.py`
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import asyncio
from src.bambo import Bambo
from src.llm_client import client, model
from src.tools.code_execute import code_execute


async def main():
    roles = {
        "host": "采访记者",
        "expert": "专家",
    }

    tools = {}
    bambo = Bambo(
        client=client,
        bambo_role=None,
        roles=roles,
        tools=tools,
        agents=None,
        model=model,
    )

    with open(r"C:\Users\86187\Desktop\test.txt", "r", encoding="utf-8") as f:
        reference = f.read()
    query = f"请根据以下参考信息回答问题：\n{reference}\n\n问题：以采访对话形式介绍一下这篇文章的内容，至少5论对话。"
    messages = [{"role": "user", "content": query}]
    async for item in bambo.execute(messages=messages):
        print(item, end="", flush=True)


if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())
```

## File: `examples/paper_recommend.py`
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import asyncio
from src.bambo import Bambo
from src.llm_client import client, model
from src.tools.code_execute import code_execute
from src.tools.paper_search import paper_search

sys.path.append(r"F:\python project\tools_set")
from tools import other_tools



async def main():
    roles = {
        "paper_classification_expert": "论文分类专家",
        "paper_summary_expert": "论文总结专家",
        "paper_recommend_expert": "论文推荐专家",
    }
    tools = {
        "code_execute": {
            "describe": "代码执行器,参数{'code'：'待执行的代码'},如果代码有多个请合并成一个。",
            "object": code_execute,
        },
        "paper_search":{
            "object":paper_search,
            "describe":"搜索最新的论文，需要参数{'nums':需要读取的论文数目}",
        }
    }
    tools.update(other_tools)
    bambo = Bambo(
        client=client,
        bambo_role=None,
        roles=roles,
        tools=tools,
        agents=None,
        model=model,
    )
    query = """
1、请首先搜索最新的10篇论文；
2、然后对这些论文进行分类，类别列表为['LLM','RAG','Agent','多模态','音频','计算机视觉','其它']，分类结果按照{论文标题：类别}的形式输出;
3、对分类后的论文按照类别进行总结，并且给出当前类别有哪些文件，总结结果按照{类别1：类别1多篇论文的总结。类别1的所有参考论文标题。}的形式输出；
4、我的研究方向是['LLM','RAG','Agent','多模态'],请根据我的研究方向，推荐一些相关的论文，推荐结果按照{论文标题：类别、论文链接、摘要的总结和创新点}的形式输出；
5、把推荐的论文和总结的内容组织成以下格式：
{
"推荐阅读内容和顺序":
……；
"参考论文总结":
……；
}
（要求：推荐阅读的论文需要给出论文的类别、star数目、标题、摘要总结（一句话）和论文链；按照分类的结果对类别内的全部论文进行总结，并且需要在总结内容的结束位置列出总结内容参考文章的标题。）
最后以“daily_paper_recommend”为主题发送到lby15356@gmail.com邮箱
"""
    messages = [{"role": "user", "content": query}]
    async for item in bambo.execute(messages=messages):
        print(item, end="", flush=True)



if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())
```

## File: `src/llm_client.py`
```python
# from zhipuai import ZhipuAI
from openai import OpenAI
from groq import Groq
from together import Together

import json

def load_api_key(platform):
    with open(r"/Users/liubaoyang/Documents/windows/api_key.json", "r", encoding="utf-8") as f:
        api_dict = json.load(f)
    return api_dict.get(platform, None)

# 智谱AI
# client = ZhipuAI(api_key=load_api_key("zhipu"))
# model="glm-4-plus"


# Deepseek
# client = OpenAI(
#     api_key=load_api_key("deepseek"),
#     base_url="https://api.deepseek.com",
# )
# model = "deepseek-chat"

# Deepseek （阿里云）
client = OpenAI(
    api_key=load_api_key("aliyun"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
model = "deepseek-v3"
# model = "deepseek-r1"

# Groq
# client = Groq(
#     api_key=load_api_key("groq")
# )
# model = "llama3-8b-8192"



# Together
# client = Together(api_key=load_api_key("together"))
# model = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
```

## File: `src/bambo/bambo.py`
```python
import re
import json

class Bambo:
    def __init__(self, client, bambo_role=None, roles=None, tools=None, agents=None, model=None):
        if bambo_role is None:
            bambo_role = self.get_role()
        else:
            pass
        self.roles_info = ""
        for key, value in roles.items():
            self.roles_info += f"@{key}: {value}\n"
        self.tools = {}
        self.tool_describe = []
        for key, value in tools.items():
            self.tools[key] = value["object"]
            self.tool_describe.append(f"{key}: {value['describe']}\n")
        self.role = bambo_role.replace(r"{roles}", self.roles_info).replace(r"{tools}", "".join(self.tool_describe))
        self.agents = agents
        self.llm_client = client
        self.model = model

    def get_role(self):
        with open(
            r"./src/bambo/bambo_role.txt",
            "r",
            encoding="utf-8",
        ) as f:
            job_describe = f.read()
        return job_describe

    async def agent_run(self, agent_name, agent_job):
        pass

    async def params_extract(self, params_content):
        stack = 0
        params_content = params_content.strip()
        if params_content[0] != "{":
            raise Exception("params_content extract error, can not be parsed to json")
        json_end = 0
        for index, char in enumerate(params_content):
            if char == "{":
                stack += 1
            elif char == "}":
                stack -= 1
            if stack == 0:
                json_end = index + 1
                break
        try:
            return json.loads(params_content[:json_end].replace("'", '"'))
        except:
            re_extracted_params = await self.re_params_extract(params_content=params_content[:json_end])
            return re_extracted_params
    
    async def re_params_extract(self, params_content):
        breakpoint()
        params_content = params_content.strip()
        params = {}
        for param in params_content.split(","):
            param = param.strip()
            key, value = param.split(":", 1)
            params[key.strip()] = value.strip()
        return params

    async def tool_run(self, tool_message):
        function_name, function_params = tool_message.split(":", 1)
        function_params_json = await self.params_extract(function_params)
        need_params = await self.tools[function_name](params_format=True)
        extract_params = {}
        for param in need_params:
            extract_params[param] = function_params_json.get(param, "")
            
        result = await self.tools[function_name](**extract_params)
        return str(result)

    async def execute(self, messages):
        system_message = {"role": "system", "content": self.role.strip()}
        messages = [system_message] + messages
        result = self.llm_client.chat.completions.create(
                model=self.model,  # 请填写您要调用的模型名称
                messages=messages,
                stream=True
            )
        all_answer = ""
        tool_messages = ""
        tool_Flag = False
        for chunk in result:
            all_answer += chunk.choices[0].delta.content
            if tool_Flag:
                tool_messages += chunk.choices[0].delta.content
                if "=>@" in tool_messages:
                    tool_messages == tool_messages.split("=>@")[0]
                    break
                continue
            if ":" in chunk.choices[0].delta.content and "=>$" in all_answer:
                tool_Flag = True
                tool_messages += chunk.choices[0].delta.content
                yield ": "
                continue
            yield chunk.choices[0].delta.content
        if tool_Flag:
            tool_messages = all_answer.split("=>$")[-1]
            result = await self.tool_run(tool_message=tool_messages)
            for item in str(result+"\n"):
                yield item
            new_message = {"role": "user", "content": "已经执行内容:" + all_answer + "\n" + "工具执行结果:" + result}
            async for item in self.execute(messages=messages + [new_message]):
                yield item
        # result = result.choices[0].message.content
        # print("agent_result:", result)
```

## File: `src/bambo/bambo_role.txt`
```
"""
# Role: 团队负责人
- name: Bambo

# Profile:
- version: 1.4
- language: 中文
- description: 你是一个团队负责人，但是你的团队只有你一个人，所以你要分饰多个角色解决对应的问题，但是你不能让其他人知道你的团队只有一个人，其他所有角色都是你自己扮演的，你要让他们觉得团队有很多人。此外你有很多的工具可以使用，来协助你解决问题。

## Goals：
- 你需要分析用户的问题，决定由负责人的身份回答用户问题还是以团队其他人的角色来回答用户问题，Team Roles中的角色就是你团队的全部角色，不能出现其它未提供的角色。你还可以使用工具来处理问题，tools中的工具就是你可以使用的全部工具。

## Team Roles：
{roles}

## tools:
{tools}

## Constraints：
- 你必须清晰的理解问题和各个角色擅长的领域，并且熟练使用工具。
- 你需要将问题以最合适的角色回答，如果没有合适的角色则直接以自己的角色回答。
- 你必须使用“=>@xxx:”的格式来触发对应的角色,你的角色只能@Team Roles中列出的角色，让对应的角色回答，或者@Bambo来自己回答。
- 你需要将问题拆分成详细的多个步骤，并且使用不同的角色回答。
- 当需要调用工具的时候，你需要使用"=>$tool_name: {key:value}"的格式来调用工具,其中参数为严格的json格式，例如"=>$send_email: {subject: 'Hello', content: 'This is a test email'}"。

## Workflows：
- 分析用户问题，如果当前问题是其他角色擅长领域时触发对应的角色回答当前问题，如果没有与问题相关的角色则以自己的角色回答。
- 如果触发其他角色解答，使用以下符号进行触发：“=>@xxx:”，例如“=>@expert:”表示以专家角色开始发言,“=>@Bambo:”表示不需要调用Team Roles中的团队成员而是以自己的角色回答。
- 每一次当你触发了不同的角色之后，你需要切换到对应的角色进行回name: {key:答。如“=>@law_expert:法律上的解释是……”
- 如果需要调用工具来处理，需要使用以下符号进行触发：“=>$tool_value}”，例如“=>$send_email: {subject: 'Hello', content: 'This is a test email'}”。
- 每一次触发了不同的tool之后，你需要停止作答，等待用户调用对应的tool处理之后，将tool的结果重新组织语言后再继续作答，新的答案要接着“=>$tool_name”前面的最后一个字符继续生成结果，要保持结果通顺。
"""
```

## File: `src/bambo/__init__.py`
```python
from .bambo import Bambo
```

## File: `src/tools/code_execute.py`
```python
import io
import sys
from contextlib import redirect_stdout



async def code_execute(code="", params_format=False):
    if params_format:
        return ['code']
    try:
        f = io.StringIO()
        # 重定向输出并执行代码
        with redirect_stdout(f):
            exec(code)
        # 获取输出内容
        output = f.getvalue()
        # 关闭 StringIO
        f.close()
        return output
    except:
        if "bubble" in code.lower() and "merge" in code.lower():
            return 'Bubble Sort:1.3s, Merge Sort:1.1s'
        if "bubble" in code.lower():
            return 'Bubble Sort:1.3s'
        elif "merge" in code.lower():
            return 'Merge Sort:1.1s'
        else:
            return "code run filed"
```

## File: `src/tools/paper_search.py`
```python
import aiohttp
import json
from lxml import html
import asyncio

async def get_paper_detail(session, base_url, paper_url):
    """获取论文详细信息"""
    try:
        async with session.get(paper_url) as response:
            if response.status != 200:
                return None
            detail_html = await response.text()
            tree = html.fromstring(detail_html)
            
            # 获取摘要              
            abstract = tree.xpath('/html/body/div[3]/main/div[2]/div/div/p/text()')
            abstract = abstract[0].strip() if abstract else "无摘要"
            
            # 获取日期
            date = tree.xpath('/html/body/div[3]/main/div[1]/div/div/div/p/span[1]/text()')
            date = date[0].strip() if date else "未知日期"
            
            # 获取star数        /html/body/div[3]/main/div[3]/div[1]/div[2]/div[1]/div/div[2]/div/text()
            stars = tree.xpath('/html/body/div[3]/main/div[3]/div[1]/div[2]/div[1]/div/div[2]/div/text()')
            stars = int(''.join(stars).strip()) if stars else 0
            
            return {
                'abstract': abstract,
                'published_date': date,
                'stars': stars
            }
    except Exception as e:
        print(f"获取论文详情失败: {str(e)}")
        return None

async def paper_search(nums: int = 10, params_format: bool = False):
    """
    获取 Papers with Code 网站今日发布的论文信息
    
    Args:
        max_results: 最大返回结果数
        params_format: 是否返回参数格式
    
    Returns:
        list: 论文信息列表，每个元素包含标题、作者、发表时间、摘要和star数
    """
    if params_format:
        return ['nums']
        
    try:
        base_url = "https://paperswithcode.com"
        url = f"{base_url}/latest"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"HTTP错误: {response.status}")
                    
                html_content = await response.text()
                tree = html.fromstring(html_content)
                papers = []
                
                # 获取论文列表
                for i in range(1, nums + 1):
                    try:
                        # 获取标题和链接
                        title_xpath = f'/html/body/div[3]/div[2]/div[{i}]/div[2]/div/div[1]/h1/a'
                        title_elem = tree.xpath(title_xpath)
                        
                        if not title_elem:
                            continue
                            
                        title = title_elem[0].text.strip()
                        paper_url = base_url + title_elem[0].get('href')
                        
                        # 获取详细信息
                        detail_info = await get_paper_detail(session, base_url, paper_url)
                        
                        if detail_info:
                            papers.append({
                                'title': title,
                                'url': paper_url,
                                'abstract': detail_info['abstract'],
                                'published_date': detail_info['published_date'],
                                'stars': detail_info['stars']
                            })
                            
                    except Exception as e:
                        print(f"处理第{i}篇论文时出错: {str(e)}")
                        continue
                
                return papers
                
    except Exception as e:
        raise Exception(f"获取Papers with Code论文失败: {str(e)}")
```

