import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy
df = pd.read_csv("C:\\Users\\Vineeth\\Desktop\\lmao\\pan.csv")
weat1=df['Season']=="RABI"
weat2=df['Season']=="KHARIF"
weat3=df['Season']=="JAYAD"
sys.__stdout__ = sys.stdout
c1=0
c2=0
c3=0
for i in range(0,len(weat1)):
    if weat1[i]==True:
        c1=c1+1
for j in range(0,len(weat2)):
    if weat2[j]==True:
        c2=c2+1
for k in range(0,len(weat3)):
    if weat3[k]==True:
        c3=c3+1
print(c1)
print(c2)
print(c3)
coun=[c1,c2,c3]
bars=('RABI','KHARIF','JAYAD')
plt.bar(bars,coun)
plt.ylabel('Count')
plt.show()
