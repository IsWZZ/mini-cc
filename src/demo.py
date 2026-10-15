import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

completion = client.chat.completions.create(
    model="qwen3.8-flash",
    messages=[{"role": "user", "content": "你是谁？"}],
)
print(completion.choices[0].message.content)
