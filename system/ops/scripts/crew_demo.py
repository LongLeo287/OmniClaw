import os
import sys

# ==========================================
# [System log: Legacy non-English comment removed]
# ==========================================
os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"
os.environ["OPENAI_API_KEY"] = "ollama"
os.environ["OPENAI_MODEL_NAME"] = "gemma2:2b"

# [System log: Legacy non-English comment removed]
sys.path.append(os.environ.get("OMNICLAW_ROOT", "."))
from crewai import Agent, Task, Crew, Process
from plugins.crewai_tools_bridge import GitingestTool, LightRAGTool

def run_crew():
    print("[OmniClaw System Event]")
    print("----------------------------------------------------------")

    # [System log: Legacy non-English comment removed]
    git_tool = GitingestTool()
    rag_tool = LightRAGTool()

    # [System log: Legacy non-English comment removed]
    analyst = Agent(
        role="NhÃ  PhÃ¢n TÃ­ch MÃ£ Nguá»“n (Code_Analyst)",
        goal="Äá»c mÃ£ nguá»“n Repo Github báº±ng Gitingest (GitNexus) vÃ  tÃ³m táº¯t cáº¥u trÃºc.",
        backstory="Báº¡n lÃ  chuyÃªn gia Ä‘á»c code nhanh. Nhiá»‡m vá»¥ cá»§a báº¡n lÃ  dÃ¹ng Gitingest Tool hÃºt source code vá» vÃ  viáº¿t 1 báº£n tÃ³m táº¯t máº¡ch láº¡c Ä‘á»ƒ bÃ n giao cho Kiáº¿n trÃºc sÆ°.",
        tools=[git_tool],
        allow_delegation=False,
        verbose=True
    )

    architect = Agent(
        role="Kiáº¿n TrÃºc SÆ° Tri Thá»©c (Knowledge_Architect)",
        goal="Sá»­ dá»¥ng LightRAG quÃ©t vÃ  nÃ©n bÃ¡o cÃ¡o cá»§a nhÃ¢n viÃªn Analyst vÃ o Äá»“ thá»‹ tri thá»©c.",
        backstory="Báº¡n lÃ  ngÆ°á»i canh giá»¯ ThÆ° viá»‡n OmniClaw. Báº¡n khÃ´ng phÃ¢n tÃ­ch code, báº¡n chá»‰ chá» nháº­n bÃ¡o cÃ¡o (Context) tá»« Analyst vÃ  thá»±c thi thao tÃ¡c Insert vÃ o LightRAG Pipeline.",
        tools=[rag_tool],
        allow_delegation=False,
        verbose=True
    )

    # [System log: Legacy non-English comment removed]
    task_code = Task(
        description="DÃ¹ng cÃ´ng cá»¥ Gitingest, hÃ£y ingest vÃ  phÃ¢n tÃ­ch Repository nÃ y: 'https: // [Removed legacy comment]
        expected_output="1 BÃ i bÃ¡o cÃ¡o ngáº¯n (dÆ°á»›i 300 chá»¯) tÃ³m lÆ°á»£c Repo.",
        agent=analyst
    )

    task_index = Task(
        description="Call cÃ´ng cá»¥ LightRAG Tool Ä‘á»ƒ náº¡p bÃ i bÃ¡o cÃ¡o cá»§a Code Analyst vÃ o Graph RAG Database. Náº¿u insert thÃ nh cÃ´ng hÃ£y bÃ¡o cÃ¡o.",
        expected_output="Tin nháº¯n xÃ¡c nháº­n hoÃ n thÃ nh cÃ´ng viá»‡c náº¡p Data.",
        agent=architect,
        context=[task_code]
    )

    # [System log: Legacy non-English comment removed]
    ai_os_crew = Crew(
        agents=[analyst, architect],
        tasks=[task_code, task_index],
        process=Process.sequential,
        verbose=True
    )

    # [System log: Legacy non-English comment removed]
    result = ai_os_crew.kickoff()

    print("[OmniClaw System Event]")
    print("===================================")
    print(result)
    print("===================================")

if __name__ == "__main__":
    run_crew()
