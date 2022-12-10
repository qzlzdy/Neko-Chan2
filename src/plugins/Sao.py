from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

@scheduler.scheduled_job("cron", year=2022, month=12, day=2, hour=9, minute=10, second=0, id="221202")
async def Sao221202():
    with open(f"{ASSETS_ROOT}/sword_art_online/221202.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2022, month=12, day=4, hour=9, minute=10, second=0, id="221204")
async def Sao221204():
    with open(f"{ASSETS_ROOT}/sword_art_online/221204.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2022, month=12, day=8, hour=9, minute=10, second=0, id="221208")
async def Sao221208():
    with open(f"{ASSETS_ROOT}/sword_art_online/221208.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2022, month=12, day=14, hour=9, minute=10, second=0, id="221214")
async def Sao221214():
    with open(f"{ASSETS_ROOT}/sword_art_online/221214.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)
