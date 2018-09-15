#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: bb.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:  查找int数组中不同的数
# @Create: 2018-09-13 15:26:00
# @Last Modified: 2018-09-13 15:26:00
#

def count(l):
    m = 0; n = len(l) - 1;
    negative = 0
    if l[m] >= 0 or l[n] <=0:
        return len(l)
    while 1:
        if l[m] >= 0 :
            return negative + len(l) - m
        if -l[m] > l[n]:
            negative += 1
            m += 1
        elif -l[m] == l[n]:
            m += 1
        else:
            n -= 1


if __name__ == "__main__":
    l = [-5,-3, 1,3,4,5,7]
    l = [-100, -12,-3, 100]
    print(count(l))


            
            
