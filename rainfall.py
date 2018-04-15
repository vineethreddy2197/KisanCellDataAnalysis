import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy
import time
class myst:
    name=''
    x=0
    def __eq__(self, other):
        return self.name == other.name
start=time.time()
df = pd.read_csv("data.csv")
weat1=df['BlockName']
weat2=df['KCCAns']
end=time.time()
sys.__stdout__ = sys.stdout
arr=[]
for i in range(0,len(weat1)):
    v=myst()
    v.name=weat1[i]
    if str(weat2[i]).find("no")!=-1 and str(weat2[i]).find("rain")!=-1 :
        if v in arr:
            arr[arr.index(v)].x=arr[arr.index(v)].x+1
        else :
            arr.append(v)
            arr[arr.index(v)].x=arr[arr.index(v)].x+1
c1=[w.x for w in arr]
c2=[z.name for z in arr]
plt.rc('font', size=5)
plt.bar(c2,c1,align='center')
plt.ylabel('Count')
print(end-start)
plt.show()
