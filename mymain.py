import os
print('1->Crop Analysis')
print('2->Season Analysis')
print('3->Statewise Analysis')
print('4->Each State Analysis')
x=int(input('Enter : '))
if x==1:
    os.system('python crop.py')
elif x==2:
    os.system('python season.py')
elif x==3:
    os.system('python statewise.py')
else:
    os.system('python state.py')
