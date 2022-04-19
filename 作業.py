# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:23:55 2022

@author: AlenChang
"""
"""
homework(1)
終極密碼
1.未猜中時，需用猜數縮小範圍
2.限制遊玩次數10  (自己練習)

"""
import random  #亂數套件

ans = random.randint(1,100)  #亂數的範圍
cnt  = 0
start = 1
end1 =100

while True:    
    guess = int(input("請猜一個數:"))
    cnt += 1
    if cnt > 10:
        print ("你的次數已用完，你輸了!!!")
        break
    elif guess == ans and cnt <= 10 :
        print (ans,"恭喜答對")
        break
    elif guess > ans:
        end1 = guess
        print("請猜小一點",start,"~",end1)
    else:
        start = guess
        print("請猜大一點",start,"~",end1)
                
print("DONE")

"""
homework(2)
因數分解 (公式上網查)
輸入一數字，列出其因數乘法
ex:720 = 2*2*2*2*3*3*5
"""
# num = int(input("請輸入一個正整數:"))
# while num > 0:
#      for n in (2,num):
#          if num %n ==0:
#              num = num/n
#              print(n,sep="*",end="")
#              # if num > 1:
#              #     continue
#              # else:
#              #     break
    
# print("Done")

"""
homework(3)
有4個數，1,2,3,4  
能組成多少個互不相同的三位數?分別是多少?

"""
# num = [1,2,3,4]
# for i in range (num):
    



"""
homework(4)
有一個分數序列 => 2/1,3/2,5/3,8/5,13/8,21/13...
求此20項的和

"""






"""
homework(5)
印出

   *
  ***
 *****
*******
 *****
  ***
   *
   
"""








