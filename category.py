import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
import sys
import numpy
class myst:
    name=''
    x=0
    def __eq__(self, other):
        return self.name == other.name
df = pd.read_csv("C:\\Users\\Vineeth\\Desktop\\lmao\\pan.csv")
weat1=df['Category']
sys.__stdout__ = sys.stdout
arr=[]
for i in range(0,len(weat1)):
    v=myst()
    v.name=weat1[i]
    if v in arr :
        arr[arr.index(v)].x=arr[arr.index(v)].x+1
    else:
        arr.append(v)
        arr[arr.index(v)].x=arr[arr.index(v)].x+1
c1=[w.x for w in arr]
c2=[z.name for z in arr]
plt.rc('font', size=5)
plt.bar(c2,c1,align='center')
plt.xticks(rotation=30)
plt.show()
