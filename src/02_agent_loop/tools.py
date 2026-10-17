import subprocess

tool = [
    {
        "type": "function",
        "function": {
            "name": "run_bash",
            "description": "提供bash命令输出运行结果",
            "parameters": {
                "type": "object",
                "properties": {
                    "cmd": {"type": "string", "description": "要执行的bash命令"}
                },
                "required": ["cmd"],
            },
        },
    }
]


def run_bash(cmd: str) -> str:
    """提供bash命令输出运行结果"""
    try:
        print(cmd)
        response = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )

        result = response.stdout
        if response.stderr:
            result += response.stderr
        return f"命令{cmd}执行成功！结果为：\n{result}"
    except subprocess.TimeoutExpired:
        return f"命令{cmd}执行超时！"
    except Exception as e:
        return f"命令{cmd}执行失败！错误信息为：\n{e!s}"


function_map = {"run_bash": run_bash}
