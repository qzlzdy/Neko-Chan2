from nonebot import require

require("nonebot_plugin_apscheduler")

import json
import requests
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain
from nonebot.adapters.mirai2.message import MessageSegment
from ..utils import sendNotice

@scheduler.scheduled_job("cron", hour=11, minute=0, second=0, day_of_week="thu")
async def KfcReminder():
    response = requests.get("https://api.jixs.cc/api/wenan-fkxqs/index.php?type=json")
    text = json.loads(response.text)[0]["kfc"]
    await sendNotice(MessageChain([MessageSegment.plain(text)]))

