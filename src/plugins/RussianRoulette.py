from random import randint
from nonebot import get_bot, on_command
from nonebot.adapters import Event

roulette = on_command("俄罗斯转盘")

@roulette.handle()
async def russianRoulette_handler(event: Event):
    bot = get_bot()
    groupId = event.get_session_id().split("_")[1]
    memberList = await bot.member_list(target=groupId)
    memberList = [mb["id"] for mb in memberList["data"]]
    luckGuy = memberList[randint(0, len(memberList) - 1)]
    await roulette.send("随机挑选一名幸运群友禁言")
    await bot.mute(target=groupId, member_id=luckGuy, time=randint(60, 600))
