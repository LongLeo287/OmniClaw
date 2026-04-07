---
id: SOPAI
type: knowledge
owner: OA_Triage
---
# SOPAI
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# SOPAi 🧠⚙️

> **SOP-as-Code platform with native MCP integration. Zero-hallucination guardrails for Enterprise AI Agents via strict state-machine routing.**

SOPAi is a next-generation Standard Operating Procedure (SOP) management platform built for both Humans and AI. By converting static text documents into dynamic, strictly enforced State Machines, SOPAi acts as the central "Rule Engine" for your enterprise. It ensures that internal AI Agents (customer service bots, AI sales, HR assistants) follow business logic with 100% accuracy, eliminating LLM hallucinations.

---

## 🚨 The Problem: Why RAG Fails for Business Logic
Throwing PDF manuals at an LLM via RAG (Retrieval-Augmented Generation) is dangerous for enterprise operations. 
* **Hallucinations:** AI might "bend the rules" if a customer is persuasive.
* **Context Loss:** Long text documents cause AI to miss crucial edge cases.
* **Lack of Control:** Management cannot confidently delegate critical tasks (like issuing refunds or granting system access) to an AI without absolute guardrails.

## 💡 The Solution: SOP-as-Code & MCP
SOPAi doesn't let AI "read" SOPs. It forces AI to **execute** them. 
Workflows are built as visual swimlanes, stored as JSON Schemas/State Machines, and exposed to AI Agents exclusively through the **Model Context Protocol (MCP)**. The AI only sees the *current step* and the *valid next actions*, stripping away its ability to make unauthorized decisions.

---

## ✨ Key Features

* 🌊 **Visual Swimlane Builder:** Drag-and-drop interface (powered by React Flow) to map out business processes. Clearly define the Actor (Human, System, or AI Agent) for every single node.
* 🤖 **AI Business Analyst Copilot:** As you design a flow, the built-in AI Copilot automatically scans the graph, identifies dead-ends, and forces you to define alternative flows (alt-flows) and edge cases to ensure 100% logic coverage.
* 🔌 **Native MCP Server:** Acts as a strictly typed API for your AI workforce. Agents call tools step-by-step (e.g., `start_sop`, `submit_step_data`), keeping their context window small and focused.
* 🎯 **Semantic Routing (Zero Keywords):** No need to hardcode trigger keywords. AI Agents use Vector Search and LLM Reasoning to match user intent with the correct SOP purpose dynamically.
* 🏢 **Enterprise-Ready & On-Premise:** Fully containerized. Deploy securely within your own infrastructure to protect sensitive company know-how.

---

## 🏗️ Architecture & Tech Stack

SOPAi is built for scalability, utilizing robust technologies to ensure high availability and data integrity:

* **Frontend:** React / Next.js / React Flow (for the visual graph builder).
* **Backend Core:** Node.js / Python (handling MCP Server protocols and State Machine logic).
* **Database:** PostgreSQL (for relational data, users, and SOP metadata).
* **Vector Store:** pgvector / MinIO (for storing embeddings and semantic routing).
* **Message Queue:** RabbitMQ (for handling async AI processing and step transitions).
* **Infrastructure:** Docker & Nginx (containerized for seamless self-hosted/on-premise deployment).

---

## 🚀 How It Works (The AI Agent Flow)

1. **Intent Matching:** A user sends a request (e.g., *"My shirt is torn, I want my money back"*).
2. **Semantic Discovery:** The Triage Agent calls the MCP `search_relevant_sop` tool. SOPAi's vector engine returns the ID for `SOP_DEFECTIVE_REFUND`.
3. **Execution Guardrails:** The Agent initiates the SOP. SOPAi returns **only** Step 1: *"Ask the user for their Order ID."*
4. **State Transition:** The Agent collects the ID, submits it via MCP. SOPAi's internal engine validates the business logic (e.g., *Is it within the 7-day return policy?*) and outputs the exact next instruction. The AI is securely "on the rails."

---

## 🛠️ Getting Started (Self-Hosted)

SOPAi is designed to be deployed internally to ensure maximum data privacy. 

### Prerequisites
* Docker & Docker Compose
* An OpenAI / Anthropic API Key (for the internal AI BA Copilot)

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-org/sopai.git](https://github.com/your-org/sopai.git)
   cd sopai
   ```
Dưới đây là bản nháp `README.md` hoàn chỉnh bằng tiếng Anh, được thiết kế theo chuẩn của các dự án công nghệ B2B/SaaS chuyên nghiệp trên GitHub. Tôi đã đưa vào các công nghệ phù hợp với kiến trúc hệ thống hiện đại (như Docker, PostgreSQL, RabbitMQ, React Flow) để bạn có thể sử dụng ngay.

2.  Configure environment variables:

    ```bash
    cp .env.example .env
    # Edit .env with your DB credentials and API keys
    ```

3.  Spin up the infrastructure via Docker:

    ```bash
    docker-compose up -d
    ```

4.  Access the web dashboard at `http://localhost:3000` to start building your first SOP.

-----

## 🗺️ Roadmap

  - [ ] Core Graph Builder & State Machine Engine
  - [ ] AI Business Analyst Copilot (Edge-case detection)
  - [ ] Basic MCP Tooling integration
  - [ ] Semantic Routing (Vector DB integration)
  - [ ] SOP Simulator (Test your flow with a mock AI agent in the UI)
  - [ ] Advanced Human-in-the-loop handoffs

-----

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details. For enterprise features and support, please check our commercial licensing options.

-----

*Architected and developed by Nguyễn Đức Minh.*

```

