# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:05:18 2022

@author: AlenChang
"""

"""
HomeWork
#甚麼時候要使用必殺技，一次扣50HP
#甚麼時候要補血?當HP小於多少可以補或不補
#可以用亂數來決定1~20。亂數值為10或20才使用。

"""


from WarriorRole import Warrior
from TamerRole import Tamer
from DancerRole import Dancer


import random 

role = list()

for i in range(2):
    num = int(input("請選擇角色。1.武士，2訓獸師，3.舞者:"))
    name = input("請輸入角色姓名:")
    if num == 1:
        role.append(Warrior(name,120,0,1))     
    elif num == 2 :
        role.append(Tamer(name,100,0,1))
    else:
        role.append(Dancer(name,90,0,1))
        if i == 0:
            Dancer1 = id(role[0])
        else:
            Dancer2 = id(role[1])
        

        
while (role[0].gethp() > 0) and (role[1].gethp() > 0):
    attack = random.randint(1,100)
    if attack % 2==0:
        print(role[0].getName(),end="")
        if role[0].getmp() == 50:
            role[0].deathblow()
            role[1].subhp(50)
            print(role[1].getName(),"的血量減少50，還剩:",role[1].gethp())
            role[0].submp(50)
            cu =  random.randint(1,20)
            if role[1].gethp() < 50 and role[1].gethp() > 0 and cu % 10 ==0 and (Dancer1 != None or Dancer2 != None):
                role[1].cure()
                role[1].addhp(30)
        else:
            role[0].fight()
            role[1].subhp(10)  
            print(role[1].getName(),"的血量減少10，還剩:",role[1].gethp())
            role[0].addmp(10)
            cu =  random.randint(1,20)
            if role[1].gethp() < 50 and role[1].gethp() > 0 and cu % 10 ==0 and (Dancer1 != None or Dancer2 != None):
                role[1].cure()
                role[1].addhp(30)
    else:
        print(role[1].getName(),end="")
        if role[1].getmp() == 50:
            role[1].deathblow()
            role[0].subhp(50)
            print(role[0].getName(),"的血量減少50，還剩:",role[0].gethp())
            role[1].submp(50)
            cu =  random.randint(1,20)
            if role[0].gethp() < 50 and  role[0].gethp() > 0 and cu % 10 ==0 and (Dancer1 != None or Dancer2 != None):
                role[0].cure()
                role[0].addhp(30)
        else:
            role[1].fight()
            role[0].subhp(10)
            print(role[0].getName(),"的血量減少10，還剩:",role[0].gethp())
            role[1].addmp(10)
            cu =  random.randint(1,20)
            if role[0].gethp() < 50 and  role[0].gethp() > 0 and cu % 10 ==0 and (Dancer1 != None or Dancer2 != None):
                role[0].cure()
                role[0].addhp(30)
        
print("-"*30)
if role[0].gethp() > 0:
    print(role[0].getName(),"WIN!")
else:
    print(role[1].getName(),"WIN!")
    
    
"""
HomeWork
#甚麼時候要使用必殺技，一次扣50HP
#甚麼時候要補血?當HP小於多少可以補或不補
#可以用亂數來決定1~20。亂數值為10或20才使用。

"""
    