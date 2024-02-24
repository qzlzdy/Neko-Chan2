from nonebot import require

require("nonebot_plugin_apscheduler")

import base64
import time
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.mirai2.message import MessageChain
from nonebot.adapters.mirai2.message import MessageSegment
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

async def sendCalendarNote(date, character, url=None):
    with open(f"{ASSETS_ROOT}/calendar/{date}-{character}.txt", "r") as f:
        desc = f.read()
    if url is None:
        await sendNotice(MessageChain([MessageSegment.plain(desc)]))
    else:
        await sendNotice(MessageChain([
            MessageSegment.plain(desc),
            MessageSegment.image(url=url)
        ]))

calendars = {
"0101": [["SatonakaChie", "https://img.moegirl.org.cn/common/thumb/f/ff/55319988_p0.jpg/420px-55319988_p0.jpg"]],
"0104": [["MinagiHiyori", "https://slowlooptv.com/images/chara/p_001.png"]],
"0107": [["HimeragiYukina", "http://www.strike-the-blood.com/first/imgs/character/chara02.jpg"]],
"0111": [["MiniwaTsumiki", "https://www.tbs.co.jp/anime/ackc/character/images/chara_img01.jpg"]],
"0115": [["AkiyamaMio", "https://img.moegirl.org.cn/common/thumb/2/2e/The_Bowl.jpg/420px-The_Bowl.jpg"]],
"0123": [["TakimotoHifumi", "http://newgame-anime.com/assets/character/c4.png"]],
"0201": [["YukimiKoume", "https://www.tbs.co.jp/anime/urara/chara/img/koume_left.png"]],
"0202": [
    ["SuzukazeAoba", "http://newgame-anime.com/assets/character/c1.png"],
    ["TsutsukakushiTsukiko", "http://www.henneko.jp/character/img/p_tsukiko.png"]
],
"0203": [["TohsakaRin", "https://www.nbcuni.co.jp/rondorobe/anime/staynight/character/img/chphoto_003.gif"]],
"0205": [["KasuganoSora", "https://img.moegirl.org.cn/common/thumb/7/75/Kasugano_sora_game_CG_ring.jpg/420px-Kasugano_sora_game_CG_ring.jpg"]],
"0207": [["FutanariDay"]],
"0208": [["KneeHighDay"]],
"0210": [["Louise", "https://zh.moegirl.org.cn/File:Louise_francis.jpg"]],
"0214": [["TedezaRize", "https://gochiusa.com/core_sys/images/main/cont/chara/rize_body.png"]],
"0217": [["Shiina", "https://www.tbs.co.jp/anime/koufuku_g/chara/images/chara_img03.jpg"]],
"0221": [["GotouHitori", "https://img.moegirl.org.cn/common/thumb/c/c7/Gotou_hitori_goods.jpg/375px-Gotou_hitori_goods.jpg"]],
"0223": [["KumegawaBotan", "https://anne-happy.com/wp-content/uploads/2016/02/ch3-2.png"]],
"0302": [["MatouSakura", "https://www.nbcuni.co.jp/rondorobe/anime/staynight/character/img/chphoto_005.gif"]],
"0303": [
    ["KoizukaKoyume", "http://comic-girls.com/character/img/chara2.png"],
    ["MomokiRun", "https://www.a-ch.jp/character/img/ch02.jpg"],
    ["NakamachiKana", "https://www.tv-tokyo.co.jp/contents/kanamemo/chara/images/chara_01.jpg"]
],
"0304": [["KagamiharaNadeshiko", "https://yurucamp.jp/first/images/chara_list1.png"]],
"0310": [["SatenRuiko", "https://toaru-project.com/railgun_t/core_sys/images/main/cont_chara/11_body.png"]],
"0315": [["TatsumiKon", "https://www.tbs.co.jp/anime/urara/chara/img/kon_left.png"]],
"0320": [["HimekawaYoshino", "https://date-a-live-anime.com/1st-2nd/common/images/2nd/character/character_yoshino.png"]],
"0403": [["KurawashiRiko", "https://www.love-lab.tv/chara/img/riko00.jpg?1680924886863"]],
"0404": [
    ["AzukiAzusa", "http://www.henneko.jp/character/img/p_azusa.png"],
    ["SakuraIno", "http://ochifuru-anime.com/images/chara/001/p_002.png"],
    ["SakuranomiyaMaika", "https://blend-s.jp/assets/img/character/chara_01/02.png"]
],
"0405": [
    ["AliceCartelet", "http://kinmosa.com/series/images/s2character/c2.png"],
    ["TakeyaYuki", "https://gakkougurashi.com/core_sys/images/main/cont/chara/ch01-1.png"]
],
"0406": [
    ["HigaKanata", "https://www.harukana-receive.jp/assets/character/1b.png"],
    ["IchinoseHana", "https://slow-start.com/shared/images/top/chara_d_hana_img.png"]
],
"0408": [["KousakaKirino", "https://www.oreimo-anime.com/1st/chara/img/chara01.jpg"]],
"0410": [["HotoKokoa", "https://gochiusa.com/core_sys/images/main/cont/chara/cocoa_body.png"], ["ShibasakiRoka", "http://www.d-fragments.net/character/images/shibasaki_roka.jpg"]],
"0411": [["AmanoSaki", "https://www.tv-tokyo.co.jp/contents/kanamemo/chara/images/chara_02.jpg"]],
"0412": [["SawatariUki", "http://animayell.com/core_sys/images/main/cont/chara/main_uki.png"]],
"0420": [["GokouRuri", "https://www.oreimo-anime.com/1st/chara/img/chara04.jpg"]],
"0421": [["KitaIkuyo", "https://bocchi.rocks/assets/img/page/character/ikuyo/main.png"]],
"0427": [["MisakiMei", "https://www.pa-works.jp/wp-content/uploads/2012/04/08_another-727x1024.jpg"]],
"0501": [["IchiiYui", "https://www.yuyushiki.net/core_sys/images/main/cont/chara/chara2_cos1.jpg"]],
"0502": [
    ["MisakaMikoto", "https://toaru-project.com/railgun/core_sys/images/contents/00000004/base/001.jpg?1615808050"],
    ["AragakiAyase", "https://www.oreimo-anime.com/1st/chara/img/chara06.jpg"],
    ["HanaNFountainstand", "https://hanayamata.com/assets/images/profile/chara02_off.png"],
    ["OdagiriFutaba", "https://sansyasanyou.com/core_sys/images/contents/00000003/base/sn_001.png?1552483627"]
],
"0504": [["KatsukiTsubasa", "http://comic-girls.com/character/img/chara4.png"]],
"0510": [["MaidDay"]],
"0515": [["StockingDay"]],
"0523": [["KissDay"]],
"0524": [["NishiYuuko", "https://www.a-ch.jp/character/img/ch03.jpg"]],
"0528": [
    ["IchijyouHotaru", "https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/hotaru/ph_front_01.png"],
    ["IzumiKonata", "https://img.moegirl.org.cn/common/thumb/0/0e/Izumi_Konata_Hinnyuu.jpg/450px-Izumi_Konata_Hinnyuu.jpg"]
],
"0529": [["IjichiNijika", "https://bocchi.rocks/assets/img/page/character/nijika/main.png"]],
"0601": [["SasameYaya", "https://hanayamata.com/assets/images/profile/chara03_off.png"]],
"0603": [["SengokuNadeko", "https://www.monogatari-series.com/bakemonogatari/chara/images/i04.jpg"]],
"0609": [["AmanoMiu", "https://blend-s.jp/assets/img/character/chara_04/chara04_1.png"]],
"0610": [["TokisakiKurumi", "https://date-a-live4th-anime.com/common/images/character/character06.png"]],
"0612": [["TakanashiRikka", "https://www.anime-chu-2.com/tv/img/character/rikka/01.png"]],
"0613": [["KonohataMira", "http://koiastv.com/images/chara/p_001.png"]],
"0620": [["TokuraEiko", "https://slow-start.com/shared/images/top/chara_d_eiko_img.png"]],
"0622": [["MachikoRyou", "https://www.tbs.co.jp/anime/koufuku_g/chara/images/chara_img01.jpg"]],
"0624": [["SonodaYuu", "https://www.tbs.co.jp/anime/sakura/chara/images/chara_img02.jpg"]],
"0628": [["IkiHiyori", "https://noragami-anime.net/images_sub/chara_detail2.png"]],
"0630": [["YoshinagaKoi", "https://slowlooptv.com/images/chara/p_003.png"]],
"0702": [["KotobukiTsumugi", "https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo04.gif"]],
"0704": [["HatoyaKohane", "http://animayell.com/core_sys/images/main/cont/chara/details_kohane_school.png"]],
"0707": [["SenjyougaharaHitagi", "https://www.monogatari-series.com/bakemonogatari/chara/images/i01.jpg"]],
"0709": [["HibarigaokaRuri", "https://anne-happy.com/wp-content/uploads/2016/02/ch2-1-1.png"]],
"0710": [["KanzakiHideri", "https://blend-s.jp/assets/img/character/chara_05/chara05_1.png"]],
"0715": [["KirimaSharo", "https://gochiusa.com/core_sys/images/main/cont/chara/syaro_body.png"]],
"0717": [["KurokawaMao", "https://wakabagirl.com/core_sys/images/contents/00000010/base/001.jpg?1555054911"]],
"0801": [["OppaiDay"]],
"0802": [["PantsDay"]],
"0803": [["AmatumeAkira", "https://img.moegirl.org.cn/common/6/6c/Akira_and_cat.jpeg"], ["ItsukaKotori", "https://date-a-live-anime.com/1st-2nd/common/images/2nd/character/character_kotori.png"], ["MigiwaKazuha", "https://img.moegirl.org.cn/common/5/54/%E6%B8%9A%E4%B8%80%E5%8F%B6%E5%B0%8F%E6%8F%90%E7%90%B4.jpeg"]],
"0811": [["NishikawaYoko", "http://sansyasanyou.com/core_sys/images/contents/00000002/base/sn_001.png?1552483627"]],
"0812": [["HinataKaho", "https://blend-s.jp/assets/img/character/chara_02/chara02_1.png"]],
"0820": [["InokumaYouko", "http://www.kinmosa.com/series/images/s2character/c4.png"]],
"0821": [["TainakaRitsu", "https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo03.gif"]],
"0823": [["MakiNatsuo", "https://www.love-lab.tv/chara/img/maki00.jpg"]],
"0825": [["TakayamaHaruka", "https://www.tbs.co.jp/anime/sakura/chara/images/chara_img01.jpg"]],
"0828": [
    ["AsahinaMikuru", "https://img.moegirl.org.cn/common/thumb/3/39/1096%E5%A5%B3%E4%BB%86%E8%A3%85.jpg/450px-1096%E5%A5%B3%E4%BB%86%E8%A3%85.jpg"],
    ["HondaTamaki", "http://www.dokidokivisual.com/magic_of_stella/img/banner/banner_kari_anim_l.jpg"]
],
"0831": [["HatsuneMiku", "https://ec.crypton.co.jp/img/special/vocaloid/img_MIKU_us.png"]],
"0908": [["KupaDay"]],
"0909": [
    ["CirnoDay"],
    ["MidoriHemo", "http://ochifuru-anime.com/images/chara/005/p_002.png"]
],
"0914": [["KoshigayaKomari", "https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/komari/ph_front_01.png"]],
"0915": [["KomichiAya", "http://kinmosa.com/assets/character/c/3.png"]],
"0919": [["UjimatsuChiya", "https://gochiusa.com/core_sys/images/main/cont/chara/chiya_body.png"]],
"0923": [["KanzakiHolmesAria", "http://ariaaa.tv/character/images/img_chara-2.png"]],
"0926": [["DomaUmaru", "https://umaru-ani.me/img/character/chara1_stand.png"]],
"0928": [["YoshidaYuuko", "https://www.tbs.co.jp/anime/machikado/1st/character/img/chara_img_01.png"]],
"0930": [["YuukiAsuna", "https://www.swordart-online.net/aincrad/assets/img/chara/big/02_asuna.png"]],
"1008": [["SuzumiyaHaruhi", "https://img.moegirl.org.cn/common/f/fd/Haruhi_Suzumiya_.jpg"]],
"1010": [["MoeDay"]],
"1011": [["LoliDay"]],
"1024": [["ProgrammerDay"]],
"1025": [["MamiyaAkari", "http://ariaaa.tv/character/images/img_chara-1.png"]],
"1102": [["TightsDay"]],
"1104": [["GoodButt"]],
"1107": [["GoodBelly"]],
"1108": [["GoodOppai"]],
"1111": [["TobiichiOrigami", "https://date-a-live-anime.com/1st-2nd/common/images/2nd/character/character_origami.png"]],
"1118": [["NagatoYuki", "https://img.moegirl.org.cn/common/thumb/4/4b/Nagato_Yuki2.jpg/420px-Nagato_Yuki2.jpg"]],
"1127": [["HirasawaYui", "https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo01_1.gif"]],
"1129": [["GoodMeat"]],
"1203": [["MiyauchiRenge", "https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/renge/ph_front_01.png"]],
"1204": [["KafuuChino", "https://gochiusa.com/core_sys/images/main/cont/chara/chino_body.png"]],
"1223": [["HoshikawaMafuyu", "https://blend-s.jp/assets/img/character/chara_03/chara03_1.png"]],
"1225": [["ItouMakotoDead", "https://bkimg.cdn.bcebos.com/pic/adaf2edda3cc7cd98d10aacc8c4b363fb80e7bec3bd9?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U5Mg==,g_7,xp_5,yp_5"]],
"1226": [["Takao", "http://www.d-fragments.net/character/images/takao_bucho.jpg"]],
"1231": [["HanakoizumiAnne", "https://anne-happy.com/wp-content/uploads/2016/02/ch1-1-1.png"]],
}

@scheduler.scheduled_job("cron", hour=9, minute=0, second=0)
async def CalendarNote():
    now = time.localtime(time.time())
    today = time.strftime("%m%d", now)
    if today in calendars.keys():
        for note in calendars[today]:
            if len(note) == 1:
                await sendCalendarNote(today, note[0])
            else:
                await sendCalendarNote(today, note[0], note[1])

@scheduler.scheduled_job("cron", month=7, day=21, hour=9, minute=0, second=0)
async def OnanieDay():
    with open(f"{ASSETS_ROOT}/calendar/0721-OnanieDay.txt", "r") as f:
        desc = f.read()
    infile = open(f"{ASSETS_ROOT}/0721.jpg", "rb").read()
    buf = base64.b64encode(infile)
    await sendNotice(MessageChain([
        MessageSegment.plain(desc),
        MessageSegment.image(base64=str(buf, "utf-8"))
    ]))
