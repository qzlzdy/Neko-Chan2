from nonebot import on_message
from nonebot.adapters import Event
from random import randint

duplicator = on_message()

@duplicator.handle()
async def duplicator_handler(event: Event):
    if randint(0, 9) == 0:
        await duplicator.finish(event.get_plaintext())
