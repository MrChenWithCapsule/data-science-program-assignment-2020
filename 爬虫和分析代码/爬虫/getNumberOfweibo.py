import requests
import time
import simplejson
import bs4
import re
from bs4 import BeautifulSoup
import os
import csv


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DICT = {}
def get_dict():
    for index in range(len(ALPHABET)):
        DICT[ALPHABET[index]] = index
        #62 to 10
def key62_to_key10(str_62):
    value = 0
    for s in str_62:
        value = value * 62 + DICT[s]
    return value

def key10_to_key62(str_10):
    ans=""
    if (str_10<62):
        return ALPHABET[int(str_10 % 62)]
    for i in range(0,4):
        ans=ALPHABET[int(str_10 % 62)]+ans
        str_10/=62
    return ans

def murl_to_mid(murl):
    length = len(murl)
    mid = ''
    group = int(length/4)
    #four characters per group
    last_count = length % 4
    #head group character counts
    for loop in range(group):
        value = key62_to_key10(murl[length-(loop+1)*4:length-loop*4])
        mid = str(value) + mid
        if last_count:
            value = key62_to_key10(murl[:length-group*4])
            mid = str(value) + mid
    return mid

def mid_to_murl(mid):
    murl=""
    murl=murl+key10_to_key62(int(mid[0:2]))
    murl=murl+key10_to_key62(int(mid[2:9]))
    murl = murl + key10_to_key62(int(mid[9:16]))
    return murl

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie':'''***'''
}
access_token='***'
#access_token='***'
url='https://api.weibo.com/2/statuses/count.json?access_token={}&ids={}'

def getCommentsByMid(mid):
    time.sleep(2)
    r=requests.get(url.format(access_token,mid),headers=headers)
    print(r.text)
    json=simplejson.loads(r.text,encoding='utf-8')
    return json[0].get("comments")

def writeCommentsInFile(path):
    print(path)
    str=""
    with open(path,"r",encoding='utf-8') as f:
        #print(f.readline())
        json=simplejson.loads(f.readline(),encoding='utf-8')
        num=getCommentsByMid(json.get("mid"))
        json["Comments"]=num
        str=simplejson.dumps(json)
        #print(str)
    with open(path,"w",encoding='utf-8') as f:
        f.write(str)

def writeJSON(mid,path):
    pass

def loadAllFile(path):
    for root,ds,fs in os.walk(path):
        for file in fs:
            if (file[-4:]=="json"):
                #print(os.path.join(root,file))
                print(int(file[:16]))
                #if (int(file[:16])<=4470871236360193):
                    #continue
                writeCommentsInFile(os.path.join(root,file))
            #if (file[-3:]=="csv"):
                #writeJSON(int(file[:16]),os.path.join(root,int(file[:16])+".csv"))

get_dict()
loadAllFile("微博评论1~2月/02/")
