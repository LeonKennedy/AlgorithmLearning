#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: leastsquares.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 最小二乘法
# 对于样本数据的散点图形如函数y=ax2+bx+c的图像的数据， 在python中的拟合过程为
# @Create: 2018-03-07 15:42:30
# @Last Modified: 2018-03-07 15:42:30

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq



#Xi=np.array([1,2,3,4,5,6])
#Yi=np.array([9.1,18.3,32,47,69.5,94.8])
Xi=np.array([0,1,2,3,-1,-2,-3])
Yi=np.array([-1.21,1.9,3.2,10.3,2.2,3.71,8.7])

def func(p,x):
    a,b,c=p
    return a*x*x+b*x+c

def error(p, x, y):
    return func(p, x) - y

#初始的参数
p0 = [10,10,10]
para , count = leastsq(error, p0, args=(Xi, Yi))
# parameter ,  cost
# (array([ 2.06607141,  2.5975001 ,  4.68999985]), 1)
TY = np.array([ func(para, i) for i in Yi])
plt.scatter(Xi,Yi)
x=np.linspace(-5,5,1000)
y=np.array([ func(para,i) for i in x])
plt.plot(x,y)
plt.show()

