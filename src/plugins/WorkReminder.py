from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import sendFriendMessage

@scheduler.scheduled_job("cron", hour=8, minute=30, second=0, id="AM Work Reminder")
@scheduler.scheduled_job("cron", hour=17, minute=35, second=0, id="PM Work Reminder")
async def AmWorkReminder():
    await sendFriendMessage(419286376, "今天你打卡了吗")
