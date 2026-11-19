import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
model="openai/gpt-oss-120b"
client=Groq(api_key=my_api_key)
if not my_api_key:
    raise ValueError("Api key kaha hai bhaiiiiiiiiii!!!!!")

def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans


good_prompt="""
# ROLE
You are a support assistant at a mobile/laptop company
# TASK
You have to classify the issue in a category
# CONSTRAINT
You have to classify the issue in one of the three categories namely billing, technical, return 
#OUTPUT-FORMAT
Your answer should be in one word only.tHe one word should be one of the category given in constraints.
# Example
For instance if a user complaint says he wants a refund then category is return 
# Fallback
If the issue is unrelated to any of the categories mentioned in the constraints  then the answer should be other.

This is a user complaint My papa is angry with me classify this:


"""
print(llm_ans(bad_prompt))