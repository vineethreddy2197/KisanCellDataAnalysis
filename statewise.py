import pandas as pd
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import sys
import numpy
df = pd.read_csv("C:\\Users\\Vineeth\\Desktop\\lmao\\pan.csv")
weat1=df['StateName']=="MAHARASHTRA"
weat2=df['StateName']=="MADHYA PRADESH"
weat3=df['Sector']=="AGRICULTURE"
weat4=df['Sector']=="HORTICULTURE"
sys.__stdout__ = sys.stdout
c1=0
c2=0
c3=0
c4=0
for i in range(0,len(weat1)):
    if weat1[i]==True and weat3[i]==True:
        c1=c1+1
for j in range(0,len(weat2)):
    if weat1[j]==True and weat4[j]==True:
        c2=c2+1
for i in range(0,len(weat1)):
    if weat2[i]==True and weat3[i]==True:
        c3=c3+1
for j in range(0,len(weat2)):
    if weat2[j]==True and weat4[j]==True:
        c4=c4+1
coun1=[c1,c2]
coun2=[c3,c4]
bars1=('AGRI','HORTI')
bars2=('AGRI','HORTI')
plt1.bar(bars1,coun1)
plt1.ylabel('Count(MAHA)')
plt1.show()
plt2.bar(bars2,coun2)
plt2.ylabel('Count(MADHYA)')
plt2.show()
