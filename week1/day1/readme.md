# Day 01 – Understanding LLM API Calls

## 🎯 Objective

Understand how to communicate with a Large Language Model (LLM) programmatically using an API and explore the fundamental components involved in an LLM request and response.

## 📚 Concepts Learned

### 1. API Key
- An API key is an authentication credential used to access an LLM provider's API.
- It identifies and authorizes the application making the request.
- It should be stored securely using environment variables.
- Never expose API keys in public repositories.

### 2. Model
- A model is the specific LLM that processes the input and generates a response.
- Different models can have different capabilities, performance, context windows, and costs.
- The model is specified when making an API request.

### 3. Messages (Role & Content)

Messages represent the conversation input sent to an LLM.

Each message contains two important fields:

**Role:** Defines who is sending the message or providing instructions.

Common roles:
- `system` – Provides instructions or behavioral context.
- `user` – Contains the user's input or question.
- `assistant` – Represents the AI-generated response.

**Content:** Contains the actual text or information associated with the message.

Example:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "Explain how LLMs work."
    }
]
```

### 4. Response

After processing the request, the API returns a response containing information about the generated output.

Important components:

**Choices**
- Contains the model's generated response options.
- `choices[0]` generally represents the first generated response.
- `choices[0].message.content` contains the generated text in the Chat Completions API.

**Usage**
- Provides information about token consumption.
- Common fields include:
  - `prompt_tokens` – Tokens used in the input.
  - `completion_tokens` – Tokens generated in the output.
  - `total_tokens` – Total tokens consumed.

Usage information helps understand API consumption and estimate costs.

## 🔄 LLM API Workflow

1. Obtain an API key.
2. Select an LLM model.
3. Prepare messages with appropriate roles and content.
4. Send the API request.
5. Receive the model response.
6. Extract the generated content and inspect token usage.

## 💻 Practical Implementation

Implemented a basic LLM API call using Python.

The implementation explores:
- API authentication.
- Model selection.
- Sending messages.
- Extracting generated responses.
- Understanding token usage.

## 💡 Key Takeaways

- An API provides a communication interface between an application and an LLM.
- The API key handles authentication.
- The model determines which LLM processes the request.
- Messages provide the conversational context.
- Choices contain generated responses.
- Usage provides token consumption details.

## 🚀 Next Learning Goal

Explore how LLMs process text internally, starting with tokenization and understanding how text is converted into tokens.

---

**Day 01 Complete | AI Engineering Learning Journey**