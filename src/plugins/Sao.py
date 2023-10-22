from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

async def sendSaoNote(date):
    with open(f"{ASSETS_ROOT}/sword_art_online/{date}.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", year=2022, month=12, day=2, hour=9, minute=10, second=0, id="221202")
async def Sao221202():
    await sendSaoNote("221202")

@scheduler.scheduled_job("cron", year=2022, month=12, day=4, hour=9, minute=10, second=0, id="221204")
async def Sao221204():
    await sendSaoNote("221204")

@scheduler.scheduled_job("cron", year=2022, month=12, day=8, hour=9, minute=10, second=0, id="221208")
async def Sao221208():
    await sendSaoNote("221208")

@scheduler.scheduled_job("cron", year=2022, month=12, day=14, hour=9, minute=10, second=0, id="221214")
async def Sao221214():
    await sendSaoNote("221214")

@scheduler.scheduled_job("cron", year=2022, month=12, day=21, hour=9, minute=10, second=0, id="221221")
async def Sao221221():
    await sendSaoNote("221221")

@scheduler.scheduled_job("cron", year=2022, month=12, day=23, hour=9, minute=10, second=0, id="221223")
async def Sao221223():
    await sendSaoNote("221223")

@scheduler.scheduled_job("cron", year=2022, month=12, day=27, hour=9, minute=10, second=0, id="221227")
async def Sao221227():
    await sendSaoNote("221227")

@scheduler.scheduled_job("cron", year=2022, month=12, day=31, hour=9, minute=10, second=0, id="221231")
async def Sao221231():
    await sendSaoNote("221231")

@scheduler.scheduled_job("cron", year=2023, month=1, day=4, hour=9, minute=10, second=0, id="230104")
async def Sao230104():
    await sendSaoNote("230104")

@scheduler.scheduled_job("cron", year=2023, month=3, day=31, hour=9, minute=10, second=0, id="230331")
async def Sao230331():
    await sendSaoNote("230331")

@scheduler.scheduled_job("cron", year=2023, month=4, day=8, hour=9, minute=10, second=0, id="230408")
async def Sao230408():
    await sendSaoNote("230408")

@scheduler.scheduled_job("cron", year=2023, month=6, day=12, hour=9, minute=10, second=0, id="230612")
async def Sao230612():
    await sendSaoNote("230612")

@scheduler.scheduled_job("cron", year=2023, month=10, day=15, hour=9, minute=10, second=0, id="231015")
async def Sao231015():
    await sendSaoNote("231015")

@scheduler.scheduled_job("cron", year=2023, month=10, day=16, hour=9, minute=10, second=0, id="231016")
async def Sao231016():
    await sendSaoNote("231016")

@scheduler.scheduled_job("cron", year=2023, month=10, day=17, hour=9, minute=10, second=0, id="231017")
async def Sao231017():
    await sendSaoNote("231017")

@scheduler.scheduled_job("cron", year=2023, month=10, day=18, hour=9, minute=10, second=0, id="231018")
async def Sao231018():
    await sendSaoNote("231018")

