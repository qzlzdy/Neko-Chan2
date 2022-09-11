from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

@scheduler.scheduled_job("cron", month=2, day=2, hour=9, minute=0, second=0, id="Twin Tail Day")
async def TwinTailDay():
    with open(f"{ASSETS_ROOT}/calendar/0202-TainTailDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=1, hour=9, minute=0, second=0, id="Oppai Day")
async def OppaiDay():
    with open(f"{ASSETS_ROOT}/calendar/0801-OppaiDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=2, hour=9, minute=0, second=0, id="Pants Day")
async def PantsDay():
    with open(f"{ASSETS_ROOT}/calendar/0802-PantsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=31, hour=9, minute=0, second=0, id="Hatsune Miku's Birthday")
async def HatsuneMikuBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0831-HatsuneMikuBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=8, hour=9, minute=0, second=0, id="Kupa Day")
async def KupaDay():
    with open(f"{ASSETS_ROOT}/calendar/0908-KupaDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=9, hour=9, minute=9, second=9, id="Cirno Day")
async def CirnoDay():
    with open(f"{ASSETS_ROOT}/calendar/0909-CirnoDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=12, hour=9, minute=0, second=0, id="Minami Kotori's Birthday")
async def MinamiKotoriBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0912-MinamiKotoriBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=15, hour=9, minute=0, second=0, id="Komichi Aya's Birthday")
async def KomichiAyaBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0915-KomichiAyaBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=10, day=10, hour=9, minute=0, second=0, id="Moe Day")
async def MoeDay():
    with open(f"{ASSETS_ROOT}/calendar/1010-MoeDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=10, day=11, hour=9, minute=0, second=0, id="Loli Day")
async def LoliDay():
    with open(f"{ASSETS_ROOT}/calendar/1011-LoliDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=11, day=2, hour=9, minute=0, second=0, id="Tights Day")
async def TightsDay():
    with open(f"{ASSETS_ROOT}/calendar/1102-TightsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)
