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

@scheduler.scheduled_job("cron", year=2022, month=12, day=21, hour=9, minute=10, second=0, id="221221")
async def Sao221221():
    with open(f"{ASSETS_ROOT}/sword_art_online/221221.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2022, month=12, day=23, hour=9, minute=10, second=0, id="221223")
async def Sao221223():
    with open(f"{ASSETS_ROOT}/sword_art_online/221223.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2022, month=12, day=27, hour=9, minute=10, second=0, id="221227")
async def Sao221227():
    with open(f"{ASSETS_ROOT}/sword_art_online/221227.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2022, month=12, day=31, hour=9, minute=10, second=0, id="221231")
async def Sao221231():
    with open(f"{ASSETS_ROOT}/sword_art_online/221231.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2023, month=1, day=4, hour=9, minute=10, second=0, id="230104")
async def Sao230104():
    with open(f"{ASSETS_ROOT}/sword_art_online/230104.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", year=2023, month=3, day=31, hour=9, minute=10, second=0, id="230331")
async def Sao230331():
    with open(f"{ASSETS_ROOT}/sword_art_online/230331.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

