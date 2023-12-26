from nonebot import require

require("nonebot_plugin_apscheduler")

import base64
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain
from nonebot.adapters.mirai2.message import MessageSegment
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

async def sendBirthdayNote(character, url):
    with open(f"{ASSETS_ROOT}/calendar/{character}.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(url=url)
    ]))

@scheduler.scheduled_job("cron", month=1, day=1, hour=9, minute=0, second=0, id="Satonaka Chie's Birthday")
async def SatonakaChie():
    await sendBirthdayNote(
        "0101-SatonakaChie",
        url="https://img.moegirl.org.cn/common/thumb/f/ff/55319988_p0.jpg/420px-55319988_p0.jpg")

@scheduler.scheduled_job("cron", month=1, day=4, hour=9, minute=0, second=0, id="Minagi Hiyori's Birthday")
async def MinagiHiyori():
    await sendBirthdayNote(
        "0104-MinagiHiyori",
        url="https://slowlooptv.com/images/chara/p_001.png")

@scheduler.scheduled_job("cron", month=1, day=11, hour=9, minute=0, second=0, id="Miniwa Tsumiki's Birthday")
async def MiniwaTsumiki():
    await sendBirthdayNote(
        "0111-MiniwaTsumiki",
        url="https://www.tbs.co.jp/anime/ackc/character/images/chara_img01.jpg")

@scheduler.scheduled_job("cron", month=1, day=15, hour=9, minute=0, second=0, id="Akiyama Mio's Birthday")
async def AkiyamaMio():
    await sendBirthdayNote(
        "0115-AkiyamaMio",
        url="https://img.moegirl.org.cn/common/thumb/2/2e/The_Bowl.jpg/420px-The_Bowl.jpg")

@scheduler.scheduled_job("cron", month=1, day=23, hour=9, minute=0, second=0, id="Takimoto Hifumi's Birthday")
async def TakimotoHifumi():
    await sendBirthdayNote(
        "0123-TakimotoHifumi",
        url="http://newgame-anime.com/assets/character/c4.png")

@scheduler.scheduled_job("cron", month=2, day=1, hour=9, minute=0, second=0, id="Yukimi Koume's Birthday")
async def YukimiKoume():
    await sendBirthdayNote(
        "0201-YukimiKoume",
        url="https://www.tbs.co.jp/anime/urara/chara/img/koume_left.png")

@scheduler.scheduled_job("cron", month=2, day=2, hour=9, minute=0, second=0, id="Suzukaze Aoba's Birthday")
async def SuzukazeAoba():
    await sendBirthdayNote(
        "0202-SuzukazeAoba",
        url="http://newgame-anime.com/assets/character/c1.png")

@scheduler.scheduled_job("cron", month=2, day=2, hour=9, minute=0, second=5, id="Tsutsukakushi Tsukiko's Birthday")
async def TsutsukakushiTsukiko():
    await sendBirthdayNote(
        "0202-TsutsukakushiTsukiko",
        url="http://www.henneko.jp/character/img/p_tsukiko.png")

@scheduler.scheduled_job("cron", month=2, day=5, hour=9, minute=0, second=0, id="Kasugano Sora's Birthday")
async def KasuganoSora():
    await sendBirthdayNote(
        "0205-KasuganoSora",
        url="https://img.moegirl.org.cn/common/thumb/7/75/Kasugano_sora_game_CG_ring.jpg/420px-Kasugano_sora_game_CG_ring.jpg")

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
    await sendBirthdayNote(
        "0214-TedezaRize",
        url="https://gochiusa.com/core_sys/images/main/cont/chara/rize_body.png")

@scheduler.scheduled_job("cron", month=2, day=17, hour=9, minute=0, second=0, id="Shiina's Birthday")
async def Shiina():
    await sendBirthdayNote(
        "0217-Shiina",
        url="https://www.tbs.co.jp/anime/koufuku_g/chara/images/chara_img03.jpg")

