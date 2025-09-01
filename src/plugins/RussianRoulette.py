from random import randint
from nonebot import get_bot, on_command
from nonebot.adapters import Event

roulette = on_command("俄罗斯转盘")

@roulette.handle()
async def russianRoulette_handler(event: Event):
    bot = get_bot()
    groupId = event.get_session_id().split("_")[1]
    memberList = await bot.get_group_member_list(group_id=groupId)
    memberList = [mb["user_id"] for mb in memberList]
    luckGuy = memberList[randint(0, len(memberList) - 1)]
    await roulette.send("随机挑选一名幸运群友禁言")
    await bot.set_group_ban(group_id=groupId, user_id=luckGuy, duration=randint(60, 600))
