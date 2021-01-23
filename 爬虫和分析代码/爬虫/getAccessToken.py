import requests
import simplejson
headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie':'''SINAGLOBAL=9586457965397.959.1598603806172; SCF=AkSgI7SC_aq2QR8nBPk6pPovWpjj8WuEdb0pYiyLNcR8wyZtvdeG2ChOgxEsMg19o7ll0tGU4CD6xSYlY9nbBL0.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5syM4qJC.64UdSy23mbVBU5NHD95QNSKzc1h.R1KecWs4DqcjzH8v0q0z7eh2t; ALF=1638694420; SUB=_2A25yzzq2DeRhGeFL6VQZ-SbFyDqIHXVuMEb-rDV8PUJbkNANLWPgkW1NQlA_DTqvvemc-Y2J2Y8qSF_7iWBrxkaW; UOR=fo.ifeng.com,widget.weibo.com,www.baidu.com; _s_tentry=-; Apache=7641791790523.902.1608886696428; ULV=1608886696531:8:6:2:7641791790523.902.1608886696428:1608712517043; webim_unReadCount=%7B%22time%22%3A1608892667024%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A42%2C%22msgbox%22%3A0%7D; wvr=6; WBStorage=8daec78e6a891122|undefined'''
}
appkey='3673023763'
appsercet='ec1f1f337395c849bdcc5eb037c2362d'
code="c827e51ed9b159a100dd08093f3c7a57"
redirect_url='http://127.0.0.1:8081'
url1='https://api.weibo.com/oauth2/authorize?client_id={}&redirect_uri={}'
url2='https://api.weibo.com/oauth2/access_token?client_id={}&client_secret={}&grant_type=authorization_code&code={}&redirect_uri={}'
print(url1.format(appkey,redirect_url))
#r=requests.get(url1.format(appkey,redirect_url),headers=headers).content.decode('utf-8')
r=requests.post(url2.format(appkey,appsercet,code,redirect_url),headers=headers).content.decode('utf-8')
print(r)
print(requests.post('https://api.weibo.com/oauth2/access_token?client_id=1769153833&client_secret=5e45237d92f8d16d4ad8edc19509920e&grant_type=authorization_code&code=d5336e40c26b119ea323e2c61197e0de&redirect_uri=http://127.0.0.1:8081').text)
#4d3cf995833bcc13b5c4c7e2a0a3c4de
#d5336e40c26b119ea323e2c61197e0de