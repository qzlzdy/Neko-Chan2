from nonebot import require

require("nonebot_plugin_apscheduler")

import base64
import time
from nonebot import on_command
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11.message import MessageSegment
from ..utils import ASSETS_ROOT
from ..utils import sendNotice

cld = on_command("节日提醒")

async def sendCalendarNote(date, character, url=None):
    basename = f"{ASSETS_ROOT}/calendar/{date}-{character}"
    with open(f"{basename}.txt", "r") as f:
        desc = f.read()
    if url is None:
        await sendNotice(Message([MessageSegment.text(desc)]))
    elif url == "local":
        with open(f"{basename}.png", "rb") as infile:
            buf = base64.b64encode(infile)
        await sendNotice(Message([
            MessageSegment.text(desc),
            MessageSegment.image("base64://" + str(buf, "utf-8"))
        ]))
    else:
        try:
            await sendNotice(Message([
                MessageSegment.text(desc),
                MessageSegment.image(url)
            ]))
        except:
            print("get image failed")
            await sendNotice(Message([MessageSegment.text(desc)]))

calendars = {
"0101": [["Compilation"]],
"0103": [["Homura", "https://senran.tv/images/character/p6.jpg"]],
"0104": [["MinagiHiyori", "https://img.moegirl.org.cn/common/thumb/5/5f/Minagi_Hiyori_Chara.png/124px-Minagi_Hiyori_Chara.png"]],
"0107": [["HimeragiYukina", "http://www.strike-the-blood.com/first/imgs/character/chara02.jpg"]],
"0108": [["ShibasakiKazuha", "https://img.moegirl.org.cn/common/thumb/9/91/Disc_05.jpg/420px-Disc_05.jpg"]],
"0110": [["WienMargarete", "https://www.lovelive-anime.jp/yuigaoka/member/img/c10b.png"]],
"0111": [["MiniwaTsumiki", "https://www.tbs.co.jp/anime/ackc/character/images/chara_img01.jpg"]],
"0113": [["IrisuMakina", "https://grisaia-anime.com/kajitsu/core_sys/images/contents/00000006/base/001.png"]],
"0114": [["ShirokaneGinka", "https://www.geneitaiyo.com/character/img/main/ginka.png"]],
"0115": [["AkiyamaMio", "https://img.moegirl.org.cn/common/thumb/2/2e/The_Bowl.jpg/420px-The_Bowl.jpg"]],
"0116": [["FelixArgyle", "http://re-zero-anime.jp/tv/assets/character/c/11c.webp"]],
"0117": [
    ["Kay", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/kei_03_03-1.png"],
    ["KoizumiHanayo", "https://www.lovelive-anime.jp/otonokizaka/img/member/member08_01.png"],
    ["MochizukiMomiji", "https://img.moegirl.org.cn/common/thumb/6/62/%E6%9C%9B%E6%9C%88%E7%BA%A2%E5%8F%B6C10.png/600px-%E6%9C%9B%E6%9C%88%E7%BA%A2%E5%8F%B6C10.png"]
],
"0123": [["Compilation"]],
"0124": [["Echidna", "http://re-zero-anime.jp/tv/assets/character/c/25.png"]],
"0127": [["NaruseMio", "https://img.moegirl.org.cn/common/thumb/f/f0/%E6%88%90%E6%BF%91%E6%BE%AA.jpg/420px-%E6%88%90%E6%BF%91%E6%BE%AA.jpg"]],
"0128": [["IrizakiMei", "https://www.hai-furi.com/assets_mv/img/chara/01_kankyo/04_irizaki/img_face03.jpg"]],
"0131": [
    ["KasumigaokaUtaha", "https://img.moegirl.org.cn/common/3/37/Utaha.png"],
    ["Katyusha", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/kacyusya_03.png"]
],
"0201": [
    ["ShiinaMayuri", "http://steinsgate.tv/character/images/img_mayuri.jpg"],
    ["YukimiKoume", "https://www.tbs.co.jp/anime/urara/chara/img/koume_left.png"]
],
"0202": [
    ["Ram", "http://re-zero-anime.jp/tv/assets/character/c/5b.webp"],
    ["Rem", "http://re-zero-anime.jp/tv/assets/character/c/4b.webp"],
    ["SuzukazeAoba", "https://img.moegirl.org.cn/common/9/95/%E5%87%89%E9%A3%8E%E9%9D%92%E5%8F%B6%E4%BA%BA%E8%AE%BE%E5%9B%BE.png"],
    ["TsutsukakushiTsukiko", "http://www.henneko.jp/character/img/p_tsukiko.png"]
],
"0203": [
    ["OnigawaraRin", "local"],
    ["TohsakaRin", "https://www.nbcuni.co.jp/rondorobe/anime/staynight/character/img/chphoto_003.gif"]
],
"0205": [
    ["EmmaVerde", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c09a.png"],
    ["KasuganoSora", "https://img.moegirl.org.cn/common/thumb/7/75/Kasugano_sora_game_CG_ring.jpg/420px-Kasugano_sora_game_CG_ring.jpg"],
    ["TamakiAko", "https://netogenoyome.com/core_sys/images/main/cont/chara/ch_img2-1.png"]
],
"0206": [["MachiroRima", "https://img.moegirl.org.cn/common/thumb/2/25/Mashiro_Rima.jpg/420px-Mashiro_Rima.jpg"]],
"0210": [
    ["Louise", "https://img.moegirl.org.cn/common/a/a3/Louise_francis.jpg"],
    ["MatsuuraKanan", "https://www.lovelive-anime.jp/uranohoshi/img/member/03.png"],
    ["Yomi", "https://senran.tv/images/character/p7.jpg"]
],
"0214": [
    ["ShimotsukiMika", "https://psycho-pass.com/assets/img/character/chara06_d.png"],
    ["TedezaRize", "https://gochiusa.com/core_sys/images/main/cont/chara/rize_body.png"]
],
"0215": [["Compilation"]],
"0217": [
    ["KatakuraKoto", "https://img.moegirl.org.cn/common/thumb/c/cf/%E7%89%87%E4%BB%93%E4%BA%AC5.jpg/420px-%E7%89%87%E4%BB%93%E4%BA%AC5.jpg"],
    ["Shiina", "https://www.tbs.co.jp/anime/koufuku_g/chara/images/chara_img03.jpg"]
],
"0218": [["Hibari", "https://senran.tv/images/character/p5.jpg"]],
"0219": [["YukimuraAoi", "https://yamanosusume-ns.com/core_sys/images/main/cont/chara/aoi_stand.png"]],
"0221": [["GotouHitori", "https://img.moegirl.org.cn/common/thumb/c/c7/Gotou_hitori_goods.jpg/375px-Gotou_hitori_goods.jpg"]],
"0222": [["KowataMakoto", "https://www.vap.co.jp/flyingwitch/images/character/makoto_body.png"]],
"0223": [["KumegawaBotan", "https://anne-happy.com/wp-content/uploads/2016/02/ch3-2.png"]],
"0224": [["AzumaTokaku", "https://img.moegirl.org.cn/common/thumb/e/eb/42656999_p1.jpg/420px-42656999_p1.jpg"]],
"0225": [["ArashiChisato", "https://www.lovelive-anime.jp/yuigaoka/member/img/c03a.png"]],
"0229": [["HoshimiyaKeito", "https://www.sekaiseifuku-zzz.com/img/chara/ch01a.png"]],
"0301": [["UeharaAyumu", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c02a.png"]],
"0302": [["MatouSakura", "https://www.nbcuni.co.jp/rondorobe/anime/staynight/character/img/chphoto_005.gif"]],
"0303": [
    ["IzumiReina", "https://phantom-world.com/img/character/reina.png"],
    ["KatsuraHinagiku", "http://hayatenogotoku.com/images/chara/hina.jpg"],
    ["KoizukaKoyume", "http://comic-girls.com/character/img/chara2.png"],
    ["MomokiRun", "https://www.a-ch.jp/character/img/ch02.jpg"],
    ["NakamachiKana", "https://www.tv-tokyo.co.jp/contents/kanamemo/chara/images/chara_01.jpg"],
    ["SetoSun", "https://www.tv-tokyo.co.jp/contents/setohana/images/chara_san.jpg"],
    ["SuouAmane", "https://grisaia-anime.com/kajitsu/core_sys/images/contents/00000004/base/001.png"]
],
"0305": [["Compilation"]],
"0304": [
    ["KagamiharaNadeshiko", "https://yurucamp.jp/first/images/chara_list1.png"],
    ["KunikidaHanamaru", "https://www.lovelive-anime.jp/uranohoshi/img/member/07.png"]
],
"0306": [["ItsumiErika", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/erika_03.png"]],
"0308": [["Compilation"]],
"0310": [
    ["AnastasiaHoshin", "https://img.moegirl.org.cn/common/4/4f/%E3%82%A2%E3%83%8A%E3%82%B9%E3%82%BF%E3%82%B7%E3%82%A2%E3%83%9B%E3%83%BC%E3%82%B7%E3%83%B3.png"],
    ["SatenRuiko", "https://toaru-project.com/railgun_t/core_sys/images/main/cont_chara/11_body.png"]
],
"0312": [["KaminashiNozomi", "https://img.moegirl.org.cn/common/thumb/0/03/Keijo_nozomi.jpg/300px-Keijo_nozomi.jpg"]],
"0314": [["Elusia", "https://web.archive.org/web/20240213052037im_/https://www.tv-tokyo.co.jp/contents/kaminomi/images/chara_02.png"]],
"0315": [
    ["MotobaKirie", "https://umaru-ani.me/img/character/chara4_stand.png"],
    ["SonodaUmi", "https://www.lovelive-anime.jp/otonokizaka/img/member/member04_01.png"],
    ["TakamachiNanoha", "https://img.moegirl.org.cn/common/thumb/3/3d/Nanoha.jpg/420px-Nanoha.jpg"],
    ["TatsumiKon", "https://www.tbs.co.jp/anime/urara/chara/img/kon_left.png"]
],
"0319": [["ShirahaRaphielAinsworth", "https://img.moegirl.org.cn/common/f/f0/Gabriel_Dropout_Vol4.jpg"]],
"0320": [
    ["HimekawaYoshino", "https://img.moegirl.org.cn/common/thumb/8/8f/Yoshino2.JPG/420px-Yoshino2.JPG"],
    ["SawamuraSpencerEriri", "https://img.moegirl.org.cn/common/3/36/Eriri_Spencer_Sawamura.png"]
],
"0324": [["NarukaraFukune", "https://img.moegirl.org.cn/common/thumb/c/ca/Fukune_Narukara-2.jpg/420px-Fukune_Narukara-2.jpg"]],
"0325": [
    ["LiMeiling", "local"],
    ["ShibaMiyuki", "https://mahouka.jp/1st/img/character/c_img_2_l.png"]
],
"0326": [["HanasakaWarabi", "local"]],
"0328": [["ToshinouKyouko", "https://yuruyuri.com/1st/character/img/detail_kyoko.jpg"]],
"0331": [["SonouMomoka", "https://img.moegirl.org.cn/common/thumb/8/8f/%E8%8B%91%E7%94%9F%E7%99%BE%E8%8A%B16.jpeg/420px-%E8%8B%91%E7%94%9F%E7%99%BE%E8%8A%B16.jpeg"]],
"0401": [["Compilation"]],
"0402": [
    ["Chiya", "https://img.moegirl.org.cn/common/thumb/3/3e/%E5%8D%83%E7%9F%A2_I.jpg/420px-%E5%8D%83%E7%9F%A2_I.jpg"],
    ["FujikawaKayo", "https://img.moegirl.org.cn/common/thumb/1/16/Charaillust_chara_16030000.png/420px-Charaillust_chara_16030000.png"]
],
"0403": [
    ["AkihaRumiho", "http://steinsgate.tv/character/images/img_feiris.jpg"],
    ["KurawashiRiko", "https://www.love-lab.tv/chara/img/riko00.jpg?1680924886863"],
    ["OusakaShizuku", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c04a.png"]
],
"0404": [
    ["AzukiAzusa", "http://www.henneko.jp/character/img/p_azusa.png"],
    ["CruschKarsten", "http://re-zero-anime.jp/tv/assets/character/c/10b.webp"],
    ["SakuraIno", "http://ochifuru-anime.com/images/chara/001/p_002.png"],
    ["SakuranomiyaMaika", "https://blend-s.jp/assets/img/character/chara_01/02.png"]
],
"0405": [
    ["AliceCartelet", "https://img.moegirl.org.cn/common/thumb/e/e2/Alice-kyara.png/600px-Alice-kyara.png"],
    ["HagimuraSuzu", "https://king-cr.jp/special/seitokai/images/s-council/suzu.gif"],
    ["TakeyaYuki", "https://gakkougurashi.com/core_sys/images/main/cont/chara/ch01-1.png"]
],
"0406": [
    ["ChidorigafuchiAine", "https://img.moegirl.org.cn/common/d/d4/Chidorigafuchi_Aine_Side.png"],
    ["HigaKanata", "https://www.harukana-receive.jp/assets/character/1b.png"],
    ["IchinoseHana", "https://slow-start.com/shared/images/top/chara_d_hana_img.png"],
    ["LalatinaFordDustiness", "http://konosuba.com/3rd/character/img/darkness.png"]
],
"0407": [["SakuragaokaNanami", "https://img.moegirl.org.cn/common/thumb/2/25/%E6%A8%B1%E4%B8%98%E4%B8%83%E6%B5%B76.jpeg/420px-%E6%A8%B1%E4%B8%98%E4%B8%83%E6%B5%B76.jpeg"]],
"0408": [["KousakaKirino", "https://www.oreimo-anime.com/1st/chara/img/chara01.jpg"]],
"0410": [
    ["HotoKokoa", "https://gochiusa.com/core_sys/images/main/cont/chara/cocoa_body.png"],
    ["SakurakoujiKinako", "https://www.lovelive-anime.jp/yuigaoka/member/img/c06b.png"],
    ["ShibasakiRoka", "http://www.d-fragments.net/character/images/shibasaki_roka.jpg"]
],
"0411": [["AmanoSaki", "https://www.tv-tokyo.co.jp/contents/kanamemo/chara/images/chara_02.jpg"]],
"0412": [["SawatariUki", "http://animayell.com/core_sys/images/main/cont/chara/main_uki.png"]],
"0417": [["WatanabeYou", "https://www.lovelive-anime.jp/uranohoshi/img/member/05.png"]],
"0419": [["NishikinoMaki", "https://www.lovelive-anime.jp/otonokizaka/img/member/member06_01.png"]],
"0420": [
    ["GokouRuri", "https://www.oreimo-anime.com/1st/chara/img/chara04.jpg"],
    ["KugayamaYae", "https://img.moegirl.org.cn/common/thumb/6/61/Kugayama_Yae.png/420px-Kugayama_Yae.png"],
    ["Marie", "https://girls-und-panzer-finale.jp/iaY7mRf2zJ/wp-content/uploads/2020/02/mary-daikarui-1.png"],
    ["TenmaGabrielWhite", "https://img.moegirl.org.cn/common/3/38/Gabriel_Dropout_Vol1.jpg"]
],
"0421": [["KitaIkuyo", "https://bocchi.rocks/assets/img/page/character/ikuyo/main.png"]],
"0422": [["FunamiYui", "https://yuruyuri.com/1st/character/img/detail_yui.jpg"]],
"0424": [["Haqua", "https://www.tv-tokyo.co.jp/anime/kaminomi3/images/chara/img_03.png"]],
"0425": [["MinaseKoito", "https://phantom-world.com/img/character/koito.png"]],
"0427": [["MisakiMei", "https://img.moegirl.org.cn/common/thumb/5/51/1046253.jpg/420px-1046253.jpg"]],
"0429": [["ElsaGranhiert", "http://re-zero-anime.jp/tv/assets/character/c/17.webp"]],
"0430": [["SakuragiHinako", "https://hinakonote.jp/assets/character/c1.jpg"]],
"0501": [
    ["IchiiYui", "https://www.yuyushiki.net/core_sys/images/main/cont/chara/chara2_cos1.jpg"],
    ["ShibuyaKanon", "https://www.lovelive-anime.jp/yuigaoka/member/img/c01b.png"]
],
"0502": [
    ["MisakaMikoto", "https://toaru-project.com/railgun/core_sys/images/contents/00000004/base/001.jpg?1615808050"],
    ["AragakiAyase", "https://www.oreimo-anime.com/1st/chara/img/chara06.jpg"],
    ["HanaNFountainstand", "https://hanayamata.com/assets/images/profile/chara02_off.png"],
    ["OdagiriFutaba", "https://img.moegirl.org.cn/common/thumb/6/6b/Odagiri_Futaba.jpg/276px-Odagiri_Futaba.jpg"]
],
"0504": [["KatsukiTsubasa", "https://img.moegirl.org.cn/common/thumb/f/fc/Katsuki_Tsubasa_.jpg/420px-Katsuki_Tsubasa_.jpg"]],
"0505": [["SakuraNene", "https://img.moegirl.org.cn/common/3/30/Sakura_Nene.jpg"]],
"0510": [["NakajimaYua", "https://hinakonote.jp/assets/character/c5.jpg"]],
"0516": [["NarumiTsubame", "https://img.moegirl.org.cn/common/thumb/d/d2/%E9%B8%A3%E6%B5%B7%E7%87%95C11.png/600px-%E9%B8%A3%E6%B5%B7%E7%87%95C11.png"]],
"0517": [
    ["AobaKazane", "https://img.moegirl.org.cn/common/thumb/1/18/Keijo_kazane.jpg/300px-Keijo_kazane.jpg"],
    ["HoshikawaSeira", "https://www.geneitaiyo.com/character/img/main/seira.png"]
],
"0519": [["KashiwazakiSena", "https://www.tbs.co.jp/anime/haganai/1st/chara/images/chara_img03.jpg"]],
"0524": [["NishiYuuko", "https://www.a-ch.jp/character/img/ch03.jpg"]],
"0525": [
    ["KaranomoriShion", "https://psycho-pass.com/assets/img/character/chara05_d.png"],
    ["YuikiYaya", "https://img.moegirl.org.cn/common/thumb/e/e0/%E7%BB%93%E6%9C%A8%E5%BC%A5%E8%80%B6.jpg/420px-%E7%BB%93%E6%9C%A8%E5%BC%A5%E8%80%B6.jpg"]
],
"0527": [["MunetaniMashiro", "https://www.hai-furi.com/assets_mv/img/chara/01_kankyo/02_munetani/img_main.png"]],
"0528": [
    ["IchijyouHotaru", "https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/hotaru/ph_front_01.png"],
    ["IzumiKonata", "https://img.moegirl.org.cn/common/thumb/0/0e/Izumi_Konata_Hinnyuu.jpg/450px-Izumi_Konata_Hinnyuu.jpg"],
    ["NasaKouko", "https://www.hai-furi.com/assets_mv/img/chara/01_kankyo/05_nosa/img_face03.jpg"]
],
"0529": [
    ["FateTestarossaHarlaown", "https://img.moegirl.org.cn/common/thumb/8/8e/Myfate.jpg/420px-Myfate.jpg"],
    ["IjichiNijika", "https://bocchi.rocks/assets/img/page/character/nijika/main.png"]
],
"0530": [["MiyashitaAi", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c06a.png"]],
"0601": [["SasameYaya", "https://hanayamata.com/assets/images/profile/chara03_off.png"]],
"0603": [["SengokuNadeko", "https://www.monogatari-series.com/bakemonogatari/chara/images/i04.jpg"]],
"0604": [["YagamiHayate", "https://www.nanoha.com/archive2/chara/images/chr_132.gif"]],
"0606": [
    ["AkiyamaYukari", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/akiyama.png"],
    ["YomokawaAyame", "https://kabaneri.com/assets/img/in/character/c_ayame.png"]
],
"0609": [
    ["AmanoMiu", "https://blend-s.jp/assets/img/character/chara_04/chara04_1.png"],
    ["ToujyouNozomi", "https://www.lovelive-anime.jp/otonokizaka/img/member/member07_01.png"]
],
"0610": [["Compilation"]],
"0612": [
    ["AmakusaShino", "https://king-cr.jp/special/seitokai/images/s-council/shino.gif"],
    ["KushiedaMinori", "https://cdn.kdkw.jp/cover_500/302112/302112002287.webp"],
    ["TakanashiRikka", "https://www.anime-chu-2.com/tv/img/character/rikka/01.png"]
],
"0613": [
    ["KonohataMira", "local"],
    ["OharaMari", "https://www.lovelive-anime.jp/uranohoshi/img/member/08.png"]
],
"0615": [
    ["AiharaEnjyu", "local"],
    ["TamabaSatori", "local"]
],
"0616": [["FujinomiyaNeko", "https://img.moegirl.org.cn/common/c/c5/%E8%97%A4%E4%B9%8B%E5%AE%AB%E5%AE%81%E5%AD%90.jpg"]],
"0617": [["WakanaShiki", "https://www.lovelive-anime.jp/yuigaoka/member/img/c08a.png"]],
"0620": [["TokuraEiko", "https://slow-start.com/shared/images/top/chara_d_eiko_img.png"]],
"0622": [
    ["MachikoRyou", "https://www.tbs.co.jp/anime/koufuku_g/chara/images/chara_img01.jpg"],
    ["TakebeSaori", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/saori.png"]
],
"0624": [
    ["HoujyouSatoko", "http://www.oyashirosama.com/web/kai/character/img/satoko-bottom.jpg"],
    ["SonodaYuu", "https://www.tbs.co.jp/anime/sakura/chara/images/chara_img02.jpg"]
],
"0625": [["TakanashiNao", "local"]],
"0628": [["IkiHiyori", "local"]],
"0629": [["AsakaKarin", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c05a.png"]],
"0630": [["YoshinagaKoi", "https://slowlooptv.com/images/chara/p_003.png"]],
"0701": [["NishizumiMaho", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/maho_03.png"]],
"0702": [["KotobukiTsumugi", "https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo04.gif"]],
"0704": [["HatoyaKohane", "http://animayell.com/core_sys/images/main/cont/chara/details_kohane_school.png"]],
"0707": [["Compilation"]],
"0709": [["HibarigaokaRuri", "https://anne-happy.com/wp-content/uploads/2016/02/ch2-1-1.png"]],
"0710": [
    ["KanzakiHideri", "https://blend-s.jp/assets/img/character/chara_05/chara05_1.png"],
    ["SonozakiMion", "http://www.oyashirosama.com/web/kai/character/img/mion-bottom.jpg"],
    ["SonozakiShion", "http://www.oyashirosama.com/web/kai/character/img/shion-bottom.jpg"]
],
"0713": [["TsushimaYoshiko", "https://www.lovelive-anime.jp/uranohoshi/img/member/06.png"]],
"0715": [["KirimaSharo", "https://gochiusa.com/core_sys/images/main/cont/chara/syaro_body.png"]],
"0717": [["Compilation"]],
"0720": [
    ["AhagonUmiko", "local"],
    ["ChloeVonEinzbern", "https://anime.prisma-illya.jp/2wei/character/img/detail_kuro.png"],
    ["Haruka", "https://senran.tv/images/character/p10.jpg"],
    ["IllyasvielVonEinzbern", "https://anime.prisma-illya.jp/1st/character/img/detail_illya_pose.png"],
    ["MisakiAkeno", "https://www.hai-furi.com/assets_mv/img/chara/01_kankyo/01_misaki/img_face01.jpg"],
    ["MiyuEdelfelt", "https://anime.prisma-illya.jp/1st/character/img/detail_miyu_pose.png"]
],
"0722": [["YazawaNiko", "https://www.lovelive-anime.jp/otonokizaka/img/member/member09_01.png"]],
"0723": [["SekiAyame", "local"]],
"0724": [
    ["AkazaAkari", "https://yuruyuri.com/1st/character/img/detail_akari.jpg"],
    ["MiyataSayaka", "local"]
],
"0725": [
    ["ChinaMoeka", "https://www.hai-furi.com/assets_mv/img/chara/06_other/01_china/img_main.png"],
    ["MakiseKurisu", "http://steinsgate.tv/character/images/img_chris.jpg"]
],
"0728": [
    ["RyuuguuRena", "http://www.oyashirosama.com/web/kai/character/img/rena-bottom.jpg"],
    ["SteinsGate"]
],
"0801": [
    ["Aqua", "local"],
    ["Hanyuu", "http://www.oyashirosama.com/web/kai/character/img/hanyu-bottom.jpg"],
    ["Nanami", "https://img.moegirl.org.cn/common/5/52/Nanami_gaworare.gif"],
    ["TakamiChika", "https://www.lovelive-anime.jp/uranohoshi/img/member/01.png"]
],
"0802": [
    ["YagamiKou", "https://img.moegirl.org.cn/common/thumb/f/f8/%E5%85%AB%E7%A5%9E%EF%BC%90%EF%BC%92.png/600px-%E5%85%AB%E7%A5%9E%EF%BC%90%EF%BC%92.png"]
],
"0803": [
    ["AmatsumeAkira", "https://img.moegirl.org.cn/common/6/6c/Akira_and_cat.jpeg"],
    ["ItsukaKotori", "local"],
    ["KousakaHonoka", "https://www.lovelive-anime.jp/otonokizaka/img/member/member01_01.png"],
    ["MigiwaKazuha", "https://img.moegirl.org.cn/common/5/54/%E6%B8%9A%E4%B8%80%E5%8F%B6%E5%B0%8F%E6%8F%90%E7%90%B4.jpeg"]
],
"0805": [["TateishiShima", "https://www.hai-furi.com/assets_mv/img/chara/01_kankyo/03_tateishi/img_face02.jpg"]],
"0807": [
    ["EbisuzawaKurumi", "https://gakkougurashi.com/core_sys/images/main/cont/chara/ch02-1.png"],
    ["OnitsukaNatsumi", "https://www.lovelive-anime.jp/yuigaoka/member/img/c09b.png"]
],
"0808": [["Compilation"]],
"0811": [
    ["AobaKokona", "https://yamanosusume-ns.com/core_sys/images/main/cont/chara/kokona_stand.png"],
    ["NishikawaYouko", "http://sansyasanyou.com/core_sys/images/contents/00000002/base/sn_001.png?1552483627"]
],
"0812": [["HinataKaho", "https://blend-s.jp/assets/img/character/chara_02/chara02_1.png"]],
"0815": [["KurumizawaSatanichiaMcDowell", "https://img.moegirl.org.cn/common/2/25/Gabriel_Dropout_Vol3.jpg"]],
"0817": [["KokonoeRin", "https://www.kojika-anime.com/img/chara_01_all.jpg"]],
"0818": [["MiyafujiYoshika", "http://w-witch.jp/s-witch/pc/chara/img/chara-miya-main.jpg"]],
"0819": [["Compilation"]],
"0820": [["InokumaYouko", "http://www.kinmosa.com/series/images/s2character/c4.png"]],
"0821": [
    ["FurudeRika", "http://www.oyashirosama.com/web/kai/character/img/rika-bottom.jpg"],
    ["TainakaRitsu", "https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo03.gif"]
],
"0823": [["MakiNatsuo", "https://www.love-lab.tv/chara/img/maki00.jpg"]],
"0825": [["TakayamaHaruka", "https://www.tbs.co.jp/anime/sakura/chara/images/chara_img01.jpg"]],
"0828": [
    ["AsahinaMikuru", "https://img.moegirl.org.cn/common/thumb/3/39/1096%E5%A5%B3%E4%BB%86%E8%A3%85.jpg/450px-1096%E5%A5%B3%E4%BB%86%E8%A3%85.jpg"],
    ["HondaTamaki", "http://www.dokidokivisual.com/magic_of_stella/img/banner/banner_kari_anim_l.jpg"]
],
"0830": [["UrushibaraRuka", "http://steinsgate.tv/character/images/img_ruka.jpg"]],
"0831": [["HatsuneMiku", "https://ec.crypton.co.jp/img/special/vocaloid/img_MIKU_us.png"]],
"0901": [["ReizeiMako", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/mako.png"]],
"0902": [
    ["MahougasawaAkane", "https://img.moegirl.org.cn/common/b/bd/Akane_gaworare.png"],
    ["ToyoguchiNon", "https://img.moegirl.org.cn/common/thumb/f/f2/Keijo_non.jpg/300px-Keijo_non.jpg"]
],
"0903": [["Compilation"]],
"0906": [["Compilation"]],
"0907": [["PriscillaBarielle", "http://re-zero-anime.jp/tv/assets/character/c/15c.webp"]],
"0908": [["Asuka", "https://senran.tv/images/character/p1.jpg"]],
"0909": [
    ["Hikage", "https://senran.tv/images/character/p8.jpg"],
    ["MidoriHemo", "http://ochifuru-anime.com/images/chara/005/p_002.png"],
    ["CirnoDay"]
],
"0910": [["SasakiChiho", "https://maousama.jp/assets/img/character/character03_main.png"]],
"0912": [["MinamiKotori", "https://www.lovelive-anime.jp/otonokizaka/img/member/member03_01.png"]],
"0913": [["InabaTsukuyo"]],
"0914": [
    ["FudaYumine", "https://img.moegirl.org.cn/common/thumb/c/cd/Charaillust_chara_16040000.png/420px-Charaillust_chara_16040000.png"],
    ["KoshigayaKomari", "https://nonnontv.com/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/character/individual/komari/ph_front_01.png"]
],
"0915": [["KomichiAya", "http://kinmosa.com/assets/character/c/3.png"]],
"0916": [["Compilation"]],
"0917": [["Darjeeling", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/drgilin_03.png"]],
"0919": [
    ["SakurauchiRiko", "https://www.lovelive-anime.jp/uranohoshi/img/member/02.png"],
    ["UjimatsuChiya", "https://gochiusa.com/core_sys/images/main/cont/chara/chiya_body.png"]
],
"0921": [["KurozawaRuby", "https://www.lovelive-anime.jp/uranohoshi/img/member/09.png"]],
"0923": [
    ["AnzaiChiyomi", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/ancyobi_03.png"],
    ["Emilia", "http://re-zero-anime.jp/tv/assets/character/c/2.webp"],
    ["KanzakiHolmesAria", "http://ariaaa.tv/character/images/img_chara-2.png"],
    ["KatouMegumi", "https://www.saenai.tv/images/character/chara_megumi_vsl.png"]
],
"0924": [["HinamoriAmu", "https://img.moegirl.org.cn/common/thumb/9/92/Hinamori_Amu.jpg/420px-Hinamori_Amu.jpg"]],
"0926": [
    ["DomaUmaru", "https://umaru-ani.me/img/character/chara1_stand.png"],
    ["TennojiNagisa", "https://www.a-ch.jp/character/img/ch04.jpg"]
],
"0927": [["AmaneSuzuha", "http://steinsgate.tv/character/images/img_suzuha.jpg"]],
"0928": [
    ["HeannaSumire", "https://www.lovelive-anime.jp/yuigaoka/member/img/c04b.png"],
    ["KunizukaYayoi", "https://psycho-pass.com/assets/img/character/chara04_d.png"],
    ["YoshidaYuuko", "https://www.tbs.co.jp/anime/machikado/1st/character/img/chara_img_01.png"]
],
"0930": [["YuukiAsuna", "https://www.swordart-online.net/aincrad/assets/img/chara/big/02_asuna.png"]],
"1001": [
    ["CrestiaBell", "https://maousama.jp/assets/img/character/character06_main.png"],
    ["HaginoChiaki", "https://hinakonote.jp/assets/character/c4.jpg"],
    ["ShimaRin", "https://yurucamp.jp/second/images/chara2_full.png"]
],
"1004": [["Compilation"]],
"1005": [["MifuneShioriko", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c11a.png"]],
"1006": [["Izetta", "https://img.moegirl.org.cn/common/thumb/f/f0/Izetta2.jpg/420px-Izetta2.jpg"]],
"1008": [["SuzumiyaHaruhi", "https://img.moegirl.org.cn/common/f/fd/Haruhi_Suzumiya_.jpg"]],
"1010": [
    ["EkodaRen", "https://anne-happy.com/wp-content/uploads/2016/02/ch5-1-1.png"],
    ["TsukinoseVignetteApril", "https://img.moegirl.org.cn/common/a/a8/%E6%9C%88%E4%B9%83%E6%BF%912.jpg"],
    ["MoeDay"]
],
"1011": [
    ["WakasaYuuri", "https://gakkougurashi.com/core_sys/images/main/cont/chara/ch03-1.png"],
    ["LoliDay"]
],
"1014": [["KawakamiMai", "https://phantom-world.com/img/character/mai.png"]],
"1015": [["Compilation"]],
"1018": [["HasegawaKobato", "https://www.tbs.co.jp/anime/haganai/1st/chara/images/chara_img06.jpg"]],
"1019": [["EbinaNana", "https://umaru-ani.me/img/character/chara3_stand.png"]],
"1020": [["Compilation"]],
"1021": [["Compilation"]],
"1023": [["NishizumiMiho", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/miho.png"]],
"1024": [
    ["ProgrammerDay"],
    ["ShimadaArisu", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/arisu.png"]
],
"1025": [
    ["EmiliaJustina", "https://maousama.jp/assets/img/character/character02_main.png"],
    ["MamiyaAkari", "http://ariaaa.tv/character/images/img_chara-1.png"]
],
"1027": [["Compilation"]],
"1029": [
    ["ShiretokoRin", "https://www.hai-furi.com/assets_mv/img/chara/01_kankyo/06_shiretoko/img_main.png"],
    ["YonemeMei", "https://www.lovelive-anime.jp/yuigaoka/member/img/c07a.png"]
],
"1101": [["HoshizoraRin", "https://www.lovelive-anime.jp/otonokizaka/img/member/member05_01.png"]],
"1102": [
    ["HiyajyouMaho", "https://steinsgate0-anime.com/wp-content/themes/steinsgate/img/index/img_charamain09_1.png"],
    ["NatsuMegumi", "https://gochiusa.com/core_sys/images/main/cont/chara/megu_body.png"]
],
"1103": [["Noel", "https://sora-no-method.jp/character/img/chara_noel_body.png"]],
"1105": [["Katsuragi", "https://senran.tv/images/character/p3.jpg"]],
"1106": [["YoshikawaChinatsu", "https://yuruyuri.com/1st/character/img/detail_chinatsu.jpg"]],
"1107": [["SuminoeXko", "https://img.moegirl.org.cn/common/a/a1/Suminoe_Ako_Riko.jpg"]],
"1109": [["TsukiyomiUtau", "https://img.moegirl.org.cn/common/thumb/5/53/Tsukiyomi_Utau2.jpg/420px-Tsukiyomi_Utau2.jpg"]],
"1110": [["SakakiYumiko", "https://grisaia-anime.com/kajitsu/core_sys/images/contents/00000003/base/001.png"]],
"1111": [
    ["KuraueHinata", "https://yamanosusume-ns.com/core_sys/images/main/cont/chara/hinata_stand.png"],
    ["TobiichiOrigami", "https://date-a-live-anime.com/1st-2nd/common/images/2nd/character/character_origami.png"]
],
"1113": [["Compilation"]],
"1118": [
    ["NagatoYuki", "https://img.moegirl.org.cn/common/thumb/4/4b/Nagato_Yuki2.jpg/420px-Nagato_Yuki2.jpg"],
    ["TsukiyomiRuna", "https://www.geneitaiyo.com/character/img/main/luna.png"]
],
"1119": [["Compilation"]],
"1122": [["KoiwaiYoshino", "https://img.moegirl.org.cn/common/a/a5/Koiwai_Yoshino_2023.jpg"]],
"1124": [["HazukiRen", "https://www.lovelive-anime.jp/yuigaoka/member/img/c05a.png"]],
"1125": [["Compilation"]],
"1127": [["HirasawaYui", "https://www.tbs.co.jp/anime/k-on/k-on_tv/chara/images/chara_photo01_1.gif"]],
"1129": [["ShichijyouAria", "https://king-cr.jp/special/seitokai/images/s-council/aria.gif"]],
"1130": [["Mika", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/mika.png"]],
"1201": [["Compilation"]],
"1203": [
    ["MiyauchiRenge", "https://img.moegirl.org.cn/common/thumb/1/1d/%E5%AE%AB%E5%86%85%E8%8E%B2%E5%8D%8E.jpg/540px-%E5%AE%AB%E5%86%85%E8%8E%B2%E5%8D%8E.jpg"],
    ["SanzeninNagi", "http://hayatenogotoku.com/images/chara/nagi.jpg"],
    ["TouyamaRin", "https://img.moegirl.org.cn/common/thumb/1/17/%E8%BF%9C%E5%B1%B1%E4%BC%A6.png/750px-%E8%BF%9C%E5%B1%B1%E4%BC%A6.png"]
],
"1204": [
    ["KafuuChino", "https://gochiusa.com/core_sys/images/main/cont/chara/chino_body.png"],
    ["Megumin", "http://konosuba.com/3rd/character/img/megumin.png"]
],
"1206": [
    ["IijimaYun", "https://img.moegirl.org.cn/common/thumb/8/87/%E9%A5%AD%E5%B2%9B6.png/600px-%E9%A5%AD%E5%B2%9B6.png"],
    ["MiaTaylor", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c12a.png"]
],
"1208": [["NishiKinuyo", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/kinuyo.png"]],
"1210": [
    ["IzumiSagiri", "https://eromanga-sensei.com/assets/img/character/chara_02.png"],
    ["NaokiMiki", "https://gakkougurashi.com/core_sys/images/main/cont/chara/ch04-1.png"]
],
"1212": [["Compilation"]],
"1215": [["KaramaruChitose", "https://img.moegirl.org.cn/common/thumb/e/e8/Karasuma_blu.png/420px-Karasuma_blu.png"]],
"1216": [
    ["IsuzuHana", "https://girls-und-panzer.jp/XPLk3DYg/wp-content/uploads/2020/02/isuzu.png"],
    ["KonoeKanata", "https://www.lovelive-anime.jp/nijigasaki/img/tv/member/c07a.png"],
    ["NatsumeNono", "https://img.moegirl.org.cn/common/thumb/0/04/%E4%B9%83%E4%B9%83_I.jpg/420px-%E4%B9%83%E4%B9%83_I.jpg"]
],
"1222": [["EnmaAi", "https://img.moegirl.org.cn/common/7/70/Cute.jpg"]],
"1223": [
    ["HoshikawaMafuyu", "https://blend-s.jp/assets/img/character/chara_03/chara03_1.png"],
    ["Yagyuu", "https://senran.tv/images/character/p4.jpg"]
],
"1224": [
    ["AdagakiAki", "https://img.moegirl.org.cn/common/0/0d/Adagakiaki.jpg"],
    ["HiiragiMayuki", "https://hinakonote.jp/assets/character/c3.jpg"],
    ["MikazukiYozora", "https://www.tbs.co.jp/anime/haganai/1st/chara/images/chara_img02.jpg"],
    ["TachibanaSylphinford", "https://umaru-ani.me/img/character/chara5_stand.png"]
],
"1225": [
    ["Eris", "http://konosuba.com/3rd/character/img/chris.png"],
    ["HayamaTeru", "http://sansyasanyou.com/core_sys/images/contents/00000004/base/sn_001.png"],
    ["MatsushimaMichiru", "https://grisaia-anime.com/kajitsu/core_sys/images/contents/00000005/base/001.png"],
    ["MurakamiShiina", "https://img.moegirl.org.cn/common/thumb/a/a0/Charaillust_chara_16020010.png/420px-Charaillust_chara_16020010.png"],
    ["ItouMakotoDead", "https://bkimg.cdn.bcebos.com/pic/adaf2edda3cc7cd98d10aacc8c4b363fb80e7bec3bd9?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U5Mg==,g_7,xp_5,yp_5"]
],
"1226": [["Takao", "https://img.moegirl.org.cn/common/thumb/e/ed/Takao_bucho.jpg/420px-Takao_bucho.jpg"]],
"1228": [
    ["Mirai", "https://senran.tv/images/character/p9.jpg"],
    ["OnitsukaTomari", "https://www.lovelive-anime.jp/yuigaoka/member/img/c11a.png"]
],
"1231": [
    ["HanakoizumiAnne", "https://anne-happy.com/wp-content/uploads/2016/02/ch1-1-1.png"],
    ["Yumi", "https://senran2.tv/img/charactor_yumi.png"]
]
}

@cld.handle()
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
    await sendNotice(Message([
        MessageSegment.text(desc),
        MessageSegment.image("base64://" + str(buf, "utf-8"))
    ]))
