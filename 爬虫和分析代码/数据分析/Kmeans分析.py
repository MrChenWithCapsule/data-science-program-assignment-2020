import  csv
import simplejson
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  scipy import stats
from Kmeans结果评价 import SSECal
from scipy.cluster.vq import kmeans,vq,whiten
count=[0,0,0,0,0,0,0,0]
arr=[]
sse=SSECal()
def getDataNumInCSV(path):
    #print(path)
    try:
        df=(pd.DataFrame(pd.read_csv(path)))
    except:
        return 0
    return len(df)

#获得JSON文件内的评论数
def getCommentNumInJSON(path):
    #print(path)
    with open(path,'r',encoding='utf-8') as f:
        str=f.readline()
        json=simplejson.loads(str,encoding='utf-8')
        num=json.get("Comments")
        if (num==None):
            return 0
        #arr.append(num)
        arr.append(int(num))
        #print(num)
    return num

def getAllFile(path):
    for root,ds,fs in os.walk(path):
        for file in fs:
            if (file[-4:]=="json"):
                getCommentNumInJSON(os.path.join(root,file))

# def getAllFileofBili(path):
#     for root,ds,fs in os.walk(path):
#         for file in fs:
#             arr.append(getDataNumInCSV(os.path.join(root,file)))

def getBilibiliDataNum():
    pass
    #path1='大作业数据集合/B站数据/综合'
    #getAllFile(path1)
    #path2 = '大作业数据集合/B站数据/新冠'
    #getAllFileofBili(path2)

#获得所有目录下的微博信息
def getWeiboDataNum():
    path1 = '大作业数据集合/微博数据/Data/01'
    path2='大作业数据集合/微博数据/Data/02'
    path3 = '大作业数据集合/微博数据/Data/03'
    path4 = '大作业数据集合/微博数据/Data/04'
    path5 = '大作业数据集合/微博数据/Data/05'
    path6 = '大作业数据集合/微博数据/Data/06'
    path7 = '大作业数据集合/微博数据/Data/07'
    path8 = '大作业数据集合/微博数据/Data/08'
    getAllFile(path1)
    run(1)
    getAllFile(path2)
    run(2)
    getAllFile(path3)
    run(3)
    getAllFile(path4)
    run(4)
    getAllFile(path5)
    run(5)
    getAllFile(path6)
    run(6)
    getAllFile(path7)
    run(7)
    getAllFile(path8)
    run(8)

def KmeansAnalysis(p,data,K):
    p=whiten(p)
    #print(p)
    center,dis=kmeans(p,K)
    #print(center)
    print(dis)
    cluster,_=vq(p,center)
    #print(cluster)
    clu=[[],[],[],[],[],[],[]]
    for i in range(0,len(cluster)):
        clu[cluster[i]].append(i)
    for i in range(0,K):
        #print(clu[i])
        print("len="+str(len(clu[i])))
    return clu

def getPicture(num,clu,data,K):
    plt.title="{}月数据".format(num)
    comments=0
    group=[0]
    max1=0
    max2=0
    max3=0
    max4=0
    for i in range(0,K):
        x=[]
        y=[]
        for j in clu[i]:
            x.append(j)
            y.append(data[j])
        group.append(max(y))
        if (group[i+1]>group[max1]):
            max4=max3
            max3=max2
            max2 = max1
            max1=i+1
        elif (group[i+1]>group[max2]):
            max4=max3
            max3=max2
            max2=i+1
        elif (group[i+1]>=group[max3]):
            max4=max3
            max3=i+1
        elif (group[i+1]>=group[max4]):
            max4=i+1
        plt.scatter(x,y,label=i)
        plt.legend()
    print(str(max1-1)+" "+str(max2-1)+" "+str(max3-1))
    comments=len(clu[max1-1])+len(clu[max2-1])
    print("过滤后有"+str(comments))
    #plt.savefig('E:/大学学习资料/数据分析/{}月评论量分布图'.format(num))
    plt.show()
    return {"L":str(group[max3]+1),"R":str(group[max1])}

def run(num):
    global arr
    arr.sort()
    p = np.array(arr)
    data = np.array(arr)
    global sse
    sse.addData(data)
    print(str(num)+"'s len="+str(len(p)))
    count[num-1]=len(p)
    K=5
    clu = KmeansAnalysis(p, data,K)
    section=getPicture(num,clu,data,K)
    print(section)
    with open("{}月过滤评论区间.json".format(num),'w',encoding='utf-8') as f:
        json=simplejson.dumps(section,encoding='utf-8')
        #f.write(json)
    arr=[]

arr=[]
getWeiboDataNum()
print(count)
sse.SSE()

