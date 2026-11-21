# Day 07 – Building a ReAct AI Agent with Tool Calling

## Overview

Today's learning focuses on **ReAct (Reasoning + Acting)**, an approach that enables Large Language Models (LLMs) to interact with external tools and perform tasks step by step.

Using Python and the Groq API, I built a basic AI-powered shopping assistant that can retrieve product prices and perform mathematical calculations using custom-defined tools.

Instead of answering everything directly, the LLM decides which tool to use, receives the tool's output, and uses that observation to continue its task.

## Concepts Covered

- **ReAct Framework:** Combining reasoning and actions to solve tasks step by step.
- **LLM Tool Calling:** Enabling an LLM to interact with external Python functions.
- **Custom Tool Creation:** Defining Python functions that perform specific operations.
- **Tool Mapping:** Registering functions in a dictionary so they can be accessed dynamically.
- **Prompt Engineering:** Defining instructions that control the agent's behaviour.
- **Regular Expressions:** Using Python's `re` module to identify and extract tool calls.
- **Agent Loop:** Allowing the LLM to perform multiple reasoning and action steps.
- **Observations:** Returning tool execution results to the LLM.
- **Groq API Integration:** Using an LLM to power the agent's decision-making process.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Groq API | LLM integration |
| GPT-OSS-120B | Language model |
| Regular Expressions (`re`) | Extracting tool calls |
| `os` | Accessing environment variables |
| `python-dotenv` | Managing API keys |
| `time.sleep()` | Adding delays between iterations |

## Tools Implemented

### 1. Product Price Tool

A custom Python function that retrieves predefined product prices.

Supported products:
- iPhone 17
- iPhone 15

### 2. Calculator Tool

A Python function that evaluates mathematical expressions and returns the calculated result.

### Tool Registration

Both functions are registered in a Python dictionary:

- `get_product_price`
- `calculator`

The LLM selects the appropriate tool, and Python executes the corresponding function.

## Understanding the ReAct Workflow

The agent follows a step-by-step process:

1. **Thought:** The LLM decides what needs to be done.
2. **Action:** The LLM specifies which tool to execute.
3. **Observation:** Python executes the selected tool and returns its result.
4. **Reasoning:** The LLM uses the observation to decide its next step.
5. **Final Answer:** The LLM provides the completed response.

## Example

**User Query:**

```text
I have 5000 rupees.
What is the price of an iPhone 17?
How much money will I have left?
```

**Agent Workflow:**

```text
Thought: I need to find the iPhone 17 price.

Action: get_product_price("iPhone 17")

Observation: 1000

Thought: Now I need to subtract the price from the budget.

Action: calculator("5000 - 1000")

Observation: 4000

Final Answer:
The iPhone 17 costs ₹1000.
You will have ₹4000 left.
```

*The prices above are predefined values in the custom Python function, not live market prices.*

## Learning Outcomes

Through this exercise, I learned:

- How to build a basic tool-using AI agent.
- How LLMs decide which external function to execute.
- How to connect LLM reasoning with Python functions.
- How the Thought–Action–Observation cycle works.
- How to extract tool calls using regular expressions.
- How an agent can perform multiple actions before generating its final response.
- How to build a reusable agent loop with a maximum number of execution steps.

## Future Improvements

- Implement native function calling instead of extracting actions through regular expressions.
- Add more tools, such as product search and inventory checking.
- Improve error handling for invalid tool calls.
- Add support for dynamic product prices.
- Build a multi-tool shopping assistant.
- Explore more advanced agent architectures.

---

**Day 07 | AI Engineering Lab**

Exploring AI agents, ReAct architecture, and tool integration using Python and Large Language Models.