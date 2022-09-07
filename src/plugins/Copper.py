from nonebot.adapters import Event
from nonebot.rule import Rule
from nonebot import on_message

async def copper_ai(event: Event) -> bool:
    return "炼" in  event.get_plaintext()

async def copper_cu(event: Event) -> bool:
    return "铜" in event.get_plaintext()

copper_checker = Rule(copper_ai, copper_cu)

copper = on_message(rule=copper_checker)

@copper.handle()
async def copper_handler():
    await copper.finish("https://www.66law.cn/zuiming/321.aspx")

