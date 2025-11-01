# 🧪 AI Test Intelligence Assistant  
_Automated, AI-powered test planning pipeline for modern QA teams._

## 📖 Overview

**AI Test Intelligence** is a proof-of-concept project that demonstrates how **Artificial Intelligence can assist Quality Assurance (QA)** engineers in the early stages of test design.  
It uses **LangChain** and **OpenAI GPT models** to automatically generate a structured **test plan** from a simple *user story* or product requirement.

Instead of manually writing test cases, the assistant performs four intelligent steps:

1. **Extract testable requirements** from the story.  
2. **Analyze potential risks** (security, compliance, stability, UX).  
3. **Generate BDD (Gherkin) test scenarios**.  
4. **Prioritize tests** into *Smoke*, *Regression*, and *Nightly* categories.

This enables QA teams to:
- Start testing earlier (“Shift Left” approach),
- Maintain consistent test documentation,
- Identify risks and coverage gaps faster,
- Communicate better with developers and product owners.

## 🔄 Workflow

```text
User Story  →  Requirements Extraction
                  ↓
               Risk Analysis (JSON)
                  ↓
             Gherkin Test Generation
                  ↓
          Test Plan Prioritization
                  ↓
          Ready-to-use QA Deliverables
```

Each step is powered by a dedicated LangChain “chain”, which structures the LLM prompts, input, and output in a reproducible way.

## ⚙️ Technical Stack

| Component | Purpose |
|------------|----------|
| **Python 3.11+** | Main runtime |
| **LangChain** | Workflow orchestration |
| **OpenAI GPT-4o / GPT-4o-mini** | Natural language generation |
| **dotenv** | Secure environment variable management |
| **Markdown / JSON / Gherkin outputs** | Human-readable QA deliverables |

## 🧠 Generated Outputs (Detailed Explanation)

After running the assistant, four files are created under `src/output/`.  
Each file corresponds to a key artifact in a QA process.

### 1️⃣ `generated_requirements.md` – Extracted Testable Requirements

Transforms a user story into a structured list of **functional** and **implicit business rules**.

### 2️⃣ `risk_matrix.json` – Risk Analysis Matrix

Lists potential risks extracted from the requirements, with **category**, **probability**, **severity**, and **QA focus**.

### 3️⃣ `generated_tests.feature` – Gherkin Test Scenarios

Contains **BDD-style scenarios** (`Given/When/Then`) generated directly from the extracted requirements and identified risks.

### 4️⃣ `priority_plan.md` – Test Plan Prioritization

Groups all generated scenarios by their **execution priority**:
- **SMOKE** → Must pass for a release to go live.  
- **REGRESSION** → Verified every sprint to ensure stability.  
- **NIGHTLY** → Broader coverage, non-blocking tests.

## 🧱 Folder Structure

```text
ai-test-intelligence/
├── README.md
├── requirements.txt
├── LICENSE
├── .env.example
├── src/
│   ├── main.py
│   ├── data/
│   ├── output/
│   ├── chains/
│   ├── models/
│   └── utils/
```

## 🚀 How to Run Locally

### 1️⃣ Setup environment

```bash
pip install -r requirements.txt
```

### 2️⃣ Configure `.env`

Create a `.env` file at the project root with:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
MODEL_NAME=gpt-4o-mini
```

### 3️⃣ Run the pipeline

```bash
python src/main.py --input ./src/data/sample_ticket_login.md
```

### 4️⃣ Check results

All outputs will be generated in `src/output/`.

## 🧠 Key Takeaways

| Step | Output File | Purpose |
|------|--------------|----------|
| Requirements Extraction | `generated_requirements.md` | Defines the test scope and acceptance criteria |
| Risk Analysis | `risk_matrix.json` | Prioritizes QA focus areas based on risk |
| Test Generation | `generated_tests.feature` | Produces executable BDD scenarios |
| Prioritization | `priority_plan.md` | Builds a test execution strategy for release gates |

## 👤 Author

**David Garcia**  
AI-Augmented Software Engineer / Senior QA Automation Engineer  
Specialized in **Python, CI/CD, and AI-driven QA workflows**

📧 mail.garcia.david@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/david-garcia-qa/)

## 📜 License

MIT License © 2025 David Garcia  
_For educational and demonstration purposes only._

