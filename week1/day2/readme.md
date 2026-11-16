# Day 02 – System Role & Temperature in LLMs

## 🎯 Objective

Understand how system instructions control LLM behavior and how temperature influences the randomness and creativity of generated responses.

## 📚 Concepts Learned

### 1. System Role

The `system` role provides instructions and behavioral guidelines to an LLM.

It helps define how the model should respond, what personality it should adopt, and what rules it should follow.

**Example:**

```python
message_system = {
    "role": "system",
    "content": "You are a helpful AI assistant."
}
```

**Key points:**
- Defines the assistant's behavior.
- Establishes conversational context.
- Guides the tone and style of responses.
- Can provide specific instructions and constraints.

### 2. Temperature

Temperature is a parameter that controls the randomness of token selection during text generation.

It influences how predictable or varied the model's responses are.

**Understanding temperature values:**

| Temperature | Behavior |
|---|---|
| 0.0 | More predictable and focused |
| 0.3 | Relatively consistent responses |
| 0.7 | More varied and creative |
| 1.0 | Higher randomness |

*These are illustrative tendencies, not guaranteed output behaviors. The effect depends on the model and provider.*

**Example:**

```python
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.7
)
```

**Key points:**
- Lower temperature generally produces more predictable outputs.
- Higher temperature generally increases response diversity.
- Temperature affects token selection probabilities.
- It does not change the underlying knowledge or intelligence of the model.

## 💻 Practical Implementation

Implemented a Python application using the Groq API to experiment with system instructions and LLM response generation.

**Technologies used:**
- Python
- Groq API
- Groq Python SDK
- python-dotenv

**Implementation highlights:**
- Loading API keys using environment variables.
- Initializing the Groq client.
- Selecting the `openai/gpt-oss-120b` model.
- Defining system and user messages.
- Sending messages to the chat completion endpoint.
- Extracting the generated response using `choices[0].message.content`.

Experimented with the system instruction:

`You are my loving girlfriend`

And the user prompt:

`I love you baby!!!`

The implementation can be extended by changing the temperature parameter and comparing the generated responses.

## 💡 Key Takeaways

- System role controls the behavioral instructions given to an LLM.
- Temperature influences randomness during text generation.
- System instructions and generation parameters serve different purposes.
- The same prompt can generate different responses depending on system instructions and temperature settings.

## 🚀 Next Learning Goal

Explore tokenization and understand how LLMs convert human-readable text into tokens and token IDs before processing it.

---

**Day 02 Complete | AI Engineering Learning Journey**