from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg
from ..utils import sendNotice

echo = on_command("echo")

@echo.handle()
async def echo_handler(args: Message = CommandArg()):
    text = args.extract_plain_text()
    await echo.finish(text)
