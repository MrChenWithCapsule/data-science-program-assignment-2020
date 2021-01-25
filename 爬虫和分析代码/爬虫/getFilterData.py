import requests
import time
import simplejson
import bs4
import re
from bs4 import BeautifulSoup
import os
import csv

url='https://weibo.com/aj/v6/comment/big?id={}&page={}&filter=hot&from=singleWeiBo'
search_url='https://s.weibo.com/weibo?q={}&category=4&suball=1&timescope=custom:{}-0:{}-23&Refer=g&page={}'
headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie':'''***'''
}
access_token='***'
def getCommnetsInPage(html):
    if (html==None):
        return []
    bs = BeautifulSoup(html, 'html.parser')
    resultSet=bs.find_all("div",attrs={"comment_id":re.compile("\d+")})
    commentSet=[]
    for item in resultSet:
        text=item.find("div",class_="WB_text").text
        text=str(text).split("：")[1]
        date=item.find("div",class_="WB_from S_txt2").text
        # print(text)
        # print(date)
        if(text==""):
            continue
        commentSet.append({"date":date,"text":text})
    return commentSet

def writeInFile(mid,month,page,comments):
    if (os.path.exists('FilterData/{}'.format(month)) == False):
        os.mkdir('FilterData/{}'.format(month))
    with open("FilterData/{}/{}.csv".format(month,mid),'a',encoding='utf-8') as f:
        csv_writer=csv.writer(f)
        for item in comments:
            csv_writer.writerow([item.get("date"),item.get("text"),page])

def getComments(mid,month):
    last=""
    page=1
    while (page<=50):
        print("Comments page="+str(page))
        time.sleep(1)
        try:
            r=requests.get(url.format(mid,page),headers=headers).content.decode("utf-8")
        except:
            r = requests.get(url.format(mid, page), headers=headers).content.decode("utf-8")
        json=simplejson.loads(r,encoding='utf-8')
        html=json.get("data").get("html")
        comments=getCommnetsInPage(html)
        if (comments==None or len(comments)==0):
            break
        if (comments[0].get('text')==last):
            print(page)
            break
        last=comments[0].get('text')
        writeInFile(mid,month,page,comments)
        page+=1

def ReadInfoInFile(month, L, R):
    path = "Data/{}".format(month)
    for root, ds, fs in os.walk(path):
        for file in fs:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                s = f.readline()
                # print(s)
                f.close()
                json = simplejson.loads(s, encoding='utf-8')
                comments = json.get("Comments")
                # print(comments)
                if (int(comments) >= L and int(comments) <= R):
                    mid = file[:-5]
                    if (os.path.exists("FilterData/{}/{}.csv".format(month,mid)) == False):
                        print(mid)
                        getComments(mid,month)
                    with open("FilterData/{}/{}.json".format(month,mid),'w',encoding='utf-8') as f:
                        f.write(simplejson.dumps(json,encoding='utf-8'))


def ReadAllJSONFile(month):
    path='{}月过滤评论区间.json'.format(month)
    L=0
    R=0
    with open(path,'r',encoding='utf-8') as f:
        json=f.readline()
        section=simplejson.loads(json,encoding='utf-8')
        L=int(section.get("L"))
        R=int(section.get("R"))
    if (month<10):
        ReadInfoInFile("0"+str(month),L,R)
    else:
        ReadInfoInFile(str(month), L, R)


if __name__=='__main__':
    for i in range(1,3):
        ReadAllJSONFile(i)

