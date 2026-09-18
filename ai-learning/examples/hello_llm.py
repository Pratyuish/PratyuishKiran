"""Minimal LLM learning example.

Set OPENAI_API_KEY in your environment before running.

This file intentionally stays small. Later modules should add:
- structured output
- retries/timeouts
- logging
- tracing
- tests
- FastAPI
- RAG
- tools/agents
"""

import os
from openai import OpenAI


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY before running this example.")

    client = OpenAI()

    response = client.responses.create(
        model="gpt-5.6",
        input=(
            "You are an SRE mentor. Explain Kubernetes CrashLoopBackOff "
            "in five concise troubleshooting steps."
        ),
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
