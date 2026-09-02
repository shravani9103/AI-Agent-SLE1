# ADR 1: Selection of Tech Stack for Basic AI Agent

## Status

Accepted

## Date

02 September 2026

## Context

The AI-Augmented Workflow course project requires the development of a basic AI-related agent and documentation of the development process.

The project should be simple enough for a beginner to understand, test, and maintain. It should also support the use of AI-assisted development tools and version control.

The initial version of the project uses a simple rule-based AI Agent. The agent accepts user input, checks predefined rules, and returns an appropriate response.

## Decision

The following technologies and tools were selected:

| Technology / Tool | Purpose |
|---|---|
| Python | Main programming language |
| Visual Studio Code | Code editor and development environment |
| Git | Version control |
| GitHub | Repository hosting and project sharing |
| Markdown | Project documentation |
| Python Virtual Environment | Isolated project environment |

The initial AI Agent will use a rule-based approach rather than requiring an external AI API.

Future versions may integrate an LLM such as the OpenAI API or a local model through Ollama.

## Why Python?

Python was selected because:

- It is beginner-friendly.
- It has simple and readable syntax.
- It is widely used in Artificial Intelligence and Machine Learning.
- It has a large ecosystem of AI and machine-learning libraries.
- AI-assisted coding tools can easily generate and explain Python code.

## Why a Rule-Based Agent for the Initial Version?

A rule-based agent provides a simple way to demonstrate the basic concept of an AI Agent without requiring an API key or external service.

The agent receives user input, evaluates predefined conditions, and selects a response.

This makes the first version:

- Easy to understand
- Easy to test
- Easy to debug
- Free from API costs
- Suitable for demonstrating basic agent behaviour

## AI-Assisted Coding Compatibility

AI tools can be used to support the development process by:

- Explaining Python concepts
- Suggesting code
- Explaining errors
- Helping with debugging
- Improving documentation
- Suggesting project structure
- Helping create test cases

However, AI-generated code must be reviewed and tested by the student before it is accepted into the project.

AI assistance will be documented in `AI_Contribution_Log.md`.

The student remains responsible for understanding the code, checking its correctness, testing the program, and making the final project decisions.

## Consequences

### Positive Consequences

- Python makes the project easy to understand.
- The rule-based agent has no external API dependency.
- The project can run locally.
- Git and GitHub provide version control.
- Markdown makes documentation simple.
- The project can later be extended with an LLM.
- AI-assisted development can help with learning and debugging.

### Negative Consequences

- The rule-based agent has limited language understanding.
- Responses depend on predefined rules.
- An OpenAI API integration would introduce API costs and API-key security requirements.
- Local AI models such as Ollama may require additional computer resources.
- AI-generated code can contain mistakes and must be reviewed.

## Alternatives Considered

### Java

Java was considered but not selected because Python provides simpler syntax and is more convenient for this beginner-level AI project.

### C/C++

C and C++ were not selected because they require more low-level programming and would add unnecessary complexity for this project.

### OpenAI API as the Initial Implementation

The OpenAI API was considered for the first version but was not selected initially because it would require API credentials and an external service.

It remains a possible future enhancement.

### Ollama as the Initial Implementation

Ollama was also considered because it can support local AI models. It was not selected for the first version because the basic rule-based implementation is simpler and requires fewer dependencies.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| AI-generated code may contain errors | Test and review all generated code |
| Student may depend too heavily on AI | Understand and explain the final code |
| API keys could be exposed in future | Store secrets in environment variables and exclude `.env` using `.gitignore` |
| Rule-based agent has limited capabilities | Document limitations and plan future improvements |
| Local AI models may require high resources | Use them only when the computer can support them |

## Final Decision

Python, Visual Studio Code, Git, GitHub, Markdown, and a Python virtual environment were selected for the project.

A simple rule-based AI Agent will be used for the initial implementation. The architecture allows future integration with an OpenAI API or Ollama if required.

The project will use AI-assisted development responsibly, with AI contributions documented and all generated code reviewed and tested by the student.