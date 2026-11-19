# Day 06 – Prompt Engineering with Groq API

## Overview

Today's learning focuses on **Prompt Engineering and LLM-based Text Classification** using Python and the Groq API.

The project demonstrates how to communicate with a Large Language Model (LLM) through structured prompts and guide its responses using clear instructions, constraints, examples, and fallback conditions.

A customer support classification task is implemented to categorize user complaints into predefined categories.

## Concepts Covered

- **Groq API Integration:** Connecting a Python application with an LLM using the Groq API.
- **Environment Variables:** Using `python-dotenv` and `os` to securely manage API keys.
- **Reusable LLM Function:** Creating a function to send prompts and retrieve model responses.
- **Role Prompting:** Defining the role the LLM should perform.
- **Task Prompting:** Clearly specifying the task to be completed.
- **Constraints:** Restricting the model to predefined categories.
- **Output Formatting:** Controlling the structure of the model's response.
- **Few-Shot Prompting:** Providing examples to guide model behaviour.
- **Fallback Instructions:** Handling inputs that do not belong to the defined categories.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Groq API | LLM integration |
| GPT-OSS-120B | Language model |
| python-dotenv | Environment variable management |
| Pydantic | Imported for structured data learning |

## Project Workflow

1. Load environment variables from the `.env` file.
2. Retrieve the Groq API key securely.
3. Initialize the Groq client.
4. Define a reusable function to communicate with the LLM.
5. Design a structured prompt with role, task, constraints, examples, and fallback instructions.
6. Pass a customer complaint to the LLM.
7. Receive the classification result.

## Classification Categories

The customer support assistant classifies complaints into four possible outputs:

| Category | Description |
|---|---|
| Billing | Payment or billing-related issues |
| Technical | Mobile or laptop technical issues |
| Return | Product return or refund requests |
| Other | Issues unrelated to the defined categories |

## Example

**Input:**

```text
My papa is angry with me.
```

**Expected Output:**

```text
other
```

The model is instructed to return only one word representing the appropriate category.

## Learning Outcomes

Through this exercise, I learned:

- How to integrate an LLM into a Python application.
- How to make API calls using the Groq client.
- How to create reusable functions for LLM interactions.
- How to structure prompts for better and more predictable responses.
- How role, task, constraints, examples, and fallback instructions influence model behaviour.
- How to build a basic AI-powered text classification system.

## Future Improvements

- Implement structured output using Pydantic.
- Add more customer support categories.
- Handle invalid or ambiguous classifications.
- Build a customer support ticket classification application.
- Explore different prompting strategies and compare their results.

---

**Day 06 | AI Engineering Lab**

Learning to design effective prompts and build practical applications using Large Language Models and Python.