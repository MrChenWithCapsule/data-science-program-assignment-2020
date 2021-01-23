import  csv
import simplejson
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  scipy import stats
from statsmodels.stats.diagnostic import lilliefors
count=0
arr=[]
def getDataNumInCSV(path):
    print(path)
    try:
        df=(pd.DataFrame(pd.read_csv(path)))
    except:
        return 0
    print(len(df))
    global count
    count+=len(df)
    #arr.append(len(df))
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
        arr.append(int(num))
        #print(num)
    return num

def getAllFile(path):
    for root,ds,fs in os.walk(path):
        for file in fs:
            if (file[-4:]=="json"):
                getCommentNumInJSON(os.path.join(root,file))
            else:
                getDataNumInCSV(os.path.join(root,file))

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
    #getAllFile(path1)
    #getAllFile(path2)
    #getAllFile(path3)
    getAllFile(path4)
    #getAllFile(path5)
    #getAllFile(path6)
    #getAllFile(path7)

def getDoubanDataNum():
    pass

#对目录下所有文件过滤
def FilterAllFile(path):
    for root,ds,fs in os.walk(path):
        for file in fs:
            if (file[-4:]=="json"):
                if (filterDataInJSON(os.path.join(root,file))):
                    pass


def FilterWeiboData(Min,Max):
    path1 = '大作业数据集合/微博数据/01'
    path2='大作业数据集合/微博数据/02'
    path3 = '大作业数据集合/微博数据/03'
    path4 = '大作业数据集合/微博数据/04'
    path5 = '大作业数据集合/微博数据/05'
    path6 = '大作业数据集合/微博数据/06'
    FilterAllFile(path1)
    FilterAllFile(path2)
    FilterAllFile(path3)
    FilterAllFile(path4)
    FilterAllFile(path5)
    FilterAllFile(path6)

#正态分析
def DataAnalyseByNormal(a):
    # print(np.mean(p))
    # print(np.std(p))
    # print(np.std(p,ddof=1))
    #print(a)
    print(stats.shapiro(a))
    print(stats.anderson(a,dist='norm'))
    print(stats.kstest(a, 'norm'))



def filterDataInJSON(path):
    pass


getBilibiliDataNum()
getWeiboDataNum()
getDoubanDataNum()
arr.sort()
p=np.array(arr)
print(len(p))
print(p)

m=np.mean(p)
std=np.std(p,ddof=1)
p=(p-np.mean(p))/np.std(p,ddof=1)
DataAnalyseByNormal(p)

print("上分位点="+str(stats.norm.isf(0.25,0,1)))
p2=np.array([])
for i in p:
    if (i<-stats.norm.isf(0.3,0,1)):
        p2=np.append(p2,i)
#print(p2)
#DataAnalyseByNormal(p2)
#FilterWeiboData(np.min(p2),np.max(p2))
print(count)

