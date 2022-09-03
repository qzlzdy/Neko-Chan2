from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import ASSETS_ROOT
from ..utils import sendFriendMessage
from random import randint
import sqlite3
import base64
from nonebot.adapters.mirai2.message import MessageSegment
from nonebot.adapters.mirai2.message import MessageChain

@scheduler.scheduled_job("cron", hour=7, minute=30, second=0, id="AM Setu")
@scheduler.scheduled_job("cron", hour=12, minute=50, second=0, id="Noon Setu")
@scheduler.scheduled_job("cron", hour=23, minute=20, second=0, id="PM Setu")
async def sendSetu():
    db = sqlite3.connect(f"{ASSETS_ROOT}/Setu.db")
    cur = db.cursor()
    sql = "SELECT extension FROM setus WHERE illust_id = ?"
    for i in range(5):
        illust_id = randint(29201, 49200)
        res = cur.execute(sql, (illust_id,))
        ext = res.fetchall()[0][0]
        infile = open(f"{ASSETS_ROOT}/setu/H{illust_id}.{ext}", "rb").read()
        buf = base64.b64encode(infile)
        await sendFriendMessage(419286376, MessageChain([
            MessageSegment.image(
                base64=str(buf, "utf-8")
            ),
            MessageSegment.plain(str(illust_id))
        ]))
    db.close()
