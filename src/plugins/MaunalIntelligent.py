import base64
from nonebot import on_keyword, on_message
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.rule import Rule
from ..utils import ASSETS_ROOT

# 114514
senpai = on_keyword(["啊啊啊啊", "恶臭"])
@senpai.handle()
async def senpai_handler():
    infile = open("/home/alarm/Neko-Chan/Neko-Chan2/assets/114514.mp3", "rb").read()
    buf = base64.b64encode(infile)
    audio = MessageSegment.record("base64://" + str(buf, "utf-8"))
    await senpai.finish(audio)

# Amiya
amiya = on_keyword(["休息", "下班"])
@amiya.handle()
async def amiya_handler():
    await amiya.finish("刀客塔，你还有很多工作没有完成，现在还不能休息哦")

# Lolicon
async def copper_ai(event: Event) -> bool:
    return "炼" in  event.get_plaintext()

async def copper_cu(event: Event) -> bool:
    return "铜" in event.get_plaintext()

copper_checker = Rule(copper_ai, copper_cu)
copper = on_message(rule=copper_checker)
@copper.handle()
async def copper_handler():
    await copper.finish("https://www.66law.cn/zuiming/321.aspx")

# Kawaii
kawaii = on_keyword(["可爱"])
@kawaii.handle()
async def kawaii_handler():
    infile = open(f"{ASSETS_ROOT}/kawaii.jpg", "rb").read()
    buf = base64.b64encode(infile)
    await kawaii.send(Message([
        MessageSegment.text("我很可爱  请给我钱"),
        MessageSegment.image("base64://" + str(buf, "utf-8"))
    ]))