@scheduler.scheduled_job("cron", month=2, day=21, hour=9, minute=0, second=0, id="Gotou Hitori's Birthday")
async def GotouHitori():
    await sendBirthdayNote(
        "0221-GotouHitori",
        url="https://img.moegirl.org.cn/common/thumb/c/c7/Gotou_hitori_goods.jpg/375px-Gotou_hitori_goods.jpg")

@scheduler.scheduled_job("cron", month=2, day=23, hour=9, minute=0, second=0, id="Kumegawa Botan's Birthday")
async def KumegawaBotan():
    await sendBirthdayNote(
        "0223-KumegawaBotan",
        url="https://anne-happy.com/wp-content/uploads/2016/02/ch3-2.png")

@scheduler.scheduled_job("cron", month=3, day=3, hour=9, minute=0, second=0, id="Koizuka Koyume's Birthday")
async def KoizukaKoyume():
    await sendBirthdayNote(
        "0303-KoizukaKoyume",
        url="http://comic-girls.com/character/img/chara2.png")

@scheduler.scheduled_job("cron", month=3, day=3, hour=9, minute=0, second=5, id="Momoki Run's Birthday")
async def MomokiRun():
    await sendBirthdayNote(
        "0303-MomokiRun",
        url="https://www.a-ch.jp/character/img/ch02.jpg")

@scheduler.scheduled_job("cron", month=3, day=3, hour=9, minute=0, second=10, id="Nakamachi Kana's Birthday")
async def NakamachiKana():
    await sendBirthdayNote(
        "0303-NakamachiKana",
        url="https://www.tv-tokyo.co.jp/contents/kanamemo/chara/images/chara_01.jpg")

@scheduler.scheduled_job("cron", month=3, day=4, hour=9, minute=0, second=0, id="Kagamihara Nadeshiko's Birthday")
async def KagamiharaNadeshiko():
    await sendBirthdayNote(
        "0304-KagamiharaNadeshiko",
        url="https://yurucamp.jp/first/images/chara_list1.png")

@scheduler.scheduled_job("cron", month=3, day=10, hour=9, minute=0, second=0, id="Saten Ruiko's Birthday")
async def SatenRuiko():
    await sendBirthdayNote(
        "0310-SatenRuiko",
        url="https://toaru-project.com/railgun_t/core_sys/images/main/cont_chara/11_body.png")

@scheduler.scheduled_job("cron", month=3, day=15, hour=9, minute=0, second=0, id="Tatusmi Kon's Birthday")
async def TatsumiKon():
    await sendBirthdayNote(
        "0315-TatsumiKon",
        url="https://www.tbs.co.jp/anime/urara/chara/img/kon_left.png")

@scheduler.scheduled_job("cron", month=3, day=20, hour=9, minute=0, second=0, id="Himekawa Yoshino's Birthday")
async def HimekawaYoshino():
    await sendBirthdayNote(
        "0320-HimekawaYoshino",
        url="https://date-a-live-anime.com/1st-2nd/common/images/2nd/character/character_yoshino.png")

@scheduler.scheduled_job("cron", month=4, day=3, hour=9, minute=0, second=0, id="Kurawashi Riko's Birthday")
async def KurawashiRiko():
    await sendBirthdayNote(
        "0403-KurawashiRiko",
        url="https://www.love-lab.tv/chara/img/riko00.jpg?1680924886863")

@scheduler.scheduled_job("cron", month=4, day=4, hour=9, minute=0, second=0, id="Sakuranomiya Maika's Birthday")
async def SakuranomiyaMaika():
    await sendBirthdayNote(
        "0404-SakuranomiyaMaika",
        url="https://blend-s.jp/assets/img/character/chara_01/02.png")

@scheduler.scheduled_job("cron", month=4, day=4, hour=9, minute=0, second=5, id="Sakura Ino's Birthday")
async def SakuraIno():
    await sendBirthdayNote(
        "0404-SakuraIno",
        url="http://ochifuru-anime.com/images/chara/001/p_002.png")

@scheduler.scheduled_job("cron", month=4, day=4, hour=9, minute=0, second=10, id="Azuki Azusa's Birthday")
async def AzukiAzusa():
    await sendBirthdayNote(
        "0404-AzukiAzusa",
        url="http://www.henneko.jp/character/img/p_azusa.png")

