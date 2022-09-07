from nonebot import get_bot
from nonebot.adapters.mirai2.event.base import PrivateChatInfo, GroupChatInfo, GroupInfo
from nonebot.adapters.mirai2.event.message import FriendMessage, GroupMessage
import time

ASSETS_ROOT = "/home/pi/Neko-Chan/Neko-Chan2/assets"

GroupId = [855524548, 1161079807]

async def sendFriendMessage(friend_id, message):
    bot = get_bot()
    await bot.send(FriendMessage(
        self_id=3620447366,
        type="FriendMessage",
        sender=PrivateChatInfo(
            id=friend_id,
            nickname="",
            remark=""
        ),
        messageChain=[]), message)

async def sendGroupMessage(group_id, message):
    bot = get_bot()
    await bot.send(GroupMessage(
      self_id=3620447366,
      type="GroupMessage",
      sender=GroupChatInfo(
        id=0,
        memberName="",
        specialTitle="",
        permission="MEMBER",
        joinTimestamp=0,
        lastSpeakTimestamp=0,
        muteTimeRemaining=0,
        group=GroupInfo(
          id=group_id,
          name="",
          permission="MEMBER"
        )
      ),
      messageChain=[]
    ), message)

async def sendNotice(desc):
    for group_id in GroupId:
        await sendGroupMessage(group_id, desc)
        time.sleep(2)
