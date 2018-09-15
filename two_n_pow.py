#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: two_n_pow.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-09-13 14:36:08
# @Last Modified: 2018-09-13 14:36:08
#

def solution(n):
    if n < 512 or n > 1024:
        return 0
    s = '134078079299425970995740249982058461274\
    7936582059239337772356144372176403007354697680187\
    4298166903427690031858186486050853753882811946569\
    946433649006084096'
    while n - 512 > 0:
        s = twoPow(s, 0)
        n -= 1

def twoPow(s, carry):
    if len(s) <= 9:
        return  str(int(s) * 2 + carry)
    max_int_input = str(int(s[-9:]) * 2 + carry)
    carry = 0
    if len(max_int_input) > 9:
        carry = 1
        max_int_input = max_int_input[1:]

    out_string =  twoPow(s[0:-9], carry)
    return out_string + max_int_input

if __name__ == "__main__":
  s = twoPow('12345678901234567890',0)
  print(s)
  pass
