#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: unordered_string_comparsion.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 乱序字符串比对
# @Create: 2018-07-30 18:18:33
# @Last Modified: 2018-07-30 18:18:33
#

def comparison(str_a, str_b):
  if len(str_a) != len(str_b):
    return False
  hash_table = dict()
  for char in str_a:
    if char in hash_table:
      hash_table[char] += 1
    else:
      hash_table[char] = 1
  for char in str_b:
    if char in hash_table:
      hash_table[char] -= 1
      if hash_table[char] < 0:
        return False
    else:
      return False
  return True

if __name__ == "__main__":
  a = 's你好e'
  b = 'e好你s'
  print("%s and %s is same? %s" % (a,b,comparison(a,b)))

