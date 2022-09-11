from nonebot import on_keyword

cat = on_keyword(["来点猫猫"])

@cat.handle()
async def cat_handler():
    await cat.finish("/猫猫")