@scheduler.scheduled_job("cron", month=4, day=5, hour=9, minute=0, second=0, id="Takeya Yuki's Birthday")
async def TakeyaYuki():
    await sendBirthdayNote(
        "0405-TakeyaYuki",
        url="https://gakkougurashi.com/core_sys/images/main/cont/chara/ch01-1.png")

@scheduler.scheduled_job("cron", month=4, day=5, hour=9, minute=0, second=5, id="Alice·Cartelet's Birthday")
async def AliceCartelet():
    await sendBirthdayNote(
        "0405-AliceCartelet",
        url="http://kinmosa.com/series/images/s2character/c2.png")

@scheduler.scheduled_job("cron", month=4, day=6, hour=9, minute=0, second=0, id="Higa Kanata's Birthday")
async def HigaKanata():
    await sendBirthdayNote(
        "0406-HigaKanata",
        url="https://www.harukana-receive.jp/assets/character/1b.png")

@scheduler.scheduled_job("cron", month=4, day=6, hour=9, minute=0, second=5, id="Ichinose Hana's Birthday")
async def IchinoseHana():
    await sendBirthdayNote(
        "0406-IchinoseHana",
        url="https://slow-start.com/shared/images/top/chara_d_hana_img.png")

@scheduler.scheduled_job("cron", month=4, day=8, hour=9, minute=0, second=0, id="Kousaka Kirino's Birthday")
async def KousakaKirino():
    await sendBirthdayNote(
        "0408-KousakaKirino",
        url="https://www.oreimo-anime.com/1st/chara/img/chara01.jpg")

@scheduler.scheduled_job("cron", month=4, day=10, hour=9, minute=0, second=0, id="Hoto Kokoa's Birthday")
async def HotoKokoa():
    await sendBirthdayNote(
        "0410-HotoKokoa",
        url="https://gochiusa.com/core_sys/images/main/cont/chara/cocoa_body.png")

@scheduler.scheduled_job("cron", month=4, day=11, hour=9, minute=0, second=0, id="Amano Saki's Birthday")
async def AmanoSkai():
    await sendBirthdayNote(
        "0411-AmanoSaki",
        url="https://www.tv-tokyo.co.jp/contents/kanamemo/chara/images/chara_02.jpg")

@scheduler.scheduled_job("cron", month=4, day=12, hour=9, minute=0, second=0, id="Sawatari Uki's Birthday")
async def SawatariUki():
    await sendBirthdayNote(
        "0412-SawatariUki",
        url="http://animayell.com/core_sys/images/main/cont/chara/main_uki.png")

@scheduler.scheduled_job("cron", month=4, day=20, hour=9, minute=0, second=0, id="Gokou Ruri's Birthday")
async def GokouRuri():
    await sendBirthdayNote(
        "0420-GokouRuri",
        url="https://www.oreimo-anime.com/1st/chara/img/chara04.jpg")

@scheduler.scheduled_job("cron", month=4, day=21, hour=9, minute=0, second=0, id="Kita Ikuyo's Birthday")
async def KitaIkuyo():
    await sendBirthdayNote(
        "0421-KitaIkuyo",
        url="https://bocchi.rocks/assets/img/page/character/ikuyo/main.png")

@scheduler.scheduled_job("cron", month=4, day=27, hour=9, minute=0, second=0, id="Misaki Mei's Birthday")
async def MisakiMei():
    await sendBirthdayNote(
        "0427-MisakiMei",
        url="https://www.pa-works.jp/wp-content/uploads/2012/04/08_another-727x1024.jpg")

@scheduler.scheduled_job("cron", month=5, day=1, hour=9, minute=0, second=0, id="Ichii Yui's Birthday")
async def IchiiYui():
    await sendBirthdayNote(
        "0501-IchiiYui",
        url="https://www.yuyushiki.net/core_sys/images/main/cont/chara/chara2_cos1.jpg")

