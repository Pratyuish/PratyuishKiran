# AI Portfolio Projects

## Project 1 — Kubernetes RAG Troubleshooting Assistant

Purpose:
Answer Kubernetes troubleshooting questions using grounded internal-style runbooks.

Architecture:

Engineer → FastAPI → RAG Service → Vector Store → LLM

Data:
- Kubernetes runbooks
- operational guides
- incident notes
- architecture docs

Features:
- document ingestion
- chunking
- embeddings
- semantic retrieval
- grounded answers
- source references
- confidence / fallback behavior

Interview story:
Explain how grounding reduces hallucination and how retrieval quality is evaluated.

---

## Project 2 — AI SRE Incident Agent

Purpose:
Use tools to collect infrastructure evidence before suggesting actions.

Tools:
- list pods
- get logs
- get events
- describe deployment
- read metrics
- search runbook

Workflow:

Question → Agent → Tool Calls → Evidence → Reasoning → Recommendation

Safety:
- read-only by default
- no autonomous deletion/restart
- human approval for write actions
- audit every tool call

---

## Project 3 — Kubernetes MCP Server

Purpose:
Expose controlled Kubernetes operational capabilities using MCP.

Tools:
- list_clusters
- list_namespaces
- list_pods
- describe_pod
- get_logs
- get_events
- get_deployment_status
- get_helm_release

Production concerns:
- service-account RBAC
- namespace scoping
- authentication
- rate limits
- audit logs
- tenant isolation

---

## Project 4 — AI-Powered SRE Operations Platform

Purpose:
Create a flagship portfolio project combining AI with platform engineering.

Architecture:

Engineer
  ↓
Web / CLI
  ↓
AI SRE Copilot
  ├── RAG → Runbooks / Postmortems / Architecture Docs
  ├── Agents → Tool Calling / Investigation
  └── MCP → Kubernetes / AWS / CI-CD / Terraform
  ↓
Observability / Evaluation / Audit

Capabilities:
- incident investigation
- log analysis
- Kubernetes troubleshooting
- runbook recommendations
- CI/CD failure analysis
- Terraform review
- AWS troubleshooting
- change-risk summaries
- post-incident summaries

Production additions:
- Docker
- Helm
- Kubernetes
- Terraform
- GitOps / Argo CD
- OpenTelemetry
- dashboards
- RBAC
- secret management
- HA / DR
- cost tracking

Resume-friendly outcome after completion:

"Built a hands-on AI-powered SRE operations platform integrating RAG, LLM agents, MCP, Kubernetes and cloud tooling to investigate operational issues and provide grounded troubleshooting recommendations, with focus on security, observability and human-approved actions."
