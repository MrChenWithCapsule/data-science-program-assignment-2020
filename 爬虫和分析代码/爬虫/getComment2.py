from urllib import request
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie': '''***'''
}
url='https://weibo.com/aj/v6/comment/big?id={}&page={}&filter=hot&from=singleWeiBo'
id = '4462923885496647'

for i in range(51, 55):
    print('page {}'.format(i))
    with open('out/{}.json'.format(i), 'wb') as out:
        req = request.Request(url.format(id, i), headers=header)
        with request.urlopen(req) as resp:
            json = resp.read()
            out.write(json)
            # print(json)
