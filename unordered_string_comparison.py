#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: unordered_string_comparsion.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 乱序字符串比对
# @Create: 2018-07-30 18:18:33
# @Last Modified: 2018-07-30 18:18:33
#
import random, string

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


def shuffler(data):
  temp = [i for i in data]
  random.shuffle(temp)
  return ''.join(temp)

def unit_test():
  chinese = '飞机房间的身份'
  str_a = ''.join(random.sample(string.ascii_letters + string.digits + chinese, 8))
  str_b = shuffler(str_a)
  str_c = ''.join(random.sample(string.ascii_letters + string.digits + chinese, 8))
  print("(string a)%s" % str_a)
  print("(string b)%s" % str_b)
  assert comparison('','')
  assert comparison(str_a,str_b)
  assert not comparison(str_a,str_c)

if __name__ == "__main__":
  #print("%s and %s is same? %s" % (a,b,comparison(a,b)))
  unit_test()

