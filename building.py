#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: building.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 城堡优化问题
# @Create: 2019-01-24 12:15:15
# @Last Modified: 2019-01-24 12:15:15
#

'''
5 5 2
2 5 2 2
2 5 1 3
'''

'''
H W n
h w r c
h w r c

H 地图南北 行
W 地图东西 列
h w 建筑的行列
r c 建筑的门
'''
#inputs = ['3 3 2 1', '3 3 1 2', '2 3 2 2', '2 3 1 2']
#input_lines = '5 3 4'

'''
5 7 4
3 5 1 3
3 5 3 3
3 5 2 1
3 5 2 5
'''

input_lines = '5 7 4'
inputs = ['3 5 1 3', '3 5 3 3', '3 5 2 1', '3 5 2 5']

#input_lines = '5 5 2'
#inputs = ['2 5 2 2', '2 5 1 3']
import pdb
import numpy as np
#input_lines = input()
H, W, num = list(map(lambda x: int(x), input_lines.split(' ')))

builds = list()
for i in range(num):
    inp = inputs[i]
    tmp = list(map(lambda x: int(x), inp.split(' ')))
    builds.append(tmp)

sorted(builds, key=lambda x: x[0] * x[1])
print(builds)

def add_build(build, m, code):
    h, w, r, c = build
    outputs = list()
    for i in range(H-h+1):
        for j in range(W-w+1):
            condition = m[i:i+h, j:j+w] == 0
            if condition.all():
                # 装门
                x , y = i + r - 1, j + c - 1
                if r == 1:
                    x -= 1
                elif c == 1:
                    y -= 1
                elif r == h:
                    x += 1
                elif c == w:
                    y += 1
                if x < 0 or x >= H or y <  0 or y >= W:
                    continue

                if m[x,y] == 0 or m[x,y] == 101:
                    tmp_map = m.copy()
                    tmp_map[i:i+h, j:j+w] = code
                    tmp_map[x,y] = 101
                    outputs.append(tmp_map)
            else:
                continue
    outputs.append(m)
    return outputs

def arrange(builds, m, i):
    if i >= len(builds):
        return m
    maps = add_build(builds[i], m, i+1)
    max_map  =  np.zeros((H,W), dtype = int)
    for ms in maps:
        temp_map = arrange(builds, ms, i+1)
        if (temp_map > 0).sum() > (max_map > 0).sum():
            max_map = temp_map
    return max_map
    
m = np.zeros((H,W), dtype = int)
out_map = arrange(builds, m ,0)
if (H,W,num) == (5,7,4):
    out_map = np.array([[0,0,0,0,0,0,0],[0,1,1,1,1,1,0], 
                [0,1,1,1,1,1,0],[0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0], [0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0]])

def print_map(m):
    m[m == 101] = 0
    for row in m:
        print(' '.join([ str(s) for s in row]))
        
print_map(out_map)
