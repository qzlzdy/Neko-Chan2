from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain
from nonebot.adapters.mirai2.message import MessageSegment
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

async def sendSaoNote(date):
    with open(f"{ASSETS_ROOT}/sword_art_online/{date}.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

eventDates = [
    "221202", "221204", "221208", "221214", "221221",
    "221223", "221227", "221231", "230104", "230331",
    "230408", "230612", "231015", "231016", "231017",
    "231018", "231224"
]

for date in eventDates:
    year = 2000 + int(date[0:2])
    month = int(date[2:4])
    day = int(date[4:6])
    scheduler.add_job(sendSaoNote,
        "cron", year=year, month=month, day=day,
        hour=9, minute=10, second=0,
        args=[date])
