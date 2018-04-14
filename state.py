import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy
df = pd.read_csv("C:\\Users\\Vineeth\\Desktop\\lmao\\pan.csv")
weat1=df['StateName']=="MAHARASHTRA"
weat2=df['StateName']=="MADHYA PRADESH"
sys.__stdout__ = sys.stdout
c1=0
c2=0
for i in range(0,len(weat1)):
    if weat1[i]==True:
        c1=c1+1
for j in range(0,len(weat2)):
    if weat2[j]==True:
        c2=c2+1
print(c1)
print(c2)
coun=[c1,c2]
bars=('Maha','Madhya')
plt.bar(bars,coun)
plt.ylabel('Count')
plt.show()
