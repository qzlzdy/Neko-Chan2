from nonebot import require

require("nonebot_plugin_apscheduler")

import base64
import io
from PIL import Image
from nmb.NetBIOS import NetBIOS
from random import randint
from smb.SMBHandler import SMBHandler
import sqlite3
import urllib
from nonebot import on_command
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.adapters.onebot.v11.message import Message
from ..utils import ASSETS_ROOT
from ..utils import sendFriendMessage
from ..config import USERNAME
from ..config import PASSWORD
from ..config import HOSTNAME

setu = on_command("来点黄色")

@setu.handle()
@scheduler.scheduled_job("cron", hour="5-22", minute=50, second=11, id="Setu please")
async def sendSetu():
    db = sqlite3.connect(f"{ASSETS_ROOT}/Setu.db")
    cur = db.cursor()
    sql = "SELECT extension FROM setus WHERE illust_id = ?"
    ip_addresses = NetBIOS().queryName(HOSTNAME)
    for i in range(len(ip_addresses)):
        illust_id = randint(1, 99657)
        res = cur.execute(sql, (illust_id,))
        ext = res.fetchall()[0][0]
        #infile = open(f"{ASSETS_ROOT}/setu/H{illust_id}.{ext}", "rb").read()
        #buf = base64.b64encode(infile)
        opener = urllib.request.build_opener(SMBHandler)
        fh = opener.open(f"smb://{USERNAME}:{PASSWORD}@{ip_addresses[0]}/Multimedia/Pictures/setu/H{illust_id}.{ext}")
        img = Image.open(fh)
        img = img.rotate(180)
        fh.close()
        buf = io.BytesIO()
        img.save(buf, format="png")
        buf = buf.getvalue()
        buf = base64.b64encode(buf)
        await sendFriendMessage(419286376, Message([
            MessageSegment.image("base64://" + str(buf, "utf-8")),
            MessageSegment.text(str(illust_id))
        ]))
    db.close()
