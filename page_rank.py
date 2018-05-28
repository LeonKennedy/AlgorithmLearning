#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: page_rank.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-05-28 18:48:34
# @Last Modified: 2018-05-28 18:48:34
#

import numpy as np
import pdb

#网页数量
N = 15
# 平滑系数
a = 0.0001

data = np.random.randint(0,2, (N, N)) 
print('n 对 m 的指向数')
print(data)
data = data / np.sum(data, axis = 0)

print('去除指向自己')
for i in range(len(data)):
  data[i,i] = 0
data = data / np.sum(data, axis = 0)
print(data)


rank = np.ones(N).T * 1 / N
print(rank)
for i in range(10):
  temp = a / N * np.eye(N) + (1-a) * data
  rank = np.dot(a/N * np.eye(N) + (1 - a) * data, rank)
  print(rank)

