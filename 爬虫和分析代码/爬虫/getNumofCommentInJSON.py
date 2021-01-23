import simplejson
cnt=0
for i in range(1,35):
    with open('JSON{}.txt'.format(i),'r',encoding='utf-8') as f:
        jsonstr=f.readlines()
        for str in jsonstr:
            json=simplejson.loads(str,encoding='utf-8')
            cnt+=len(json.get("comments"))
            print(len(json.get("comments")))
print(cnt)