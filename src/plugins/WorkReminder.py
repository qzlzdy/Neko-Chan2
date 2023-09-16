from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain, MessageSegment
from ..utils import sendFriendMessage, sendGroupMessage

@scheduler.scheduled_job("cron", hour=20, minute=40, second=0, id="Jap Reminder")
async def JapReminder():
    await sendGroupMessage(1161079807, MessageChain([
        MessageSegment.plain("今天你学語彙と文法了吗\n今天你刷软考题了吗\n今天你面试了吗\n今天你闻美少女脚臭了吗")
        #MessageSegment.at(1020051753)
    ]))

