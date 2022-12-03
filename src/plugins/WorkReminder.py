from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain, MessageSegment
from ..utils import sendFriendMessage, sendGroupMessage

@scheduler.scheduled_job("cron", hour=8, minute=30, second=0, id="AM Work Reminder")
@scheduler.scheduled_job("cron", hour=17, minute=35, second=0, id="PM Work Reminder")
async def WorkReminder():
    await sendFriendMessage(419286376, "今天你打卡了吗")

@scheduler.scheduled_job("cron", hour=20, minute=40, second=0, id="Jap Reminder")
async def JapReminder():
    await sendGroupMessage(1161079807, MessageChain([
        MessageSegment.plain("今天你学五十音了吗"),
        MessageSegment.at(1020051753)
    ]))

