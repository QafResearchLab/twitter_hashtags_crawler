from datetime import date
import snscrape.modules.twitter
import json
import time
import os


dictionary = [
    'ارحلوالننترككم',
    'ارحلوا_لن_نترككم',
    'انهزام_امريكا',
    'قدماستقالةفاشل',
    'قدم_استقالة_فاشل',
    'الكاظميزعيمالمافيات',
    'الكاظمي_زعيم_المافيات',
]

timeSpent = 'Begenning = '
startDate = time.time()
timeSpent += str(date.today()) + '\n'
totalTime = 0

try:
    os.mkdir('snscrape/')
except:
    pass

for dictionaraya in dictionary:
    finalList = []
    print(f"{dictionaraya}")
    snscrape.modules
    for tweet in snscrape.modules.twitter.TwitterHashtagScraper(f'{dictionaraya}').get_items():
        finalList.append(
            {"username": tweet.username, "content": tweet.content, "datetime": str(tweet.date), "url": tweet.url, "id": tweet.id})
    jsonized = json.dumps(finalList, separators=(',', ':'), ensure_ascii=False)
    f = open(f"snscrape/{dictionaraya}.txt", "w", encoding='utf8')
    f.write(jsonized)
    f.close()
    temp = time.time() - startDate
    totalTime += temp
    timeSpent += dictionaraya + ' took = ' + str(temp) + '\n'
    startDate = time.time()

timeSpent += 'Total Time = ' + str(totalTime)

startDateFile = open("timeSpent.txt", "w", encoding="utf-8")
startDateFile.write(timeSpent)
startDateFile.close()