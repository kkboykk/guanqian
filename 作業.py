# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:03:57 2022

@author: AlenChang
"""

#ctrl+!  全選註解
"""
homework(1)
1
22
333
4444
55555 

"""
for a in range (1,6):     #[1,2,3,4,5,6]
    for x in range (a):
            print(a,end="")
    print()

"""
homework(2)
55555
4444
333
22
1

"""
for a in range (5,0,-1):     #[1,2,3,4,5,6]
    for x in range (a):
        print(a,end="")
    print()

"""
homework(3)
9999999999
7777777
55555
333
1

"""
for a in range (9,0,-2):     #[1,2,3,4,5,6]
    for x in range (a):
        print(a,end="")
    print()

"""
homework(4)
求質數 :可以被1及自己整除的數
請輸出1~100間的質數有哪些

"""

for i in range(2,101):
    x=0
    for j in range(1,i+1):
        if i%j==0:
            x+=1
    if x==2:
        print (i,"是質數")
    
    