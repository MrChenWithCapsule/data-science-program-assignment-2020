import requests
import time
import simplejson

#m.weibo.cn/api/comments/show?id=4585004007170918&page={}'
#url='https://api.weibo.com/2/comments/show.json?access_token={}&id={}&page={}'
url='https://weibo.com/aj/v6/comment/big?id={}&page={}&filter=hot&from=singleWeiBo'
headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie':'''***'''
}
#access_token='***'

time.sleep(1)
cnt=100000000
#4585003164115089
while (True):
    #r=requests.post('https://api.weibo.com/oauth2/access_token?client_id=***&client_secret=***&grant_type=authorization_code&redirect_uri=http://127.0.0.1:8081&code=***',headers=headers)
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
