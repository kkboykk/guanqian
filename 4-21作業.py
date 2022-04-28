# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:19:40 2022

@author: AlenChang
"""

"""
homework(1)
抓取新北市 ubike資料，請依區別來村放ubike資料。

區別使用串列存。(sarea)
ex:[蘆洲區,三重區,.....]

由使用者輸入區別
area = input("請輸入查詢區別:")


系統要顯示該區別的所有站別+可借+可停  資訊

"""
import json    #解析json格式用
import requests  #用上網抓取資料用

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=10000000"

data = requests.get(url)   #是stream 串流資料 bytes 位元組

bike = data.text  #將串流資料轉換成文字檔

content = json.loads(bike) #將文字格式代入轉成 json格式  
#content = json格式

area = []
cnt = 0
for row in content:
    if area.count(row["sarea"]) > 0:
        continue
    else:
        area.append(row["sarea"])
        
#print(area)  #先不顯示

ans = input("請輸入欲查詢區域:")

if ans in area:
    for row in content:
        if ans == row["sarea"]:
            print("地點:",row["sna"])
            print("地址:",row["ar"])
            print("可借數:",row["sbi"])
            print("可停數:",row["bemp"])
            cnt += 1
        else:
            continue
else:
    print("該區域還未有YouBike服務，謝謝!")

print()
print("共查出{}筆資訊".format(cnt))