@scheduler.scheduled_job("cron", month=5, day=2, hour=9, minute=0, second=0, id="Hana N Fountainstand's Birthday")
async def HanaNFountainstand():
    await sendBirthdayNote(
        "0502-HanaNFountainstand",
        url="https://hanayamata.com/assets/images/profile/chara02_off.png")

@scheduler.scheduled_job("cron", month=5, day=2, hour=9, minute=0, second=5, id="Odagiri Futaba's Birthday")
async def OdagiriFutaba():
    await sendBirthdayNote(
        "0502-OdagiriFutaba",
        url="https://sansyasanyou.com/core_sys/images/contents/00000003/base/sn_001.png?1552483627")

@scheduler.scheduled_job("cron", month=5, day=2, hour=9, minute=0, second=10, id="Misaka Mikoto's Birthday")
async def MisakaMikoto():
    await sendBirthdayNote(
        "0502-MisakaMikoto",
        url="https://toaru-project.com/railgun/core_sys/images/contents/00000004/base/001.jpg?1615808050")

@scheduler.scheduled_job("cron", month=5, day=2, hour=9, minute=0, second=15, id="Aragaki Ayase's Birthday")
async def AragakiAyase():
    await sendBirthdayNote(
        "0502-AragakiAyase",
        url="https://www.oreimo-anime.com/1st/chara/img/chara06.jpg")

@scheduler.scheduled_job("cron", month=5, day=4, hour=9, minute=0, second=0, id="Katsuki Tsubasa's Birthday")
async def KatsukiTsubasa():
    await sendBirthdayNote(
        "0504-KatsukiTsubasa",
        url="http://comic-girls.com/character/img/chara4.png")

