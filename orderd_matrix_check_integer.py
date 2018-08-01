#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: orderd_matrix_check_integer.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:  给定一个N*M的整数矩阵，其中每行的元素是递增的，而每列元素递减。设计算法，判断整数x是否存在在矩阵中。
# @Create: 2018-08-01 17:29:16
# @Last Modified: 2018-08-01 17:29:16
#
import pdb  


def order_matrix_is_exist_integer(matrix, value):
  i = 0
  j = 0
  rows_count = len(matrix)
  if rows_count == 0 :
    return False
  columns_count = len(matrix[0])
  while i<columns_count and j<rows_count:
    if matrix[i][j] < value :
      j += 1
    elif matrix[i][j] == value:
      return True
    else:
      i += 1
  return False

if __name__ == "__main__":
  matrix = [
    [9, 18, 29],
    [7, 16, 17],
    [3, 5,  6]
  ]
  value = 6
  a = order_matrix_is_exist_integer([], value)
  print(a)
  
