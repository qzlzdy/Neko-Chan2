import base64
from nonebot import on_keyword
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11.message import MessageSegment
from ..utils import ASSETS_ROOT

kawaii = on_keyword(["可爱"])

@kawaii.handle()
async def kawaii_handler():
    infile = open(f"{ASSETS_ROOT}/kawaii.jpg", "rb").read()
    buf = base64.b64encode(infile)
    await kawaii.send(Message([
        MessageSegment.text("我很可爱  请给我钱"),
        MessageSegment.image("base64://" + str(buf, "utf-8"))
    ]))
