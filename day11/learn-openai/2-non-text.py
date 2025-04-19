import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

messages = [{
    "role": "user",
    "content": [
        {"type": "text", "text": "What is in this image?"},
        {
            "type": "image_url",
            "image_url": {
                "url": "https://i.ytimg.com/vi/tGHVgtq1cBU/hq720_2.jpg?sqp=-oaymwE7CK4FEIIDSFryq4qpAy0IARUAAAAAGAAlAADIQj0AgKJD8AEB-AHOBYAC0AWKAgwIABABGHIgRSgvMA8=&rs=AOn4CLAnOO2x2uY2Inn2OjLX0W0wE1M5KA"
            }
        }
    ]
}]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

content = response.choices[0].message.content

print(content)