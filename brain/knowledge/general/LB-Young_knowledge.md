---
id: lb-young-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:03.769013
---

# KNOWLEDGE EXTRACT: LB-Young
> **Extracted on:** 2026-03-30 17:40:13
> **Source:** LB-Young

---

## File: `Bambo.md`
```markdown
# 📦 LB-Young/Bambo [🔖 PENDING/APPROVE]
🔗 https://github.com/LB-Young/Bambo


## Meta
- **Stars:** ⭐ 33 | **Forks:** 🍴 2
- **Language:** Python | **License:** MIT
- **Last updated:** 2025-12-03
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Bambo is a new proxy framework. Compared with mainstream frameworks, it is more lightweight and flexible and can handle various load tasks.

## README (trích đầu)
```
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
- query:"请根据以下参考信息回答问题：\n{reference}\n\n问题：以采访对话形式介绍
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

