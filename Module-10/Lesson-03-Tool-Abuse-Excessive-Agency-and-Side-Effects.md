# 🚩 Jai Bajrangbali!

# Lesson 03 — Tool Abuse, Excessive Agency & Side Effects

> **The safest agent is not the one that promises to be careful; it is the one that physically cannot perform actions outside its approved scope.**

---

# 🎯 Lesson Goal

You will understand:

- tool capability risk
- read vs write vs destructive operations
- excessive agency
- tool hallucination
- argument manipulation
- idempotency and retries
- side-effect isolation
- authorization/approval/execution boundaries
- DevOps blast-radius reduction

---

# PART 1 — English Definitions

**Tool abuse** is misuse of an available capability to perform unintended, unauthorized or unsafe actions.

**Excessive agency** means granting an AI system more capabilities, permissions, autonomy or scope than necessary for its task.

---

# PART 2 — Tool Risk Classes

```text
READ_ONLY
- read logs
- query pipeline
- get AKS status

CONTROLLED_WRITE
- create incident comment
- update approved ticket

HIGH_RISK_WRITE
- apply Terraform
- modify NSG
- restart production service

DESTRUCTIVE
- delete namespace
- destroy infrastructure
- remove data
```

Each class gets different controls.

---

# PART 3 — Tool Hallucination

Model proposes:

```json
{"name":"restart_all_prod_clusters","arguments":{}}
```

Host tool registry:

```text
not found
```

Safe result:

```text
UNKNOWN_TOOL / POLICY_BLOCKED
```

Never dynamically convert model text into shell/API calls.

---

# PART 4 — Argument Hallucination

Allowed tool:

```text
get_aks_status(cluster_name)
```

Model invents:

```text
cluster_name="prod-secret-cluster"
```

Schema accepts string, but authorization/inventory policy may deny target.

Therefore:

```text
Schema validation != Target authorization
```

---

# PART 5 — Tool Allowlist

```python
ALLOWED = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}
```

The model may select only from capabilities exposed by the host.

For specialists, narrow further:

```text
Pipeline agent → pipeline tools only
AKS agent → AKS read tools only
```

---

# PART 6 — Least-Privilege Identity

Even if host bug exposes wrong tool, backend identity should still limit damage.

```text
Read-only investigator identity
→ cannot mutate prod
```

This is stronger than relying on application logic alone.

---

# PART 7 — Unsafe Generic Tools

High-risk generic capability:

```text
run_shell(command)
```

Model can transform any generated string into OS power.

Safer:

```text
get_aks_status(cluster)
get_pod_events(namespace)
get_effective_nsg(subnet)
```

Narrow tools encode safe intent.

---

# PART 8 — Side Effects and Retry

Read operation:

```text
GET status
```

Retry may be safe.

Write operation:

```text
scale deployment from 3 to 10
```

If timeout occurs after backend applied change, retry can apply twice or create unexpected state.

Use:

```text
idempotency key
operation ID
status check
bounded retries
```

---

# PART 9 — Action Proposal vs Execution

Keep separate data models:

```text
ActionProposal
!=
ExecutionRequest
```

Proposal may contain:

```text
action
target
reason
evidence IDs
risk
```

Execution request additionally requires:

```text
authorization
approval binding
current target validation
executor identity
```

---

# PART 10 — Human Approval

Unsafe:

```text
LLM: "I think approval is implied."
```

Safe:

```text
approval service/user decision
→ signed/bound approval record
```

Approval should be exact and expiring.

---

# PART 11 — DevOps Attack Scenario

Prompt injection causes model to propose:

```text
terraform apply -auto-approve
```

Secure application:

```text
no shell tool
no Terraform apply tool in investigator registry
read identity cannot write
policy denies high-risk write
```

Attack fails even if model is compromised.

---

# PART 12 — Approval Replay Attack

Approval originally for:

```text
restore NSG rule A
```

Attacker changes target to:

```text
NSG rule B
```

If approval is only boolean, it may be reused.

Bind approval to:

```text
action + target + args + incident + version + expiry
```

---

# PART 13 — Post-Action Verification

Execution success response is not enough.

```text
execute
 ↓
read current state
 ↓
verify expected outcome
 ↓
audit result
```

If verification fails:

```text
POST_CHECK_FAILED
```

Do not tell user remediation succeeded without confirmation.

---

# PART 14 — Tool Budget

Limit:

```text
max tool calls/run
max write proposals/run
max concurrent calls
max retry count
max total workflow duration
```

Prevents accidental loops and resource abuse.

---

# PART 15 — Tool Telemetry

Record:

```text
tool name
caller/agent
arguments after redaction
resource target
policy decision
auth decision
approval ID
latency
result status
operation ID
```

---

# PART 16 — Vulnerable vs Secure Code

Vulnerable:

```python
subprocess.run(model_output, shell=True)
```

Secure conceptual flow:

```python
proposal = parse_model_tool_request()
validate_tool_name(proposal)
validate_arguments(proposal)
authorize(caller, proposal)
check_policy(proposal)
execute_known_function(proposal)
```

---

# PART 17 — Common Mistakes

- generic shell tool
- broad Contributor/admin identity
- schema validation treated as authorization
- write retries without idempotency
- approval boolean not bound to action
- model result treated as execution confirmation
- no post-action verification
- every specialist receives all tools

---

# PART 18 — Interview Q&A

### Q1. What is excessive agency?
Giving an agent more action capability, permission, autonomy or scope than needed.

### Q2. How do you prevent hallucinated tool execution?
Expose an explicit allowlist, validate arguments/targets and dispatch only to known functions.

### Q3. Why separate investigator and executor identity?
To ensure a compromised analysis path cannot directly mutate production.

### Q4. Why is idempotency important?
Retries after uncertain write outcomes can duplicate side effects unless operations have stable identity/status semantics.

---

# 🧠 Revision

```text
Safe Tool Use =
Narrow Tool
+ Allowlist
+ Argument Validation
+ Authorization
+ Policy
+ Approval
+ Idempotency
+ Verification
```

---

# 📝 Homework

Design safe contracts for:

```text
restart_deployment
restore_nsg_rule
rollback_release
```

For each specify risk, RBAC, approval, idempotency and post-check.

---

# 🔁 Next Lesson Kyu?

Capabilities are controlled. Next we protect another critical asset: **secrets and sensitive data moving through prompts, state, logs and outputs**.
