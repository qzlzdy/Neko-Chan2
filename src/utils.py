import time
from nonebot import get_bot

ASSETS_ROOT = "/home/alarm/Neko-Chan/Neko-Chan2/assets"

GROUP_TOKYO = 855524548
GROUP_YANGV = 343327491

GroupId = [GROUP_TOKYO, GROUP_YANGV]

async def sendFriendMessage(friend_id, message):
    bot = get_bot()
    await bot.send_friend_message(target=friend_id, message_chain=message)

async def sendGroupMessage(group_id, message):
    bot = get_bot()
    await bot.send_group_message(target=group_id, message_chain=message)

async def sendNotice(desc):
    for group_id in GroupId:
        await sendGroupMessage(group_id, desc)
        time.sleep(1)
