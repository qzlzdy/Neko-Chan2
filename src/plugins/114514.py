import base64
from nonebot import on_keyword
from nonebot.adapters.mirai2.message import MessageSegment
from nonebot.adapters.mirai2.message import MessageType

senpai = on_keyword(["啊啊啊啊", "恶臭"])

@senpai.handle()
async def senpai_handler():
    infile = open("/home/alarm/Neko-Chan/Neko-Chan2/assets/114514.mp3", "rb").read()
    buf = base64.b64encode(infile)
    audio = MessageSegment(type=MessageType.VOICE, base64=str(buf, "utf-8"))
    await senpai.finish(audio)
