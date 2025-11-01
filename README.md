# 🧪 AI Test Intelligence Assistant  
Automated, risk-aware test planning for modern QA teams.

## 🚀 Overview
AI Test Intelligence demonstrates how an AI-augmented QA Lead / SDET can use Large Language Models (LLMs) and LangChain to:
- Extract testable requirements from a user story.
- Perform structured risk analysis (security, stability, compliance).
- Generate BDD-style Gherkin scenarios.
- Prioritize tests into SMOKE / REGRESSION / NIGHTLY for release gates.

This is not “let GPT write my tests.”
This is: **inject intelligence into the QA process and make release decisions faster.**

The example provided is based on a realistic user story: *Login with MFA, lockout after 3 failed attempts, OTP via SMS, audit trail.*

---

## 🔄 Workflow

```text
User Story (Jira / Markdown)
        ↓
Requirements Extraction
        ↓
Risk Analysis (JSON matrix)
        ↓
Gherkin Scenario Generation
        ↓
Test Plan Prioritization (SMOKE / REGRESSION / NIGHTLY)
        ↓
Ready-to-use QA evidence
