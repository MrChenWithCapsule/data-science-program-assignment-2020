import simplejson
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  scipy import stats
from scipy.cluster.vq import kmeans,vq,whiten
#todo：
#SSE(簇内误方差)法
class SSECal:
    data=[]
    def addData(self,data):
        self.data.append(data)

    def SSE(self):
        result=np.array([])
        for i in range(1,16):
            distortion=np.array([])
            for j in self.data:
                p = whiten(j)
                # print(p)
                center, dis = kmeans(p, i)
                distortion=np.append(distortion,dis)
                # print(center)
            result=np.append(result,np.mean(distortion))
        plt.plot(result)
        plt.savefig('E:/大学学习资料/数据分析/Kmeans聚类结果评估')
        plt.show()
#todo:
#轮廓系数 检验



