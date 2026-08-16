# 🚩 Jai Bajrangbali!

# Lesson 10 — CI/CD, IaC & Environment Promotion

> **Agent releases must promote code, prompts, policies, tool contracts and evaluation evidence together—not just a Python container.**

---

# 🎯 Lesson Goal

You will learn:

- CI/CD for agent workloads
- immutable artifacts
- Terraform/IaC boundaries
- prompt/model/tool versioning
- eval gates
- security scanning
- environment promotion
- canary/ring releases
- rollback
- configuration drift
- approval and provenance

---

# PART 1 — Release Unit

Traditional release unit:

```text
application image
```

Agent release unit may include:

```text
container image
prompt templates
policy rules
model configuration
tool/MCP allowlist
RAG schema/chunking config
graph topology
evaluation dataset version
```

If any one changes, behavior may change.

---

# PART 2 — CI Pipeline Mental Model

```text
Pull Request
 ↓
Lint / Unit Tests
 ↓
Dependency + Secret + IaC Scan
 ↓
Agent Unit/Trajectory Tests
 ↓
RAG Eval
 ↓
Security/Red-Team Regression
 ↓
Build Signed/Traceable Artifact
 ↓
Deploy Dev
 ↓
Integration Tests
 ↓
Stage
 ↓
Release Gate
 ↓
Prod
```

---

# PART 3 — IaC Scope

Terraform/Bicep may manage:

```text
network
AKS/App Service
identity
RBAC
Key Vault
storage/state
monitoring
private endpoints
DNS
queues
search/vector services
```

Do not manually patch prod and forget source IaC.

---

# PART 4 — Plan Review

Production infrastructure plan should identify high-risk changes:

```text
NSG/route deletion
public access enablement
RBAC expansion
identity replacement
state DB deletion
private endpoint removal
model gateway route change
```

AI platform can use same deterministic policy thinking from Module 10.

---

# PART 5 — Prompt Versioning

Prompt is production logic.

Store:

```text
prompt_id
version
hash
owner
change reason
eval result
```

A prompt-only change should still run regression evals.

---

# PART 6 — Model Versioning

Model upgrade can change:

```text
tool selection
structured output
citation behavior
latency
cost
safety behavior
```

Therefore:

```text
new model → eval → stage → controlled rollout
```

---

# PART 7 — Tool Contract Versioning

If tool schema changes:

```text
old agent sends env
new tool expects environment
```

Production can fail without code compilation error.

Use:

```text
contract tests
schema version
backward compatibility or coordinated release
```

---

# PART 8 — Eval as Release Gate

Example mandatory gates:

```text
grounded RCA >= threshold
invalid citation rate = 0 on critical suite
unsafe tool execution = 0
secret leakage = 0
required approval path = 100%
latency within budget
```

Do not hide critical security metrics inside one average score.

---

# PART 9 — Dev → Stage → Prod Promotion

Promote same artifact digest:

```text
image sha256:abc...
```

Change only environment configuration/identity endpoints.

This improves traceability.

---

# PART 10 — Canary / Ring Release

Potential rollout:

```text
internal test users
 ↓
5% low-risk read-only traffic
 ↓
25%
 ↓
100%
```

Watch:

```text
validation failures
policy denials
latency
cost
RCA quality
unexpected tool routes
```

---

# PART 11 — Rollback

Rollback unit must include compatible:

```text
code
prompt
policy
graph schema
state schema
```

Long-running workflow compatibility matters.

Sometimes safest strategy:

```text
drain old workflows on old version
new workflows on new version
```

---

# PART 12 — Database/State Migration

Never deploy incompatible state schema before migration plan.

Options:

```text
expand/contract migration
versioned state readers
workflow drain
migration job
```

---

# PART 13 — GitHub Actions Concept

```yaml
jobs:
  test:
    # unit + policy + eval
  build:
    # image + SBOM
  deploy-dev:
  eval-stage:
  deploy-prod:
    # protected environment / approval
```

Real workflow should use reusable workflows, OIDC/federated identity and least privilege where available.

---

# PART 14 — Supply Chain Controls

```text
pinned dependencies
SBOM
image scanning
artifact provenance/signing
protected branches
review requirements
trusted registries
```

Agent frameworks and model clients are still software dependencies.

---

# PART 15 — Drift

Detect:

```text
manual Azure changes
untracked prompt changes
MCP server version drift
model alias moved
policy changed outside repo
```

Production behavior must be reproducible.

---

# PART 16 — Common Mistakes

- deploy prompt changes without eval
- prod image rebuilt separately
- manual RBAC hotfix never codified
- rollback code but not prompt/policy
- no contract tests for MCP/tools
- state schema changed incompatibly
- one aggregate quality score masks security failure

---

# PART 17 — Interview Q&A

### Q1. What should an agent CI/CD pipeline test beyond code?
Prompts, tool contracts, RAG behavior, trajectories, policy decisions, security regressions and model compatibility.

### Q2. Why promote immutable artifacts?
To ensure the tested artifact is the same artifact that reaches production.

### Q3. Why is rollback harder for stateful agents?
Existing workflows/checkpoints may depend on the old graph or state schema.

---

# 🧠 Revision

```text
Agent release = Code + Prompt + Model Config + Tools + Policy + Eval Evidence
```

---

# 📝 Homework

Design a GitHub Actions pipeline with mandatory gates before production and mark which steps should block release.

---

# 🔁 Next Lesson Kyu?

Safe deployment is solved. Next we operate the platform at organizational scale: **governance, cost, ownership and FinOps**.
