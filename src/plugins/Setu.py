from nonebot import require

require("nonebot_plugin_apscheduler")

import base64
import io
from PIL import Image
from random import randint
import sqlite3
from nonebot import on_command
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageSegment
from nonebot.adapters.mirai2.message import MessageChain
from ..utils import ASSETS_ROOT
from ..utils import sendFriendMessage

setu = on_command("来点黄色")

@setu.handle()
@scheduler.scheduled_job("cron", hour="5-22", minute=50, second=11, id="Setu please")
async def sendSetu():
    db = sqlite3.connect(f"{ASSETS_ROOT}/Setu.db")
    cur = db.cursor()
    sql = "SELECT extension FROM setus WHERE illust_id = ?"
    for i in range(1):
        illust_id = randint(79401, 89400)
        res = cur.execute(sql, (illust_id,))
        ext = res.fetchall()[0][0]
        #infile = open(f"{ASSETS_ROOT}/setu/H{illust_id}.{ext}", "rb").read()
        #buf = base64.b64encode(infile)
        img = Image.open(f"{ASSETS_ROOT}/setu/H{illust_id}.{ext}")
        img = img.rotate(180)
        buf = io.BytesIO()
        img.save(buf, format="png")
        buf = buf.getvalue()
        buf = base64.b64encode(buf)
        await sendFriendMessage(419286376, MessageChain([
            MessageSegment.image(
                base64=str(buf, "utf-8")
            ),
            MessageSegment.plain(str(illust_id))
        ]))
    db.close()
