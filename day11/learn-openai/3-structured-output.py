import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

class TutorialofAnything(BaseModel):
    tutorial_name: str
    tutorial_description: str
    tutorial_tools: list[str]
    tutorial_steps: list[str]

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

messages = [{
    "role": "user",
    "content": "Tell me a tutorial about having a date with girlfriend for gen z?"
}]

response = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=messages,
    response_format=TutorialofAnything
)

parsed_output = response.choices[0].message.parsed

print("== Tutorial Name ==")
print(parsed_output.tutorial_name)
print("== Tutorial Description ==")
print(parsed_output.tutorial_description)
print("== Tutorial Tools ==")
for tool in parsed_output.tutorial_tools:
    print(f"- {tool}")
print("== Tutorial Steps ==")
for step in parsed_output.tutorial_steps:
    print(f"- {step}")
print("== End ==")