import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
import sys
import time
import numpy
class myst:
    name=''
    x=0
    def __eq__(self, other):
        return self.name == other.name
start=time.time()
df = pd.read_csv("data.csv")
weat1=df['StateName']
end=time.time()
sys.__stdout__ = sys.stdout
arr=[]
for i in range(0,len(weat1)):
    v=myst()
    v.name=weat1[i]
    if v in arr :
        arr[arr.index(v)].x=arr[arr.index(v)].x+1
    else:
        arr.append(v)
c1=[w.x for w in arr]
c2=[z.name for z in arr]
print(end-start)
plt.rc('font', size=5)
plt.bar(c2,c1)
plt.xticks(rotation=90)
plt.show()
