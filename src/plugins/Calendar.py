from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain
from nonebot.adapters.mirai2.message import MessageSegment
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
async def HatsuneMikuBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0831-HatsuneMikuBirthday.txt", "r") as f:
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

@scheduler.scheduled_job("cron", month=9, day=12, hour=9, minute=0, second=0, id="Minami Kotori's Birthday")
async def MinamiKotoriBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0912-MinamiKotoriBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.lovelive-anime.jp/otonokizaka/worldwide/img/member/member03_01.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=15, hour=9, minute=0, second=0, id="Komichi Aya's Birthday")
async def KomichiAyaBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0915-KomichiAyaBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://kinmosa.com/assets/character/c/3.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=19, hour=9, minute=0, second=0, id="Ujimatsu Chiya's Birthday")
async def UjimatsuChiyaBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0919-UjimatsuChiyaBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://gochiusa.com/core_sys/images/main/cont/chara/chiya_body.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=21, hour=9, minute=0, second=0, id="Kurosawa Ruby's Birthday")
async def KurosawaRubyBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0921-KurosawaRubyBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.lovelive-anime.jp/uranohoshi/js/sunshine_member4.hyperesources/09b-1.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=26, hour=9, minute=0, second=0, id="Doma Umaru's Birthday")
async def DomaUmaruBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0926-DomaUmaruBirthday.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://umaru-ani.me/img/character/chara1_stand.png")
    ]))

@scheduler.scheduled_job("cron", month=9, day=28, hour=9, minute=0, second=0, id="Yoshida Yuuko's Biethday")
async def YoshidaYuukoBirthday():
    with open(f"{ASSETS_ROOT}/calendar/0928-YoshidaYuukoBirthday.txt", "r") as f:
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

@scheduler.scheduled_job("cron", month=10, day=28, hour=9, minute=0, second=0, id="Koishi x2 Day")
async def KoishiX2Day():
    with open(f"{ASSETS_ROOT}/calendar/1028-KoishiX2Day.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://static.wikia.nocookie.net/touhou/images/6/6e/Koishi.png/revision/latest/scale-to-width-down/200?cb=20091024182756")
    ]))

@scheduler.scheduled_job("cron", month=11, day=2, hour=9, minute=0, second=0, id="Tights Day")
async def TightsDay():
    with open(f"{ASSETS_ROOT}/calendar/1102-TightsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)
