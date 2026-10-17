import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))


def mian():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    while True:
        content = input(">>>请问:")

        messages.append({"role": "user", "content": content})

        completion = client.chat.completions.create(
            model="qwen3.8-flash", messages=messages
        )

        print(completion.choices[0].message.content)


if __name__ == "__main__":
    mian()
