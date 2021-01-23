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
    path1='大作业数据集合/B站数据/综合'
    getAllFile(path1)
    path2 = '大作业数据集合/B站数据/新冠'
    getAllFile(path2)

#获得所有目录下的微博信息
def getWeiboDataNum():
    path1 = '大作业数据集合/微博数据/Data/01'
    path2='大作业数据集合/微博数据/Data/02'
    path3 = '大作业数据集合/微博数据/Data/03'
    path4 = '大作业数据集合/微博数据/Data/04'
    path5 = '大作业数据集合/微博数据/05'
    path6 = '大作业数据集合/微博数据/06'
    path7 = '大作业数据集合/微博数据/07'
    path12='大作业数据集合/微博数据/BigData/12'
    getAllFile(path1)
    global arr
    print(len(arr))
    arr=[]
    getAllFile(path2)
    print(len(arr))
    arr = []
    getAllFile(path3)
    print(len(arr))
    arr = []
    #getAllFile(path12)
    getAllFile(path4)
    print(len(arr))
    arr = []
    #getAllFile(path5)
    #getAllFile(path6)
    #getAllFile(path7)

def getDoubanDataNum():
    pass

#getWeiboDataNum()
data=[896,1917,1920,1931]
plt.bar(['01','02','03','04'],data)
for i in range(0,4):
    plt.text(['01','02','03','04'][i],data[i]+20,str(data[i]))
plt.savefig('E:/大学学习资料/数据分析/样本容量')
plt.show()
print(count)