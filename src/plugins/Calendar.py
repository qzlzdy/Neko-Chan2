from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain, MessageSegment
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

@scheduler.scheduled_job("cron", month=1, day=1, hour=9, minute=0, second=0, id="Satonaka Chie's Birthday")
async def SatonakaChie():
    with open(f"{ASSETS_ROOT}/calendar/0101-SatonakaChie.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://img.moegirl.org.cn/common/thumb/f/ff/55319988_p0.jpg/420px-55319988_p0.jpg")
    ]))

@scheduler.scheduled_job("cron", month=1, day=4, hour=9, minute=0, second=0, id="Minagi Hiyori's Birthday")
async def MinagiHiyori():
    with open(f"{ASSETS_ROOT}/calendar/0104-MinagiHiyori.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://slowlooptv.com/images/chara/p_001.png")
    ]))

@scheduler.scheduled_job("cron", month=1, day=11, hour=9, minute=0, second=0, id="Miniwa Tsumiki's Birthday")
async def MiniwaTsumiki():
    with open(f"{ASSETS_ROOT}/calendar/0111-MiniwaTsumiki.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.tbs.co.jp/anime/ackc/character/images/chara_img01.jpg")
    ]))

@scheduler.scheduled_job("cron", month=1, day=15, hour=9, minute=0, second=0, id="Akiyama Mio's Birthday")
async def AkiyamaMio():
    with open (f"{ASSETS_ROOT}/calendar/0115-AkiyamaMio.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://img.moegirl.org.cn/common/thumb/2/2e/The_Bowl.jpg/420px-The_Bowl.jpg")
    ]))

@scheduler.scheduled_job("cron", month=1, day=23, hour=9, minute=0, second=0, id="Takimoto Hifumi's Birthday")
async def TakimotoHifumi():
    with open(f"{ASSETS_ROOT}/calendar/0123-TakimotoHifumi.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://newgame-anime.com/assets/character/c4.png")
    ]))

@scheduler.scheduled_job("cron", month=2, day=1, hour=9, minute=0, second=0, id="Yukimi Koume's Birthday")
async def YukimiKoume():
    with open(f"{ASSETS_ROOT}/calendar/0201-YukimiKoume.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.tbs.co.jp/anime/urara/chara/img/koume_left.png")
    ]))

@scheduler.scheduled_job("cron", month=2, day=2, hour=9, minute=0, second=0, id="Suzukaze Aoba's Birthday")
async def SuzukazeAoba():
    with open(f"{ASSETS_ROOT}/calendar/0202-SuzukazeAoba.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://newgame-anime.com/assets/character/c1.png")
    ]))

@scheduler.scheduled_job("cron", month=2, day=2, hour=9, minute=0, second=5, id="Twin Tail Day")
async def TwinTailDay():
    with open(f"{ASSETS_ROOT}/calendar/0202-TainTailDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=2, day=5, hour=9, minute=0, second=0, id="Kasugano Sora's Birthday")
async def KasuganoSora():
    with open(f"{ASSETS_ROOT}/calendar/0205-KasuganoSora.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://img.moegirl.org.cn/common/thumb/7/75/Kasugano_sora_game_CG_ring.jpg/420px-Kasugano_sora_game_CG_ring.jpg")
    ]))

@scheduler.scheduled_job("cron", month=2, day=7, hour=9, minute=0, second=0, id="Futanari Day")
async def FutanariDay():
    with open(f"{ASSETS_ROOT}/calendar/0207-FutanariDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=2, day=8, hour=9, minute=0, second=0, id="Knee-High Day")
async def KneeHighDay():
    with open(f"{ASSETS_ROOT}/calendar/0208-KneeHighDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=2, day=14, hour=9, minute=0, second=0, id="Tedeza Rize's Birthday")
async def TedezaRize():
    with open(f"{ASSETS_ROOT}/calendar/0214-TedezaRize.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://gochiusa.com/core_sys/images/main/cont/chara/rize_body.png")
    ]))

@scheduler.scheduled_job("cron", month=2, day=17, hour=9, minute=0, second=0, id="Shiina's Birthday")
async def Shiina():
    with open(f"{ASSETS_ROOT}/calendar/0217-Shiina.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.tbs.co.jp/anime/koufuku_g/chara/images/chara_img03.jpg")
    ]))

@scheduler.scheduled_job("cron", month=2, day=19, hour=9, minute=0, second=0, id="Morino Mari's Birthday")
async def MorinoMari():
    with open(f"{ASSETS_ROOT}/calendar/0219-MorinoMari.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://koiastv.com/images/chara/p_005.png")
    ]))

@scheduler.scheduled_job("cron", month=2, day=21, hour=9, minute=0, second=0, id="Gotou Hitori's Birthday")
async def GotouHitori():
    with open(f"{ASSETS_ROOT}/calendar/0221-GotouHitori.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://img.moegirl.org.cn/common/thumb/c/c7/Gotou_hitori_goods.jpg/375px-Gotou_hitori_goods.jpg")
    ]))

@scheduler.scheduled_job("cron", month=2, day=23, hour=9, minute=0, second=0, id="Kumegawa Botan's Birthday")
async def KumegawaBotan():
    with open(f"{ASSETS_ROOT}/calendar/0223-KumegawaBotan.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://anne-happy.com/wp-content/uploads/2016/02/ch3-2.png")
    ]))

