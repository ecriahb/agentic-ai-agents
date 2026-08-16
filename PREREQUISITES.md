# Course Prerequisites & Setup Checklist

This course is designed for AI beginners. You do **not** need prior LLM, LangChain, MCP or agent experience.

---

# Required Baseline

## Operating system

Examples are written to be understandable on Windows/PowerShell, but most Python code is portable.

## Python

Use **Python 3.10 or newer**.

Why 3.10+?

- current MCP Python SDK v2 requires Python 3.10+
- current OpenAI Python SDK supports modern Python versions
- later LangGraph/LangChain labs are cleaner on a current Python runtime

Verify:

```powershell
python --version
```

---

# Git

Recommended:

```powershell
git --version
```

Clone:

```powershell
git clone https://github.com/ecriahb/agentic-ai-agents.git
cd agentic-ai-agents
```

---

# Virtual Environment

Create one environment for the course:

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

You may also create a separate environment per module if you want stricter dependency isolation.

---

# Local LLM Track

Install Ollama and verify:

```powershell
ollama --version
```

Recommended model for new parity labs:

```powershell
ollama pull qwen3:4b
```

Some historical V10 labs use:

```powershell
ollama pull qwen2.5:3b
```

Small early-course alternative:

```powershell
ollama pull gemma3:1b
```

You do not need every model on day one. Pull a model when the specific lab needs it.

---

# OpenAI Track

Install the current course SDK range through module/shared requirements.

Set:

```powershell
$env:OPENAI_API_KEY="your-key"
$env:OPENAI_MODEL="gpt-5.6-luna"
$env:LLM_PROVIDER="openai"
```

Never commit keys.

Hosted API usage can require billing/credits and network access.

---

# Shared Provider Setup

```powershell
pip install -r shared/requirements.txt
python shared/preflight.py
python shared/provider_smoke_test.py
```

Default provider if `LLM_PROVIDER` is not set:

```text
ollama
```

---

# Module Dependencies

Install a module's requirements before its code labs:

```powershell
pip install -r Module-5/examples/requirements.txt
```

Replace `Module-5` with the module you are studying.

---

# What Is NOT Required at the Beginning

You do not need:

```text
Azure subscription
AKS cluster
Terraform production environment
GitHub Actions production project
paid LLM API
vector database server
MCP remote server
```

The course deliberately uses local/simulated evidence first.

Real production integration comes only after the contracts, security and evaluation concepts are understood.

---

# Beginner Preflight

Run:

```powershell
python shared/preflight.py
```

It checks:

- Python version
- shared Python dependencies
- provider selection
- Ollama API/model availability for local path
- OpenAI key presence for hosted path

It intentionally does **not** make an OpenAI API call.

---

# Recommended Hardware for Local Models

Local model speed depends heavily on RAM/CPU/GPU and model size.

If `qwen3:4b` is too slow for your laptop, use a smaller model for basic concept experiments and use OpenAI only when you specifically want hosted-provider comparison.

Course architecture should not depend on a specific model being fast on every machine.

---

# Important Security Setup

Create `.gitignore` entries for local secrets/venvs if not already present:

```text
.env
.venv/
__pycache__/
```

Never store:

```text
OpenAI API key
Azure client secret
GitHub token
kubeconfig credentials
Terraform secrets
```

inside prompts or committed example files.

---

# Definition of Ready

You are ready for Module 1 practicals when:

- [ ] Python 3.10+ works
- [ ] virtual environment activates
- [ ] pip works
- [ ] repository cloned
- [ ] one model path selected
- [ ] Ollama local API works **or** OpenAI key is configured
- [ ] `python shared/preflight.py` shows no blocking setup issue for your selected path

Module 0 can be studied before any of these technical setup steps.
