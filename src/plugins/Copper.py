from nonebot import on_keyword

copper = on_keyword(["炼", "铜"])

@copper.handle()
async def copper_handler():
    await copper.finish("https://www.66law.cn/zuiming/321.aspx")