@scheduler.scheduled_job("cron", month=3, day=3, hour=9, minute=0, second=0, id="Koizuka Koyume's Birthday")
async def KoizukaKoyume():
    with open(f"{ASSETS_ROOT}/calendar/0303-KoizukaKoyume.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://comic-girls.com/character/img/chara2.png")
    ]))

@scheduler.scheduled_job("cron", month=3, day=3, hour=9, minute=0, second=5, id="Momoki Run's Birthday")
async def MomokiRun():
    with open(f"{ASSETS_ROOT}/calendar/0303-MomokiRun.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.a-ch.jp/character/img/ch02.jpg")
    ]))

@scheduler.scheduled_job("cron", month=3, day=3, hour=9, minute=0, second=10, id="Nakamachi Kana's Birthday")
async def NakamachiKana():
    with open(f"{ASSETS_ROOT}/calendar/0303-NakamachiKana.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.tv-tokyo.co.jp/contents/kanamemo/chara/images/chara_01.jpg")
    ]))

@scheduler.scheduled_job("cron", month=3, day=4, hour=9, minute=0, second=0, id="Kagamihara Nadeshiko's Birthday")
async def KagamiharaNadeshiko():
    with open(f"{ASSETS_ROOT}/calendar/0304-KagamiharaNadeshiko.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://yurucamp.jp/first/images/chara_list1.png")
    ]))

@scheduler.scheduled_job("cron", month=3, day=15, hour=9, minute=0, second=0, id="Tatusmi Kon's Birthday")
async def TatsumiKon():
    with open(f"{ASSETS_ROOT}/calendar/0315-TatsumiKon.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.tbs.co.jp/anime/urara/chara/img/kon_left.png")
    ]))

@scheduler.scheduled_job("cron", month=4, day=3, hour=9, minute=0, second=0, id="Kurawashi Riko's Birthday")
async def KurawashiRiko():
    with open(f"{ASSETS_ROOT}/calendar/0403-KurawashiRiko.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.love-lab.tv/chara/img/riko00.jpg?1680924886863")
    ]))

@scheduler.scheduled_job("cron", month=4, day=4, hour=9, minute=0, second=0, id="Sakuranomiya Maika's Birthday")
async def SakuranomiyaMaika():
    with open(f"{ASSETS_ROOT}/calendar/0404-SakuranomiyaMaika.txt", "r"):
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://blend-s.jp/assets/img/character/chara_01/02.png")
    ]))

@scheduler.scheduled_job("cron", month=4, day=4, hour=9, minute=0, second=5, id="Sakura Ino's Birthday")
async def SakuraIno():
    with open(f"{ASSETS_ROOT}/calendar/0404-SakuraIno.txt", "r"):
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://ochifuru-anime.com/images/chara/001/p_002.png")
    ]))

@scheduler.scheduled_job("cron", month=4, day=5, hour=9, minute=0, second=0, id="Takeya Yuki's Birthday")
async def TakeyaYuki():
    with open(f"{ASSETS_ROOT}/calenadr/0405-TakeyaYuki.txt", "r"):
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://gakkougurashi.com/core_sys/images/main/cont/chara/ch01-1.png")
    ]))

@scheduler.scheduled_job("cron", month=4, day=5, hour=9, minute=0, second=5, id="Alice·Cartelet's Birthday")
async def AliceCartelet():
    with open(f"{ASSETS_ROOT}/calendar/0405-AliceCartelet.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="http://kinmosa.com/series/images/s2character/c2.png")
    ]))

@scheduler.scheduled_job("cron", month=4, day=6, hour=9, minute=0, second=0, id="Higa Kanata's Birthday")
async def HigaKanata():
    with open(f"{ASSETS_ROOT}/calendar/0406-HigaKanata.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://www.harukana-receive.jp/assets/character/1b.png")
    ]))

@scheduler.scheduled_job("cron", month=4, day=6, hour=9, minute=0, second=5, id="Ichinose Hana's Birthday")
async def IchinoseHana():
    with open(f"{ASSETS_ROOT}/calendar/0406-IchinoseHana.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://slow-start.com/shared/images/top/chara_d_hana_img.png")
    ]))

@scheduler.scheduled_job("cron", month=5, day=10, hour=9, minute=0, second=0, id="Maid Day")
async def MaidDay():
    with open(f"{ASSETS_ROOT}/calendar/0510-MaidDay.txt", "r") as f:
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

@scheduler.scheduled_job("cron", month=12, day=23, hour=9, minute=0, second=0, id="Hoshikawa Mafuyu's Birthday")
async def HoshikawaMafuyu():
    with open(f"{ASSETS_ROOT}/calendar/1223-HoshikawaMafuyu.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://blend-s.jp/assets/img/character/chara_03/chara03_1.png")
    ]))

@scheduler.scheduled_job("cron", month=12, day=25, hour=9, minute=0, second=0, id="Itou Makoto Dead")
async def ItouMakotoDead():
    with open(f"{ASSETS_ROOT}/calendar/1225-ItouMakotoDead.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://bkimg.cdn.bcebos.com/pic/adaf2edda3cc7cd98d10aacc8c4b363fb80e7bec3bd9?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U5Mg==,g_7,xp_5,yp_5")
    ]))

@scheduler.scheduled_job("cron", month=12, day=31, hour=9, minute=0, second=0, id="Hanakoizumi Anne's Birthday")
async def HanakoizumiAnne():
    with open(f"{ASSETS_ROOT}/calendar/1231-HanakoizumiAnne.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url="https://anne-happy.com/wp-content/uploads/2016/02/ch1-1-1.png")
    ]))
