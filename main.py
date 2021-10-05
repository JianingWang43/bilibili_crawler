import random
import requests
import json
import re
import os

os.system("pip3 install you-get")
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
def downView(url,title):
    res = requests.get(url, headers={'User-Agent': random.choice(my_headers)}, verify=False)
    with open(title,"wb")as f:
        f.write(res.content)
        f.close()

pagemax=int(input("please input max page\n"))
page = 0
durationmax=int(input("please input max duration(second)\n"))
print("getting download urls...\n")
while page <= pagemax-1:
    page+=1
    r = requests.get('https://api.bilibili.com/x/web-interface/popular?ps=20&pn='+str(page), headers={'User-Agent': random.choice(my_headers)})
    if r.status_code != 200:
        print("http error code" + r.status_code)
        exit(0)
    else:
        res = json.loads(r.text)
        for data in res['data']['list']:
            if int(data['duration']) < durationmax:

                print(data['title'])
                print(data['duration'])
                print(data['bvid'])

                url = "https://www.bilibili.com/video/"+data['bvid']
                os.system("you-get "+url)