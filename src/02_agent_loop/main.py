import json
import os

import dotenv
from openai import OpenAI

from tools import function_map, tool

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))


def loop(messages: list[dict]):
    for i in range(20):
        completion = client.chat.completions.create(
            model="qwen3.8-flash", messages=messages, tools=tool, tool_choice="auto"
        )

        msg = completion.choices[0].message

        if not msg.tool_calls:
            messages.append({"role": "assistant", "content": msg.content})
            return msg.content

        messages.append(
            {"role": "assistant", "content": msg.content, "tool_calls": msg.tool_calls}
        )

        for tool_call in msg.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            function_result = function_map[function_name](**function_args)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": function_result,
                }
            )
    return "loop 次数达到20次上限无结果"


def mian():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    while True:
        content = input(">>请输入问题:")

        if content == "exit":
            break

        messages.append({"role": "user", "content": content})

        result = loop(messages=messages)
        print(result)


if __name__ == "__main__":
    mian()
