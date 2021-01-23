import requests,time
def getIDList():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    since_id=4519108261859545
    api_url = 'https://m.weibo.cn/api/container/getIndex?containerid=100808968e8dcd713b8a2d6416b94785989da9_-_feed&luicode=10000011&lfid=100103type%3D1%26amp%3Bq%3D%E7%96%AB%E6%83%85'
    comment=[]
    for i in range(1,10):
        time.sleep(2)
        url=api_url+"&since_id="+(str)(since_id)
        reponse = requests.get(url)
        for json in reponse.json()['data']['cards'][0]['card_group']:
            comment_ID = json['mblog']['id']
            print (comment_ID)
            comment.append(comment_ID)
        since_id=(int)(comment_ID)
    return comment