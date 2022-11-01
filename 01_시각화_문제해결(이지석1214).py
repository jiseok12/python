# -*- coding: utf-8 -*-
"""01_시각화_문제해결(이지석1214).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15wqRl4gWhEPouoNcy2W_Ina2JBFY7zqX

**해결 문제 01
<br>====================================================================
>지역평균기온 txt 파일을 읽어서 딕션너리 만들고, 아래와 같이 그래프를 표시하시오
"""

import matplotlib.pyplot as plt

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

plt.rc('font', family='NanumBarunGothic')

from google.colab import drive
drive.mount('/content/drive')

fp = open('/content/drive/MyDrive/Colab Notebooks/지역평균기온.txt','r',encoding = 'utf-8')
data = fp.readlines()
fp.close()
data

dt = {} #빈 딕셔너리만들기

for line in data:
  line = line.replace("\n", "")
  #print(line)
  items = line.split(',')
  #print(items)
  dt[items[0]] = int(items[1])
  
print(type(dt))
dt

x = list(dt.keys())
y = list(dt.values())
print(x)
print(y)

import matplotlib.pyplot as plt

plt.plot(x,y,'o--', color='skyblue')
plt.title('지역별 평균기온')
plt.xlabel('도시')
plt.ylabel('온도')

for i in range(0, len(x)):
  plt.text(i, y[i], y[i], ha = 'center')
plt.show()

#해당지역의 평균기온을 알려주는 프로그램을 추가하시오
#- 단 지역입력에 q가 입력되면, 종료

input=input()
value = 0
while True :
  if(x[value]==input):
    print(y[value])
    break
  else:
    value+=1