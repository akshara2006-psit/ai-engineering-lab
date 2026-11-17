# Day 04 – Structured Outputs in LLMs

## 🎯 Objective

Understand how to make LLMs generate structured, machine-readable responses instead of plain-text answers using JSON, Pydantic, and schema-based instructions.

## 📚 Concepts Learned

### 1. What Are Structured Outputs?

By default, LLMs generate responses in natural language.

However, real-world applications often need data in a predefined format so that it can be processed by software.

**Example:**

Unstructured input:

```text
Hello, my name is Akshara.
My email is abc@gmail.com.
My iPhone is not working.
```

Expected structured output:

```json
{
    "name": "Akshara",
    "email": "abc@gmail.com",
    "issue": "My iPhone is not working"
}
```

Structured outputs make it easier to integrate LLMs with applications, databases, APIs, and automated workflows.

### 2. Pydantic

Pydantic is a Python library used for data validation and parsing using Python type annotations.

It helps define the expected structure and data types of information.

**Implementation:**

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

Here:
- `Ticket` defines a data model.
- `name` must be a string.
- `email` must be a string.
- `issue` must be a string.

### 3. JSON Schema

JSON Schema describes the expected structure, properties, and data types of JSON data.

Pydantic can automatically generate a JSON Schema from a model.

```python
schema = Ticket.model_json_schema()
print(schema)
```

This schema describes the expected fields and their types.

It can be supplied to an LLM as part of the instructions to guide structured data generation.

### 4. JSON Mode

JSON mode instructs the model to return its response in valid JSON format.

```python
response_format = {
    "type": "json_object"
}
```

It is passed to the chat completion API:

```python
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2,
    response_format=response_format
)
```

**Important distinction:**
- JSON mode ensures JSON-formatted output.
- JSON mode alone does not guarantee that the response follows your exact Pydantic schema.
- Schema-constrained structured outputs provide stronger guarantees when supported by the model and API.

### 5. System Prompt for Structured Extraction

System prompts can instruct the LLM to extract information according to a predefined schema.

```python
system_prompt = f"""
Extract the personal information from the ticket
strictly based on this schema {schema}
and give a JSON output.
"""
```

This helps the model understand which fields it needs to extract.

### 6. Extracting the LLM Response

The generated response can be accessed using:

```python
answer = response.choices[0].message.content
print(answer)
```

The response contains a JSON-formatted string.

### 7. Parsing JSON using json.loads()

A JSON string is not automatically a Python dictionary.

Python's `json` module converts JSON text into Python objects.

```python
import json

raw_json = answer
data_file = json.loads(raw_json)
```

Now, `data_file` can be accessed like a Python dictionary.

For example:

```python
print(data_file["name"])
```

### 8. Pydantic Model Validation

After parsing JSON, the extracted data can be validated using the Pydantic model.

```python
ticket = Ticket(**data_file)

print(ticket.name)
```

Here:
- `**data_file` unpacks dictionary fields as keyword arguments.
- `Ticket()` creates a Pydantic model instance.
- Pydantic validates the provided data against the model's field definitions.
- Invalid or missing required fields can raise a `ValidationError`.

## 🔄 Complete Workflow

1. Define a Pydantic model.
2. Generate its JSON Schema.
3. Include the schema in the system prompt.
4. Send the customer ticket to the LLM.
5. Request JSON-formatted output.
6. Extract the response content.
7. Parse JSON using `json.loads()`.
8. Validate the extracted data using Pydantic.
9. Access structured information through model attributes.

## 💻 Practical Implementation

**Use Case: Customer Support Ticket Information Extraction**

Built a Python application using the Groq API to extract customer information from an unstructured support ticket.

**Input:**

A customer describes an issue with an iPhone and provides personal information such as their name, email, and contact details.

**Expected extracted fields:**
- Name
- Email
- Issue

**Technologies used:**
- Python
- Groq API
- Pydantic
- JSON
- python-dotenv

**Implementation highlights:**
- Created a custom Pydantic model.
- Generated a JSON Schema automatically.
- Used system instructions to guide information extraction.
- Requested JSON-formatted LLM output.
- Parsed the response into Python data.
- Validated the extracted information using Pydantic.

## 💡 Key Takeaways

- Structured outputs make LLM responses machine-readable.
- Pydantic defines and validates expected data structures.
- JSON Schema describes the expected JSON format.
- JSON mode helps produce valid JSON responses.
- `json.loads()` converts JSON strings into Python objects.
- Pydantic validates extracted data against a defined model.
- Structured data extraction is useful in customer support, document processing, automation, and AI-powered applications.

## 🚀 Next Learning Goal

Explore how LLMs handle conversation history and maintain context across multiple interactions.

---

**Day 04 Complete | AI Engineering Learning Journey**