#======
# Basic
#======

# 복잡한 데이터 분석에 특화
# NumPy와 달리 복잡한 데이터 타입 처리 가능

#==================
# Python Data Type
#==================

float # real numbers
int # integer numbers
str # string, text
bool # True, False

# install package
Numpy
get-pip.py
python3 get-pip.p
pip install numpy


# import library
import pandas as pd
from pandas import Series, DataFrame # Series 1차원 # DataFrame 2차원 배열데이터 구조로 사용 

import numpy as np # numpy

import math
from math import radians

#==============
# data imporing
# 데이터 입력
#==============

data = pd.Series(["A", 1, "B", 2, "C", 3, "D", 4])

data = ["A", 1, "B", 2, "C", 3, "D", 4]
data

# print
# 조회하기
print(data)

# type
type(data)

# index
index()
data.index(data)

# count, 갯수 세기
count()

data.count(data)

#
# 도움말
help(str)

# 데이터 구조확인
data.shape # R의 dim(data)과 같다


# replace 
data.replace("A", "a")

# is null
pd.isnull(data)
# 값이 null 이면 True, 아니면 False를 반환한다


# 2차원 행렬 설정
pd.DataFrame(data, columns = ['col1', 'col2'])


# DataFrame 만들기
data = Series([1,2,3], index['a','b','c'])
print(data)

# index정렬하기 sorting

#    row 기준 오름차순 
print(data.sort_index())

# column 기준 오름차순
print(data.sort_index(axis= 1))


# row 기준 내림차순 
print(data.sort_index(ascending = False))

# column 기준 내림차순
print(data.sort_index(axis= 1,ascending = False))

# 객체 기준 정렬 오름차순
print(data.sort_values(by = 'a')) # by 컬럼명

# 복합 객체 기준 정렬 오름차순
print(data.sort_values(by = ['a', 'b'])) # by 컬럼명

# 순위 기준 정렬 - 동점자 처리 - 공동 처리
print(data.rank())

# 순위 기준 정렬 - 동점자 처리 - 데이터 순서 내림차순 상위 처리
print(data.rank(method = 'first'))

# 순위 기준 정렬 - 동점자 처리 - 공동 처리 
print(data.rank(ascending = False))

# 순위 기준 정렬 - 동점자 처리 - 공동 처리 
print(data.rank(method = 'first',ascending = False))

# 중복 색인은 허용됨.

#=========
# 기술 통계
#=========

# column 합계 / NA는 제외
print(data.sum)

# row합계 행의 합계 구하기
print(data.sum(axis = 1))

# 누적 column 합계 / NA는 제외
print(data.cumsum)

# 유니크 값 확인하기
print(data.unique())

# 분포 수를 계산 
print(data.value_counts())

# 수치가 들어있는 확인 # TRUE, FALSE 반환
data.isin(['a', 'b'])

# NaN(Not a Number) 결측치  확인 # TRUE, FALSE 반환
print(data.isnull())

# NA 처리 dropna 함수
print(data.dropna()) # 한개의 NA만 row에 포함되어 있더라도 해당 row 전체 제외함.
print(data.dropna(how = 'all')) # row 전체가 na일 경우 w제외함

# NA 처리 0으로 처리하기
print(data.fillna(0))

# NA 처리 앞에 값으로  처리하기
print(data.fillna(method = 'ffill')) # NA 값은 모두 앞의 값으로 가져와서 NA 처리 하는 경우
print(data.fillna(method = 'ffill', limit = 1)) # 1번만 앞에 값으로 처리하고 그 이후는 NA로 처리할 경우


# NA 처리 평균 값으로  처리하기
print(data.fillna(data.mean())) # 평균 값 


# null  값 제외한 값만 확인하기
print(data[data.notnull()])

# 기간 데이터 생성 (날짜)
pd.date_range(start = '2020-01-01', end = '2020-01-07')
pd.date_range(start = '2020/01/01', end = '2020/01/07')
pd.date_range(start = '2020-01-01', periods = 7)

pd.date_range(start = '2020-01-01', periods = 7, freq = 'W') # 주간
pd.date_range(start = '2020-01-01', periods = 7, freq = '2BM') # 달 마지막 날짜
pd.date_range(start = '2020-01-01', periods = 7, freq = 'QA') # 분기 날짜

# 데이터 프레임 만들기
pd.DataFrame([[1,2,3] , [4,5,6], [7,8,9]])

# 데이터 프레임 일부 데이터 조회 - head, tail
DataFrame_data.head([n])
DataFrame_data.tail([n])


# 데이터 프레임 일부 데이터 조회 - 열 
DataFrame_data[1:10]


# 데이터 프레임 일부 데이터 조회 - 행
DataFrame_data.loc[index_name]
DataFrame_data.loc[col1 : col3]

# columns 조회
data.columns

# index 조회
data.index

# values 조회
data.values

# 행열 바꾸기 Transform
DataFrame_data.T


# 데이터 결합 하기 - 세로
data.append(data2)
data.append(data2, ignore_index = TRUE) # index 무시하고 결합 할 경우


# 데이터 결합 하기 - 가로
data.join(data2)

# 특정열 기준으로 결합하기
data.merge(data2)
data3 = pd.merge(data,data2)
data.merge(data2, how = 'left', on = 'col1')
data.merge(data2, how = 'right', on = 'col1')
data.merge(data2, how = 'outer', on = 'col1')
data.merge(data2, how = 'inner', on = 'col1')

# 데이터 가져오기
data = pd.read.csv(file_name [,options])
data = pd.read.csv('c:/data.csv')
data = pd.read.csv('c:/data.csv' ,encoding = "cp949", sep = ",")

# 데이터 내보내기
data = pd.to.csv('c:/data.csv')
data = pd.to.csv('c:/data.csv', sep = " " , encoding = "cp949")



# 시각화
data.plot()
data.plot(grid = True) # 그리드 추가
plt.show()

# 바 차트 
plot = data.plot.bar(grid = True)
plot.set_xlabel("X-")
plot.set_ylabel("Y-")
plot.set_title("TITLE")

#==========
# Reference
#==========
# 김도형 / 김도형의 데이터 사이언스 스쿨 - 수학 편 / https://datascienceschool.net/view-notebook/04358acdcf3347fc989c4cfc0ef6121c
# 김정일 / 인공지능(AI) 프로그래밍_Machine Learning(머신러닝) 기초(파이썬 라이브러리 numpy, pandas)