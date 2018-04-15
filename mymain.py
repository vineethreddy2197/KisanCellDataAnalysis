import os
print('1->Crop Analysis')
print('2->Season Analysis')
print('3->Statewise Analysis')
print('4->Each State Analysis')
print('5->Each Category Analysis')
print('6->Each Query Analysis')
print('7->Rainfall Analysis')
x=int(input('Enter : '))
if x==1:
    os.system('python crop.py')
elif x==2:
    os.system('python season.py')
elif x==3:
    os.system('python statewise.py')
elif x==4:
    os.system('python state.py')
elif x==5:
    os.system('python category.py')
elif x==6:
    os.system('python query.py')
else:
    os.system('python rainfall.py')
