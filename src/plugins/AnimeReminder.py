from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from ..utils import sendGroupMessage

import json
import requests
import time
import sys

WeekName = ["月", "火", "水", "木", "金", "土", "日"]

GroupId = [855524548, 1161079807]

ALurl = "https://graphql.anilist.co"

QueryStr = """
query ($page: Int, $seasonYear: Int, $season: MediaSeason) {
  Page(page: $page, perPage: 20){
    pageInfo {
      total
      currentPage
      lastPage
    }
    media(seasonYear: $seasonYear, season: $season, type: ANIME) {
      title{
        native
      }
      nextAiringEpisode {
        timeUntilAiring
        episode
      }
    }
  }
}
"""

Content = "今天是{date}  {day}\n今天更新的番剧有{total}部："

def getVariables():
    now = time.localtime(time.time())
    seasonYear = now.tm_year
    month = now.tm_mon
    if month in [10, 11, 12]:
        season = "FALL"
    elif month in [1, 2, 3]:
        season = "WINTER"
    elif month in [4, 5, 6]:
        season = "SPRING"
    elif month in [7, 8, 9]:
        season = "SUMMER"
    return {"page": 1, "season": season, "seasonYear": seasonYear}

@scheduler.scheduled_job("cron", hour=8, minute=40, second=0, id="Anime Reminder")
def AnimeReminder():
    AniList = ""
    total = 0
    variables = getVariables();
    while True:
        response = requests.post(ALurl, json={"query": QueryStr, "variables": variables})
        page = json.loads(response.text)["data"]["Page"]
        pageInfo = page["pageInfo"]
        media = page["media"]
        for item in media:
            if item["nextAiringEpisode"] == None:
                continue
            restTime = item["nextAiringEpisode"]["timeUntilAiring"]
            if restTime <= 86400:
                title = item["title"]["native"]
                episode = item["nextAiringEpisode"]["episode"]
                AniList = AniList + f"\n[{total}] {title} #{episode}"
                total = total + 1
        if pageInfo["currentPage"] == pageInfo["lastPage"]:
            break
        variables["page"] = pageInfo["currentPage"] + 1
    now = time.localtime(time.time())
    date = time.strftime("%Y年%m月%d日", now)
    day = f"{WeekName[now.tm_wday]}曜日"
    AniList = Content.format(date=date, day=day, total=total) + AniList
    for group_id in GroupId:
      sendGroupMessage(group_id, AniList)
      time.sleep(2)
