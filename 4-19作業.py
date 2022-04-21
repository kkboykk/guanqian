# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:30:52 2022

@author: AlenChang
"""

"""
homework(1)
請用for迴圈處理

data=[100,80,90,70,89,30,21,35]

請排序 -> 小到大
請排序 -> 大到小
"""
data=[80,100,90,70,89,30,21,35]
l_max = []
x = 0
z = 0

for i in range(8):
    for y in data:
        z = l_max.count(y)
        if z > 0:
            break
        elif y > x:
            x = y

   
    l_max.append(x)
    data.remove(x)
    x = 0
    
print(l_max)
print(l_max[-1:-9:-1])
"""
homework(2)
data=[10,20,30,25,50,60]

請反轉內容
-> [60,50,25,30,20,10]

"""
data=[10,20,30,25,50,60]
print(data[-1:-7:-1])



"""
homework(3)
巴斯卡三角形(6層)，請用一維串列處理
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
"""