from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain, MessageSegment
from ..utils import sendFriendMessage, sendGroupMessage

@scheduler.scheduled_job("cron", hour=20, minute=40, second=0, id="Jap Reminder")
async def JapReminder():
    await sendGroupMessage(1161079807, MessageChain([
        MessageSegment.plain("今天你学語彙と文法了吗\n今天你出软考成绩了吗\n今天你签三方了吗\n今天你品尝美少女脚汗了吗")
        #MessageSegment.at(1020051753)
    ]))

