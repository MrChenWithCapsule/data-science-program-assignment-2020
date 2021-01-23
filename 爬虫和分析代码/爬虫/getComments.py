import requests
import time
import simplejson

#m.weibo.cn/api/comments/show?id=4585004007170918&page={}'
#url='https://api.weibo.com/2/comments/show.json?access_token={}&id={}&page={}'
url='https://weibo.com/aj/v6/comment/big?id={}&page={}&filter=hot&from=singleWeiBo'
headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie':'''SINAGLOBAL=306247412736.6266.1596466067403; UOR=www.51testing.com,widget.weibo.com,www.baidu.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5syM4qJC.64UdSy23mbVBU5JpX5KMhUgL.FoMfeoqR1Kn4e0q2dJLoI7y-PNSoeo57eBtt; ALF=1640423976; SSOLoginState=1608887966; SCF=AoRgUU7yBzwdBZYZTnlIDGlkru0ITifIfcWw25WPEmUhyPZ2sY5pt7qm0Z03nfX9KTyaItwkKubkYmg1YpQe690.; SUB=_2A25y4d75DeRhGeFL6VQZ-SbFyDqIHXVRlrcxrDV8PUNbmtANLRH8kW9NQlA_DaIvbmO8uKrL6F399PPtcHXsUksa; _s_tentry=weibo.com; Apache=715240225389.2177.1608887983149; ULV=1608887983207:4:2:2:715240225389.2177.1608887983149:1608720790017; WBStorage=8daec78e6a891122|undefined; webim_unReadCount=%7B%22time%22%3A1608888111515%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A41%2C%22msgbox%22%3A0%7D'''
}
#access_token='2.00kPG5NIlQdZAE8b262bdf81WAD4VD'

time.sleep(1)
cnt=100000000
#4585003164115089
while (True):
    #r=requests.post('https://api.weibo.com/oauth2/access_token?client_id=3673023763&client_secret=ec1f1f337395c849bdcc5eb037c2362d&grant_type=authorization_code&redirect_uri=http://127.0.0.1:8081&code=b24e74c3bb9116c5fe4d6617ec97fcae',headers=headers)
    print(url.format( '4585921477088841', cnt))
    time.sleep(1)
    r=requests.get(url.format('4585921477088841',cnt),headers=headers).content.decode('utf-8')
    print(r)
    json=simplejson.loads(r,encoding='utf-8')
    #if (len(json.get("comments"))==0):
        #break
    with open('JSON{}.txt'.format(str(cnt)),'w',encoding='utf-8') as f:
        f.write(json.get("data").get("html"))
    break
