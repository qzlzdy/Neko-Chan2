from nonebot import require

require("nonebot_plugin_apscheduler")

import time
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain, MessageSegment
from ..utils import sendGroupMessage

@scheduler.scheduled_job("cron", day_of_week="thu", hour=11, minute=0, second=0, id="KFC Brige")
async def kfcBrige():
    now = time.localtime(time.time())
    date = time.strftime("%Y年%m月%d日", now)
    await sendGroupMessage(1161079807, MessageChain([MessageSegment.plain("/V")]))
    await sendGroupMessage(1161079807, MessageChain([MessageSegment.plain(f"{date} 星期四 晴\n今天大胖还没有修好疯狂星期四，这个仇先记下了")]))