@scheduler.scheduled_job("cron", month=5, day=10, hour=9, minute=0, second=0, id="Maid Day")
async def MaidDay():
    with open(f"{ASSETS_ROOT}/calendar/0510-MaidDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=5, day=15, hour=9, minute=0, second=0, id="Stocking Day")
async def StockingDay():
    with open(f"{ASSETS_ROOT}/calendar/0515-StockingDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=5, day=23, hour=9, minute=0, second=0, id="Kiss Day")
async def KissDay():
    with open(f"{ASSETS_ROOT}/calendar/0523-KissDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=5, day=24, hour=9, minute=0, second=0, id="Nishi Yuuko's Birthday")
async def NishiYuuko():
    await sendBirthdayNote(
        "0524-NishiYuuko",
        url="https://www.a-ch.jp/character/img/ch03.jpg")

@scheduler.scheduled_job("cron", month=5, day=28, hour=9, minute=0, second=0, id="Izumi Konata's Birthday")
async def IzumiKonata():
    await sendBirthdayNote(
        "0528-IzumiKonata",
        url="https://img.moegirl.org.cn/common/thumb/0/0e/Izumi_Konata_Hinnyuu.jpg/450px-Izumi_Konata_Hinnyuu.jpg")

@scheduler.scheduled_job("cron", month=5, day=28, hour=9, minute=0, second=5, id="Ichijyou Hotaru's Birthday")
async def IchijyouHotaru():
    await sendBirthdayNote(
        "0528-IchijyouHotaru",
        url="https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/hotaru/ph_front_01.png")

@scheduler.scheduled_job("cron", month=5, day=29, hour=9, minute=0, second=0, id="Ijichi Nijika's Birthday")
async def IjichiNijika():
    await sendBirtdayNote(
        "0529-IjichiNijika",
        url="https://bocchi.rocks/assets/img/page/character/nijika/main.png")

@scheduler.scheduled_job("cron", month=6, day=1, hour=9, minute=0, second=0, id="Sasame Yaya's Birthday")
async def SasameYaya():
    await sendBirthdayNote(
        "0601-SasameYaya",
        url="https://hanayamata.com/assets/images/profile/chara03_off.png")

@scheduler.scheduled_job("cron", month=6, day=3, hour=9, minute=0, second=0, id="Sengoku Nadeko's Birthday")
async def SengokuNadeko():
    await sendBirthdayNote(
        "0603-SengokuNadeko",
        url="https://www.monogatari-series.com/bakemonogatari/chara/images/i04.jpg")

@scheduler.scheduled_job("cron", month=6, day=9, hour=9, minute=0, second=0, id="Amano Miu's Birthday")
async def AmanoMiu():
    await sendBirthdayNote(
        "0609-AmanoMiu",
        url="https://blend-s.jp/assets/img/character/chara_04/chara04_1.png")

@scheduler.scheduled_job("cron", month=6, day=10, hour=9, minute=0, second=0, id="Tokisaki Kurumi's Birthday")
async def TokisakiKurumi():
    await sendBirthdayNote(
        "0610-TokisakiKurumi",
        url="https://date-a-live4th-anime.com/common/images/character/character06.png")

@scheduler.scheduled_job("cron", month=6, day=12, hour=9, minute=0, second=0, id="Takanashi Rikkai's Birthday")
async def TakanashiRikka():
    await sendBirthdayNote(
        "0612-TakanashiRikka",
        url="https://www.anime-chu-2.com/tv/img/character/rikka/01.png")

@scheduler.scheduled_job("cron", month=6, day=13, hour=9, minute=0, second=0, id="Konohata Mira's Birthday")
async def KonohataMira():
    await sendBirthdayNote(
        "0613-KonohataMira",
        url="http://koiastv.com/images/chara/p_001.png")

@scheduler.scheduled_job("cron", month=6, day=20, hour=9, minute=0, second=0, id="Tokura Eiko's Birthday")
async def TokuraEiko():
    await sendBirthdayNote(
        "0620-TokuraEiko",
        url="https://slow-start.com/shared/images/top/chara_d_eiko_img.png")

@scheduler.scheduled_job("cron", month=6, day=22, hour=9, minute=0, second=0, id="Machiko Ryou's Birthday")
async def MachikoRyou():
    await sendBirthdayNote(
        "0622-MachikoRyou",
        url="https://www.tbs.co.jp/anime/koufuku_g/chara/images/chara_img01.jpg")

@scheduler.scheduled_job("cron", month=6, day=24, hour=9, minute=0, second=0, id="Sonoda Yuu's Birthday")
async def SonodaYuu():
    await sendBirthdayNote(
        "0624-SonodaYuu",
        url="https://www.tbs.co.jp/anime/sakura/chara/images/chara_img02.jpg")

@scheduler.scheduled_job("cron", month=6, day=30, hour=9, minute=0, second=0, id="Yoshinaga Koi's Birthday")
async def YoshinagaKoi():
    await sendBirthdayNote(
        "0630-YoshinagaKoi",
        url="https://slowlooptv.com/images/chara/p_003.png")

@scheduler.scheduled_job("cron", month=7, day=2, hour=9, minute=0, second=0, id="Kotobuki Tsumugi's Birthday")
async def KotobukiTsumugi():
    await sendBirthdayNote(
        "0702-KotobukiTsumugi",
        url="https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo04.gif")

@scheduler.scheduled_job("cron", month=7, day=4, hour=9, minute=0, second=0, id="Hatoya Kohane's Birthday")
async def HatoyaKohane():
    await sendBirthdayNote(
        "0704-HatoyaKohane",
        url="http://animayell.com/core_sys/images/main/cont/chara/details_kohane_school.png")

@scheduler.scheduled_job("cron", month=7, day=7, hour=9, minute=0, second=0, id="Senjyougahara Hitagi's Birthday")
async def SenjyougaharaHitagi():
    await sendBirthdayNote(
        "0707-SenjyougaharaHitagi",
        url="https://www.monogatari-series.com/bakemonogatari/chara/images/i01.jpg")

@scheduler.scheduled_job("cron", month=7, day=9, hour=9, minute=0, second=0, id="Hibarigaoka Ruri's Birthday")
async def HibarigaokaRuri():
    await sendBirthdayNote(
        "0709-HibarigaokaRuri",
        url="https://anne-happy.com/wp-content/uploads/2016/02/ch2-1-1.png")

@scheduler.scheduled_job("cron", month=7, day=10, hour=9, minute=0, second=0, id="Kanzaki Hideri's Birthday")
async def KanzakiHideri():
    await sendBirthdayNote(
        "0710-KanzakiHideri",
        url="https://blend-s.jp/assets/img/character/chara_05/chara05_1.png")

@scheduler.scheduled_job("cron", month=7, day=15, hour=9, minute=0, second=0, id="Kirima Sharo's Birthday")
async def KirimaSharo():
    await sendBirthdayNote(
        "0715-KirimaSharo",
        url="https://gochiusa.com/core_sys/images/main/cont/chara/syaro_body.png")

@scheduler.scheduled_job("cron", month=7, day=17, hour=9, minute=0, second=0, id="Kurokawa Mao's Birthday")
async def KurokawaMao():
    await sendBirthdayNote(
        "0717-KurokawaMao",
        url="https://wakabagirl.com/core_sys/images/contents/00000010/base/001.jpg?1555054911")

@scheduler.scheduled_job("cron", month=7, day=21, hour=9, minute=0, second=0, id="Onanie Day")
async def OnanieDay():
    with open(f"{ASSETS_ROOT}/calendar/0721-OnanieDay.txt", "r") as f:
        desc = f.read()
    infile = open(f"{ASSETS_ROOT}/0721.jpg", "rb").read()
    buf = base64.b64encode(infile)
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(base64=str(buf, "utf-8"))
    ]))

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

