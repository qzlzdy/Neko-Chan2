from nonebot import on_keyword
from nonebot import on_message
from nonebot.adapters import Event
from nonebot.rule import Rule
from nonebot.matcher import Matcher
from urllib.parse import quote
from random import randint

async def question_words(event: Event) -> bool:
    text = event.get_plaintext()
    return text.endswith("吗")

async def question_predicates(event: Event) -> bool:
    preds = ["是", "有", "要", "去"]
    text = event.get_plaintext()
    for p in preds:
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
    if randint(0, 9) == 0:
        keyword = event.get_plaintext()
        await matcher.finish(redirectToBaidu(keyword))

