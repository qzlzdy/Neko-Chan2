from nonebot import get_bot
from nonebot.adapters.mirai2.message import MessageChain
import time

ASSETS_ROOT = "/home/alarm/Neko-Chan/Neko-Chan2/assets"

GroupId = [855524548, 1161079807]

async def sendFriendMessage(friend_id, message):
    bot = get_bot()
    await bot.send_friend_message(target=friend_id, message_chain=message)

async def sendGroupMessage(group_id, message):
    bot = get_bot()
    await bot.send_group_message(target=group_id, message_chain=MessageChain(message))

async def sendNotice(desc):
    for group_id in GroupId:
        await sendGroupMessage(group_id, desc)
        time.sleep(1)
