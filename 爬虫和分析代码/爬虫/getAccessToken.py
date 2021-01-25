import requests
import simplejson
headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie':'''***'''
}
appkey='***'
appsercet='***'
code="***"
redirect_url='http://127.0.0.1:8081'
url1='https://api.weibo.com/oauth2/authorize?client_id={}&redirect_uri={}'
url2='https://api.weibo.com/oauth2/access_token?client_id={}&client_secret={}&grant_type=authorization_code&code={}&redirect_uri={}'
print(url1.format(appkey,redirect_url))
#r=requests.get(url1.format(appkey,redirect_url),headers=headers).content.decode('utf-8')
r=requests.post(url2.format(appkey,appsercet,code,redirect_url),headers=headers).content.decode('utf-8')
print(r)
print(requests.post('https://api.weibo.com/oauth2/access_token?client_id=***&client_secret=***&grant_type=authorization_code&code=***&redirect_uri=http://127.0.0.1:8081').text)
