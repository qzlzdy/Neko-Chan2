from nonebot import on_keyword
from nonebot import on_message
from nonebot.adapters import Event
from nonebot.rule import Rule
from nonebot.matcher import Matcher
from urllib.parse import quote

async def question_words(event: Event) -> bool:
    text = event.get_plaintext()
    return text.endswith("吗")

async def question_predicates(event: Event) -> bool:
    pred = ["是", "有", "要", "去"]
    text = event.get_plaintext()
    for p in pred:
        if p in text:
            return True
    return False

pred_checker = Rule(question_words, question_predicates)

question1 = on_keyword(["什么", "怎么", "在哪"])
question2 = on_message(rule=pred_checker)

def redirectToBaidu(keyword):
    url = "https://www.baidu.com/s?wd=%s"
    wd = quote(keyword)
    return url % wd

@question1.handle()
@question2.handle()
async def question_handler(matcher: Matcher, event: Event):
    keyword = event.get_plaintext()
    await matcher.finish(redirectToBaidu(keyword))

