# Detailed AI Learning Modules

## Module 1 — LLM & Generative AI Fundamentals

Learn:
- Tokens and tokenization
- Context windows
- Transformer concepts
- Inference
- Temperature and deterministic output
- Hallucination
- Grounding
- Embeddings
- RAG vs fine-tuning
- Hosted vs open-weight models

Interview outcomes:
- Explain why LLMs hallucinate
- Explain embeddings in simple terms
- Compare RAG and fine-tuning
- Explain context-window limitations
- Discuss latency, cost and accuracy trade-offs

Hands-on:
- Call an LLM API
- Compare outputs at different temperatures
- Measure prompt and response tokens
- Return structured JSON output

---

## Module 2 — Prompt Engineering & Structured Outputs

Learn:
- System, developer and user prompts
- Zero-shot and few-shot prompting
- Prompt templates
- Role prompting
- Structured outputs
- JSON schemas
- Prompt injection
- Context management
- Guardrails

Hands-on:
- Create a Kubernetes troubleshooting prompt
- Force structured JSON responses
- Add validation with Pydantic
- Test malicious / irrelevant input

---

## Module 3 — Python for AI Applications

Focus areas:
- Virtual environments
- requests / httpx
- async / await
- FastAPI
- Pydantic
- environment variables
- logging
- error handling
- retries
- testing
- API design

Hands-on:
- Build a FastAPI wrapper around an LLM
- Add health checks
- Add timeout/retry logic
- Add structured logging
- Write unit tests

---

## Module 4 — Embeddings, Vector Search & RAG

Learn:
- Embedding models
- Semantic search
- Vector similarity
- Chunking
- Chunk overlap
- Metadata
- Top-k retrieval
- Hybrid search
- Reranking
- Citation / source grounding
- Evaluation

Pipeline:

Documents → Chunking → Embeddings → Vector Store → Retrieval → Prompt → LLM

Hands-on:
- Ingest Kubernetes runbooks
- Store embeddings
- Search semantically
- Return source-grounded answers
- Evaluate retrieval relevance

---

## Module 5 — AI Agents & Tool Calling

Learn:
- Agent loop
- Tool/function calling
- Tool schemas
- Planning
- State
- Memory
- Handoffs
- Human approval
- Multi-agent workflows

Hands-on tools:
- get_pods()
- get_pod_logs()
- get_events()
- get_deployment()
- get_cpu_metrics()
- get_memory_metrics()
- search_runbook()

Safety rule:
Start with read-only tools. Add write operations only after approval, RBAC, audit and blast-radius controls.

---

## Module 6 — Model Context Protocol (MCP)

Learn:
- MCP architecture
- Client / server model
- Tools
- Resources
- Prompts
- Transport
- Authentication
- Authorization
- Enterprise access control

Hands-on:
Build a Kubernetes MCP server exposing:
- list_clusters
- list_namespaces
- list_pods
- describe_pod
- get_logs
- get_events
- get_deployment_status
- get_helm_release

---

## Module 7 — AWS Bedrock & Enterprise GenAI

Learn:
- Amazon Bedrock
- Foundation model selection
- Knowledge bases / retrieval
- Guardrails
- Agents / AgentCore concepts
- IAM
- KMS
- VPC/private access patterns
- Cost governance
- Logging and auditing

Hands-on:
- Build a small Bedrock-backed assistant
- Compare provider/model behavior
- Design private enterprise connectivity

---

## Module 8 — LLMOps & AI Observability

Learn:
- Prompt/version management
- Evaluation datasets
- Regression testing
- Tracing
- Token usage
- Latency
- Cost
- Error rates
- Model quality
- Feedback loops
- CI/CD for AI applications

Metrics:
- request count
- p50/p95 latency
- input/output tokens
- cost per request
- retrieval hit quality
- tool-call success rate
- hallucination / groundedness score

---

## Module 9 — AI Security, Guardrails & Governance

Learn:
- Prompt injection
- Data exfiltration
- Secrets leakage
- Unsafe tool execution
- Tenant isolation
- RBAC
- Auditability
- PII handling
- Model/data governance
- Human-in-the-loop controls

Design principle:
AI agents should have the minimum privileges required to complete a task.

---

## Module 10 — Production AI Architecture

Be able to design:
- API gateway
- authN/authZ
- model gateway
- RAG service
- vector database
- caching
- agents
- tool layer
- MCP servers
- observability
- guardrails
- HA/DR
- rate limiting
- cost controls

Interview topics:
- multi-region AI service
- failure isolation
- model fallback
- provider outage
- cost spikes
- data residency
- auditability

---

## Module 11 — AI for SRE / Platform Engineering

Use cases:
- incident triage
- log summarization
- runbook search
- Kubernetes troubleshooting
- change-risk analysis
- CI/CD failure diagnosis
- Terraform review
- postmortem generation
- alert enrichment
- capacity-analysis assistance

Goal:
Combine AI with existing operational expertise instead of building generic demos.

---

## Module 12 — Senior-Level AI Interview Preparation

Prepare architecture answers for:
- enterprise RAG for 10,000 users
- secure AI agent with Kubernetes access
- AI observability platform
- multi-model strategy
- reducing hallucination
- private enterprise data integration
- disaster recovery for AI services
- AI governance and audit
- cost optimization
- safe automated remediation

Use this answer structure:
1. Requirements
2. Constraints
3. Architecture
4. Security
5. Reliability
6. Observability
7. Cost
8. Failure modes
9. Trade-offs
10. Rollout plan
