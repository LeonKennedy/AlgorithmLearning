#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: GibbsSampleing.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: Gibbs sampling 
# 吉布斯采样（英语：Gibbs sampling）是统计学中用于马尔科夫蒙特卡洛（MCMC）的一种算
# 法，用于在难以直接采样时从某一多变量概率分布中近似抽取样本序列。该序列可用于近似
# 联合分布、部分变量的边缘分布或计算积分（如某一变量的期望值）。某些变量可能为已知
# 变量，故对这些变量并不需要采样。
# 吉布斯采样常用于统计推断（尤其是贝叶斯推断）之中。这是一种随机化算法，与最大期望算法
# 等统计推断中的确定性算法相区别。与其他MCMC算法一样，吉布斯采样从马尔科夫链中抽取样本
# ，可以看作是Metropolis–Hastings算法的特例。
# 该算法的名称源于约西亚·威拉德·吉布斯，由斯图尔特·杰曼与唐纳德·杰曼兄弟于1984年提出。[1]
# @Create: 2019-02-21 15:24:37
# @Last Modified: 2019-02-21 15:24:37
#

import random, pdb
from collections import defaultdict
def roll_a_die():
    return random.choice([1,2,3,4,5,6])

def direct_sample():
    d1 = roll_a_die()
    d2 = roll_a_die()
    return d1, d1 + d2

def random_y_given_x(x):
    return x + roll_a_die()

def random_x_given_y(y):
    if y <= 7:
        return random.randrange(1,y)
    else:
        return random.randrange(y-6, 7)
        

def gibbs_sample(num_iter=100):
    x, y = 1, 2
    for _ in range(num_iter):
        x = random_x_given_y(y)
        y = random_y_given_x(x)
    return x, y

def compare_distributions(num_samples=1000):
    counts  = defaultdict(lambda: [0,0])
    for _ in range(num_samples):
        counts[gibbs_sample()][0] += 1
        counts[direct_sample()][1] += 1
    return counts

a = compare_distributions()