@scheduler.scheduled_job("cron", month=8, day=3, hour=9, minute=0, second=0, id="Itsuka Kotori's Birthday")
async def ItsukaKotori():
    await sendBirthdayNote(
        "0803-ItsukaKotori",
        url="https://date-a-live-anime.com/1st-2nd/common/images/2nd/character/character_kotori.png")

@scheduler.scheduled_job("cron", month=8, day=11, hour=9, minute=0, second=0, id="Nishikawa Yoko's Birthday")
async def NishikawaYoko():
    await sendBirthdayNote(
        "0811-NishikawaYoko",
        url="http://sansyasanyou.com/core_sys/images/contents/00000002/base/sn_001.png?1552483627")

@scheduler.scheduled_job("cron", month=8, day=12, hour=9, minute=0, second=0, id="Hinata Kaho's Birthday")
async def HinataKaho():
    await sendBirthdayNote(
        "0812-HinataKaho",
        url="https://blend-s.jp/assets/img/character/chara_02/chara02_1.png")

@scheduler.scheduled_job("cron", month=8, day=20, hour=9, minute=0, second=0, id="Inokuma Youko's Birthday")
async def InokumaYouko():
    await sendBirthdayNote(
        "0820-InokumaYouko",
        url="http://www.kinmosa.com/series/images/s2character/c4.png")

@scheduler.scheduled_job("cron", month=8, day=21, hour=9, minute=0, second=0, id="Tainaka Ritsu's Birthday")
async def TainakaRitsu():
    await sendBirthdayNote(
        "0821-TainakaRitsu",
        url="https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo03.gif")

@scheduler.scheduled_job("cron", month=8, day=23, hour=9, minute=0, second=0, id="Maki Natsuo's Birthday")
async def MakiNatsuo():
    await sendBirthdayNote(
        "0823-MakiNatsuo",
        url="https://www.love-lab.tv/chara/img/maki00.jpg")

@scheduler.scheduled_job("cron", month=8, day=25, hour=9, minute=0, second=0, id="Takayama Haruka's Birthday")
async def TakayamaHaruka():
    await sendBirthdayNote(
        "0825-TakayamaHaruka",
        url="https://www.tbs.co.jp/anime/sakura/chara/images/chara_img01.jpg")

@scheduler.scheduled_job("cron", month=8, day=28, hour=9, minute=0, second=0, id="Honda Tamaki's Birthday")
async def HondaTamaki():
    await sendBirthdayNote(
        "0828-HondaTamaki",
        url="http://www.dokidokivisual.com/magic_of_stella/img/banner/banner_kari_anim_l.jpg")

