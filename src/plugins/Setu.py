from nonebot import require

require("nonebot_plugin_apscheduler")

import base64
import io
from PIL import Image
from nmb.NetBIOS import NetBIOS
import ntpath
import random
from smb.SMBHandler import SMBHandler
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

def random_line(path):
    picked = None
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if random.randrange(i) == 0:
                picked = line
    file_path = picked.rstrip("\r\n").rsplit("|", 1)[0]
    stem, _ = ntpath.splitext(ntpath.basename(file_path))
    return file_path, stem[:6]

@setu.handle()
@scheduler.scheduled_job("cron", hour="5-22", minute=50, second=11, id="Setu please")
async def sendSetu():
    ip_addresses = NetBIOS().queryName(HOSTNAME)
    for i in range(len(ip_addresses)):
        path, illust_id = random_line(f"{ASSETS_ROOT}/setu/all_files.txt")
        opener = urllib.request.build_opener(SMBHandler)
        fh = opener.open(f"smb://{USERNAME}:{PASSWORD}@{ip_addresses[0]}/Multimedia/Pictures/{path}")
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
