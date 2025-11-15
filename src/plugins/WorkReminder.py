from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11.message import MessageSegment
from ..utils import GROUP_YANGV
from ..utils import sendGroupMessage

@scheduler.scheduled_job("cron", hour=20, minute=45, second=0, id="Jap Reminder")
async def JapReminder():
    await sendGroupMessage(GROUP_YANGV, Message([
        MessageSegment.text("今天你学語彙と文法了吗\n今天你软考五战了吗\n今天你被用户投诉了吗\n今天你品尝美少女脚汗了吗")
        #MessageSegment.at(1020051753)
    ]))
