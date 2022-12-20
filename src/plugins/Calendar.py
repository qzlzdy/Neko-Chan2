from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain, MessageSegment
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

@scheduler.scheduled_job("cron", month=2, day=2, hour=9, minute=0, second=0, id="Twin Tail Day")
async def TwinTailDay():
    with open(f"{ASSETS_ROOT}/calendar/0202-TainTailDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=1, hour=9, minute=0, second=0, id="Oppai Day")
async def OppaiDay():
    with open(f"{ASSETS_ROOT}/calendar/0801-OppaiDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=2, hour=9, minute=0, second=0, id="Pants Day")
async def PantsDay():
    with open(f"{ASSETS_ROOT}/calendar/0802-PantsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=8, day=31, hour=9, minute=0, second=0, id="Hatsune Miku's Birthday")
async def HatsuneMiku():
    with open(f"{ASSETS_ROOT}/calendar/0831-HatsuneMiku.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://ec.crypton.co.jp/img/special/vocaloid/img_MIKU_us.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=8, hour=9, minute=0, second=0, id="Kupa Day")
async def KupaDay():
    with open(f"{ASSETS_ROOT}/calendar/0908-KupaDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=9, hour=9, minute=9, second=9, id="Cirno Day")
async def CirnoDay():
    with open(f"{ASSETS_ROOT}/calendar/0909-CirnoDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=15, hour=9, minute=0, second=0, id="Komichi Aya's Birthday")
async def KomichiAya():
    with open(f"{ASSETS_ROOT}/calendar/0915-KomichiAya.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://kinmosa.com/assets/character/c/3.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=19, hour=9, minute=0, second=0, id="Ujimatsu Chiya's Birthday")
async def UjimatsuChiya():
    with open(f"{ASSETS_ROOT}/calendar/0919-UjimatsuChiya.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://gochiusa.com/core_sys/images/main/cont/chara/chiya_body.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=26, hour=9, minute=0, second=0, id="Doma Umaru's Birthday")
async def DomaUmaru():
    with open(f"{ASSETS_ROOT}/calendar/0926-DomaUmaru.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://umaru-ani.me/img/character/chara1_stand.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=28, hour=9, minute=0, second=0, id="Yoshida Yuuko's Biethday")
async def YoshidaYuuko():
    with open(f"{ASSETS_ROOT}/calendar/0928-YoshidaYuuko.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.tbs.co.jp/anime/machikado/1st/character/img/chara_img_01.png")
    ]))

@scheduler.scheduled_job("cron", month=10, day=10, hour=9, minute=0, second=0, id="Moe Day")
async def MoeDay():
    with open(f"{ASSETS_ROOT}/calendar/1010-MoeDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=10, day=11, hour=9, minute=0, second=0, id="Loli Day")
async def LoliDay():
    with open(f"{ASSETS_ROOT}/calendar/1011-LoliDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=10, day=24, hour=9, minute=0, second=0, id="1024 Day")
async def ProgrammerDay():
    with open(f"{ASSETS_ROOT}/calendar/1024-1024Day.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=11, day=2, hour=9, minute=0, second=0, id="Tights Day")
async def TightsDay():
    with open(f"{ASSETS_ROOT}/calendar/1102-TightsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=11, day=4, hour=9, minute=0, second=0, id="Good Butt")
async def GoodButt():
    with open(f"{ASSETS_ROOT}/calendar/1104-GoodButtDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=11, day=7, hour=9, minute=0, second=0, id="Good Belly")
async def GoodBelly():
    with open(f"{ASSETS_ROOT}/calendar/1107-GoodBellyDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=11, day=8, hour=9, minute=0, second=0, id="Good Oppai Day")
async def GoodOppai():
    with open(f"{ASSETS_ROOT}/calendar/1108-GoodOppaiDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=11, day=27, hour=9, minute=0, second=0, id="Hirasawa Yui's Birthday")
async def HirasawaYui():
    with open(f"{ASSETS_ROOT}/calendar/1127-HirasawaYui.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo01_1.gif")
    ]))

@scheduler.scheduled_job("cron", month=11, day=29, hour=9, minute=0, second=0, id="Good Meat Day")
async def GoodMeat():
    with open(f"{ASSETS_ROOT}/calendar/1129-GoodMeatDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=12, day=4, hour=9, minute=0, second=0, id="Kafuu Chino's Birthday")
async def KafuuChino():
    with open(f"{ASSETS_ROOT}/calendar/1204-KafuuChino.txt", "r") as f:
        desc = f.read()
    await sendNotive(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://gochiusa.com/core_sys/images/main/cont/chara/chino_body.png")
    ]))

@scheduler.scheduled_job("cron", month=12, day=25, hour=9, minute=0, second=0, id="Itou Makoto Dead")
async def ItouMakotoDead():
    with open(f"{ASSETS_ROOT}/calendar/1225-ItouMakoto.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://bkimg.cdn.bcebos.com/pic/adaf2edda3cc7cd98d10aacc8c4b363fb80e7bec3bd9?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U5Mg==,g_7,xp_5,yp_5")
    ]))
