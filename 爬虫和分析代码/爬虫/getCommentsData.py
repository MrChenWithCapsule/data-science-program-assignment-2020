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

def getDate(str):
    r=r'\d\d'
    pattern=re.compile(r)
    result=pattern.findall(str)
    print(str)
    if (len(result)==1):
        return "0000"
    if (len(result)>2):
        return "2020-"+result[2]+"-"+result[3]
    return "2020-"+result[0]+"-"+result[1]

def getInformation(card,start):
    mid=card.get("mid")
    print(mid)
    #print(card.find("p",class_="from"))
    if (card.find("p",class_="from")==None):
        return None
    From=card.find("p",class_="from").find("a").text
    date=getDate(From)
    print("From="+From)
    if (date!=start):
        return None
    text=card.find("p",class_="txt").text
    print("text="+text)
    comments=card.find("div",class_="card-act").find("a",attrs={"action-type":"feed_list_comment"}).text
    print("comments="+comments)
    pattern=re.compile('\d+')
    commentNum=pattern.search(comments)
    if (commentNum==None):
        return {"date": date, "mid": mid, "text": text, "Comments": 0}
    print("Num="+str(commentNum.group(0)))
    return {"date":date,"mid":mid,"text":text,"Comments":commentNum.group(0)}

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

def writeInFile(mid,month,date,page,comments):
    if (os.path.exists("BigData/"+month) == False):
        os.mkdir("BigData/"+month)
    with open("BigData/{}/{}.csv".format(month,mid),'a',encoding='utf-8') as f:
        csv_writer=csv.writer(f)
        for item in comments:
            csv_writer.writerow([item.get("date"),item.get("text"),page])

def writeInfoInFile(info,month):
    if (os.path.exists("BigData/") == False):
        os.mkdir("BigData/")
    if (os.path.exists("BigData/"+month) == False):
        os.mkdir("BigData/"+month)
    if (os.path.exists("BigData/{}/{}.json".format(month,info.get("mid"))) == True):
        return False
    with open("BigData/{}/{}.json".format(month,info.get("mid")),'w',encoding='utf-8') as f:
        print({"mid":info.get("mid"),"date":info.get("date"),"Comments":info.get("Comments"),"text":info.get("text")})
        json=simplejson.dumps({"mid":info.get("mid"),"date":info.get("date"),"Comments":info.get("Comments"),"text":info.get("text")},encoding='utf-8')
        f.write(json)
    return True

def getComments(info,month):
    mid=info.get("mid")
    date=info.get("date")
    last=""
    page=1
    print("new mid="+str(mid))
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
        writeInFile(mid,month,date,page,comments)
        page+=1

#只向文件中写入信息
def getSearchresult(word,start,end):
    page=1
    cnt=0
    while (page<=4):
        if (cnt>40):
            break
        time.sleep(1)
        r = requests.get(search_url.format(word, start, end,page),headers=headers).content.decode('utf-8')
        bs = BeautifulSoup(r,"html.parser")
        #print(r)
        #if not (bs.find("div",attrs={"class":"card-no-result"})):
            #break
        resultSet=bs.find_all("div",attrs={"class":"card-wrap"})
        for card in resultSet:
            if (cnt>40):
                break
            if (card==None):
                continue
            info=getInformation(card,start)
            if(info==None):
                continue
            if (writeInfoInFile(info, start[5:7])==True):
                getComments(info,start[5:7])
            cnt+=1
            #print(info)
        print("page="+str(page))
        page+=1


if __name__=='__main__':
    daysofmonth=[31,29,31,30,31,30,31,31,30,30,30,30]
    print("搜索关键词")
    word=input()
    #print("开始日期")
    #start=input()
    #print("结束日期")
    #end=input()
    #for j in range(2,3):
    start="2020-02"
    #for i in range(1,10):
        #getSearchresult(word,start+"-0"+str(i),start+"-0"+str(i))
    for i in range(12,17):
        getSearchresult(word, start+"-"+str(i),start+"-"+str(i))

