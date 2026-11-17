import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
schema=Ticket.model_json_schema()
response_format={
    "type":"json_object"
}
system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema{schema} and give a json output
"""

model="openai/gpt-oss-120b"
message_system={
    "role":"system",
    "content":system_prompt
}
role="user"
text="Hello my name is Akshara.I have an iphone which is not working at all.My address is Kanpur.My email is  abc@gmail.com.My contact number is is 82134 "
prompt=f'''
This is a customer ticket.Please extract the personal information from this.{text}
'''
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages,temperature=2,response_format=response_format)


answer=response.choices[0].message.content
print(answer)

# isko padhte kaise hai
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)
print(ticket.name)