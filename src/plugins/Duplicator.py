from nonebot import on_message
from nonebot.matcher import Matcher
from random import randint

duplicator = on_message()

@duplicator.handle()
async def duplicator_handler(matcher: Matcher):
    if randint(0, 9) == 0:
        await duplicator.finish(matcher.get_plaintext())
