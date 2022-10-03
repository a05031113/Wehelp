import urllib.request as request
import json
import csv
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 要求一
# data address
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

# open data as response and load by json.load
with request.urlopen(src) as response:
    data = json.load(response)

# set as lis
lis = data["result"]["results"]

# write data into csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # run for loop to collect data we need
    for i in lis:
        date = i["xpostDate"].split("/") # data
        address = i["address"].split(" ")[2][:3] # address with district
        jpg = i["file"].split("https") # separate all jpg url
        jpg1 = "https"+jpg[1] # first jpg file
        # collect data which >=2015
        if int(date[0])>=2015:
            writer.writerow([i["stitle"], address, i["longitude"], i["latitude"], jpg1])


# 要求二
good = [] # 好雷
bad = [] # 負雷
normal = [] # 普雷
# 定義函數
def getData(url):
    # 取得user-agent
    get = request.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
    })
    # 解碼
    with request.urlopen(get) as response:
        data = response.read().decode("utf-8")
    # 找到全部的title
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    # 辨認好普負雷並存敬list
    for title in titles:
        if title.a != None:
            if title.a.string[1:3]=="好雷":
                good.append(title.a.string)
            elif title.a.string[1:3]=="負雷":
                bad.append(title.a.string)
            elif title.a.string[1:3]=="普雷":
                normal.append(title.a.string)
    # return 下頁網址
    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]

url = "https://www.ptt.cc/bbs/movie/index.html"
# 跑十頁
count = 0
while count<10:
    url = "https://www.ptt.cc"+getData(url)
    count+=1
# 寫入檔案
with open("movie.txt", mode="w", encoding="utf-8") as file:
    for i in good:
        file.write(i)
        file.write("\n")
    for i in normal:
        file.write(i)
        file.write("\n")
    for i in bad:
        file.write(i)
        file.write("\n")