@scheduler.scheduled_job("cron", month=8, day=28, hour=9, minute=0, second=5, id="Asahina Mikuru's Birthday")
async def AsahinaMikuru():
    await sendBirthdayNote(
        "0828-AsahinaMikuru",
        url="https://img.moegirl.org.cn/common/thumb/3/39/1096%E5%A5%B3%E4%BB%86%E8%A3%85.jpg/450px-1096%E5%A5%B3%E4%BB%86%E8%A3%85.jpg")

@scheduler.scheduled_job("cron", month=8, day=31, hour=9, minute=0, second=0, id="Hatsune Miku's Birthday")
async def HatsuneMiku():
    await sendBirthdayNote(
        "0831-HatsuneMiku",
        url="https://ec.crypton.co.jp/img/special/vocaloid/img_MIKU_us.png")

@scheduler.scheduled_job("cron", month=9, day=8, hour=9, minute=0, second=0, id="Kupa Day")
async def KupaDay():
    with open(f"{ASSETS_ROOT}/calendar/0908-KupaDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=9, hour=9, minute=0, second=0, id="Midori Hemo's Birthday")
async def MidoriHemo():
    await sendBirthdayNote(
        "0909-MidoriHemo",
        url="http://ochifuru-anime.com/images/chara/005/p_002.png")

@scheduler.scheduled_job("cron", month=9, day=9, hour=9, minute=9, second=9, id="Cirno Day")
async def CirnoDay():
    with open(f"{ASSETS_ROOT}/calendar/0909-CirnoDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(desc)

@scheduler.scheduled_job("cron", month=9, day=14, hour=9, minute=0, second=0, id="Koshigaya Komari's Birthday")
async def KoshigayaKomari():
    await sendBirthdayNote(
        "0914-KoshigayaKomari",
        url="https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/komari/ph_front_01.png")

@scheduler.scheduled_job("cron", month=9, day=15, hour=9, minute=0, second=0, id="Komichi Aya's Birthday")
async def KomichiAya():
    await sendBirthdayNote(
        "0915-KomichiAya",
        url="http://kinmosa.com/assets/character/c/3.png")

@scheduler.scheduled_job("cron", month=9, day=19, hour=9, minute=0, second=0, id="Ujimatsu Chiya's Birthday")
async def UjimatsuChiya():
    await sendBirthdayNote(
        "0919-UjimatsuChiya",
        url="https://gochiusa.com/core_sys/images/main/cont/chara/chiya_body.png")

@scheduler.scheduled_job("cron", month=9, day=26, hour=9, minute=0, second=0, id="Doma Umaru's Birthday")
async def DomaUmaru():
    await sendBirthdayNote(
        "0926-DomaUmaru",
        url="https://umaru-ani.me/img/character/chara1_stand.png")

@scheduler.scheduled_job("cron", month=9, day=28, hour=9, minute=0, second=0, id="Yoshida Yuuko's Biethday")
async def YoshidaYuuko():
    await sendBirthdayNote(
        "0928-YoshidaYuuko",
        url="https://www.tbs.co.jp/anime/machikado/1st/character/img/chara_img_01.png")

@scheduler.scheduled_job("cron", month=9, day=30, hour=9, minute=0, second=0, id="Yuuki Asuna's Birthday")
async def YuukiAsune():
    await sendBirthdayNote(
        "0930-YuukiAsuna",
        url="https://www.swordart-online.net/aincrad/assets/img/chara/big/02_asuna.png")

@scheduler.scheduled_job("cron", month=10, day=8, hour=9, minute=0, second=0, id="Suzumiya Haruhi's Birthday")
async def SuzumiyaHaruhi():
    await sendBirthdayNote(
        "1008-SuzumiyaHaruhi",
        url="https://img.moegirl.org.cn/common/f/fd/Haruhi_Suzumiya_.jpg")

@scheduler.scheduled_job("cron", month=10, day=10, hour=9, minute=0, second=0, id="Moe Day")
async def MoeDay():
    with open(f"{ASSETS_ROOT}/calendar/1010-MoeDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=10, day=11, hour=9, minute=0, second=0, id="Loli Day")
async def LoliDay():
    with open(f"{ASSETS_ROOT}/calendar/1011-LoliDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=10, day=24, hour=9, minute=0, second=0, id="1024 Day")
async def ProgrammerDay():
    with open(f"{ASSETS_ROOT}/calendar/1024-1024Day.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=11, day=2, hour=9, minute=0, second=0, id="Tights Day")
async def TightsDay():
    with open(f"{ASSETS_ROOT}/calendar/1102-TightsDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=11, day=4, hour=9, minute=0, second=0, id="Good Butt")
async def GoodButt():
    with open(f"{ASSETS_ROOT}/calendar/1104-GoodButtDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=11, day=7, hour=9, minute=0, second=0, id="Good Belly")
async def GoodBelly():
    with open(f"{ASSETS_ROOT}/calendar/1107-GoodBellyDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=11, day=8, hour=9, minute=0, second=0, id="Good Oppai Day")
async def GoodOppai():
    with open(f"{ASSETS_ROOT}/calendar/1108-GoodOppaiDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=11, day=11, hour=9, minute=0, second=0, id="Tobiichi Origami's Birthday")
async def TobiichiOrigami():
    await sendBirthdayNote(
        "1111-TobiichiOrigami",
        url="https://date-a-live-anime.com/1st-2nd/common/images/2nd/character/character_origami.png")

@scheduler.scheduled_job("cron", month=11, day=18, hour=9, minute=0, second=0, id="Nagato Yuki's Birthday")
async def NagatoYuki():
    await sendBirthdayNote(
        "1118-NagatoYuki",
        url="https://img.moegirl.org.cn/common/thumb/4/4b/Nagato_Yuki2.jpg/420px-Nagato_Yuki2.jpg")

@scheduler.scheduled_job("cron", month=11, day=27, hour=9, minute=0, second=0, id="Hirasawa Yui's Birthday")
async def HirasawaYui():
    await sendBirthdayNote(
        "1127-HirasawaYui",
        url="https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo01_1.gif")

@scheduler.scheduled_job("cron", month=11, day=29, hour=9, minute=0, second=0, id="Good Meat Day")
async def GoodMeat():
    with open(f"{ASSETS_ROOT}/calendar/1129-GoodMeatDay.txt", "r") as f:
        desc = f.read()
    await sendNotice(MessageChain([MessageSegment.plain(desc)]))

@scheduler.scheduled_job("cron", month=12, day=3, hour=9, minute=0, second=0, id="Miyauchi Renge's Birthday")
async def MiyauchiRenge():
    await sendBirthdayNote(
        "1203-MiyauchiRenge",
        url="https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/renge/ph_front_01.png")

@scheduler.scheduled_job("cron", month=12, day=4, hour=9, minute=0, second=0, id="Kafuu Chino's Birthday")
async def KafuuChino():
    await sendBirthdayNote(
        "1204-KafuuChino",
        url="https://gochiusa.com/core_sys/images/main/cont/chara/chino_body.png")

@scheduler.scheduled_job("cron", month=12, day=23, hour=9, minute=0, second=0, id="Hoshikawa Mafuyu's Birthday")
async def HoshikawaMafuyu():
    await sendBirthdayNote(
        "1223-HoshikawaMafuyu",
        url="https://blend-s.jp/assets/img/character/chara_03/chara03_1.png")

@scheduler.scheduled_job("cron", month=12, day=25, hour=9, minute=0, second=0, id="Itou Makoto Dead")
async def ItouMakotoDead():
    await sendBirthdayNote(
        "1225-ItouMakotoDead",
        url="https://bkimg.cdn.bcebos.com/pic/adaf2edda3cc7cd98d10aacc8c4b363fb80e7bec3bd9?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U5Mg==,g_7,xp_5,yp_5")

@scheduler.scheduled_job("cron", month=12, day=31, hour=9, minute=0, second=0, id="Hanakoizumi Anne's Birthday")
async def HanakoizumiAnne():
    await sendBirthdayNote(
        "1231-HanakoizumiAnne",
        url="https://anne-happy.com/wp-content/uploads/2016/02/ch1-1-1.png")
