from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg

echo = on_command("echo")

@echo.handle()
async def echo_handler(args: Message = CommandArg()):
    text = args.extract_plain_text()
    await echo.finish(text)
