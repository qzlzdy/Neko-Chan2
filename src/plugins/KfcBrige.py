from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import sendGroupMessage

@scheduler.scheduled_job("cron", day_of_week="thu", hour=11, minute=0, second=0, id="KFC Brige")
async def kfcBrige():
    await sendGroupMessage(1161079807, "/V")
