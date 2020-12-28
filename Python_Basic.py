#======
# Basic
#======

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


# import package
import numpy as np
import math
from math import radians

#==============
# data imporing
# 데이터 입력
#==============
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

# median
np.median(data)

# mean
np.mean(data)

# Standard Deviation
np.std(data)

# Corretation coefficient
# 상관계수
np.coef(data)

# 도움말
help(str)

# 데이터 구조확인
data.shape # R의 dim(data)과 같다



# replace 
data.replace("A", "a")


#==========
# Reference
#==========
# DataCamp / datacamp.com
# https://datascienceschool.net/view-notebook/04358acdcf3347fc989c4cfc0ef6121c