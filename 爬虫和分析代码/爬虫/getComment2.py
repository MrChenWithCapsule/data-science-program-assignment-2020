from urllib import request
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie': '''SINAGLOBAL=306247412736.6266.1596466067403; login_sid_t=9bbd0f8cd2f72d4e31e8a32793f53756; cross_origin_proto=SSL; _s_tentry=www.baidu.com; UOR=www.51testing.com,widget.weibo.com,www.baidu.com; Apache=3534626251570.1255.1608720790011; ULV=1608720790017:3:1:1:3534626251570.1255.1608720790011:1606631489433; ALF=1640256820; SSOLoginState=1608720820; SUB=_2A25y51HkDeRhGeFL6VQZ-SbFyDqIHXVRlcQsrDV8PUNbmtB-LUXNkW9NQlA_DXvcomSxvFIpTLhGFjXvw6x1Tl8R; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5syM4qJC.64UdSy23mbVBU5JpX5KzhUgL.FoMfeoqR1Kn4e0q2dJLoI7y-PNSoeo57eBtt; wvr=6; webim_unReadCount=%7B%22time%22%3A1608721929406%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A42%2C%22msgbox%22%3A0%7D'''
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
