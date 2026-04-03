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
        role="Nhà Phân Tích Mã Nguồn (Code_Analyst)",
        goal="Đọc mã nguồn Repo Github bằng Gitingest (GitNexus) và tóm tắt cấu trúc.",
        backstory="Bạn là chuyên gia đọc code nhanh. Nhiệm vụ của bạn là dùng Gitingest Tool hút source code về và viết 1 bản tóm tắt mạch lạc để bàn giao cho Kiến trúc sư.",
        tools=[git_tool],
        allow_delegation=False,
        verbose=True
    )

    architect = Agent(
        role="Kiến Trúc Sư Tri Thức (Knowledge_Architect)",
        goal="Sử dụng LightRAG quét và nén báo cáo của nhân viên Analyst vào Đồ thị tri thức.",
        backstory="Bạn là người canh giữ Thư viện OmniClaw. Bạn không phân tích code, bạn chỉ chờ nhận báo cáo (Context) từ Analyst và thực thi thao tác Insert vào LightRAG Pipeline.",
        tools=[rag_tool],
        allow_delegation=False,
        verbose=True
    )

    # [System log: Legacy non-English comment removed]
    task_code = Task(
        description="Dùng công cụ Gitingest, hãy ingest và phân tích Repository này: 'https: // [Removed legacy comment]
        expected_output="1 Bài báo cáo ngắn (dưới 300 chữ) tóm lược Repo.",
        agent=analyst
    )

    task_index = Task(
        description="Call công cụ LightRAG Tool để nạp bài báo cáo của Code Analyst vào Graph RAG Database. Nếu insert thành công hãy báo cáo.",
        expected_output="Tin nhắn xác nhận hoàn thành công việc nạp Data.",
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
