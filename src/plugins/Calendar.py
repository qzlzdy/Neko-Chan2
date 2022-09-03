from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

@scheduler.scheduled_job("cron", month=2, day=2, hour=9, minute=0, second=0, id="Twin Tail Day Reminder")
async def TwinTailDayReminder():
    with open(f"{ASSETS_ROOT}/calendar/0202-TainTailDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=1, hour=9, minute=0, second=0, id="Oppai Day Reminder")
async def OppaiDayReminder():
    with open(f"{ASSETS_ROOT}/calendar/0801-OppaiDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=2, hour=9, minute=0, second=0, id="Pants Day Reminder")
async def PantsDayReminder():
    with open(f"{ASSETS_ROOT}/calendar/0802-PantsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=31, hour=9, minute=0, second=0, id="Miku's Birthday Reminder")
async def MikuBirthdayReminder():
    with open(f"{ASSETS_ROOT}/calendar/0831-MikuBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=9, hour=9, minute=9, second=9, id="Cirno Day Reminder")
async def CirnoDayReminder():
    with open(f"{ASSETS_ROOT}/calendar/0909-CirnoDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=10, day=10, hour=9, minute=0, second=0, id="Moe Day Reminder")
async def MoeDayReminder():
    with open(f"{ASSETS_ROOT}/calendar/1010-MoeDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=10, day=11, hour=9, minute=0, second=0, id="Loli Day Reminder")
async def LoliDayReminder():
    with open(f"{ASSETS_ROOT}/calendar/1011-LoliDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=11, day=2, hour=9, minute=0, second=0, id="Tights Day Reminder")
async def TightsDayReminder():
    with open(f"{ASSETS_ROOT}/calendar/1102-TightsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)
