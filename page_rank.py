#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: page_rank.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-05-28 18:48:34
# @Last Modified: 2018-05-28 18:48:34
#

import numpy as np

data = np.random.randint(0,2, (10,10)) 
print(data)

rank = np.ones(10).T * 1 /15
print(rank)
for i in range(100):
  rank = np.dot(data, rank)
print(rank)

