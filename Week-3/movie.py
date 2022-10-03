import urllib.request as request
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/movie/index.html"

def getData(url):
    get = request.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
    })

    with request.urlopen(get) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    print(root)

url = "https://www.ptt.cc/bbs/movie/index.html"
getData(url)