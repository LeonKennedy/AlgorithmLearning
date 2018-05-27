#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: katz_backoff.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 描述Katz backoff 卡茨退避法
# @Create: 2018-05-25 21:53:24
# @Last Modified: 2018-05-25 21:53:24
#

import numpy as np
import pdb

#data
word_size = 15
T = 28 # 8-10
corpus = np.random.randint(word_size,size=(25,20))
print('****** data dict *******')
print(corpus)
print('***** word frequence in a row *****')
word_frequence_matrix = list() 
for row in corpus:
  temp = [ np.count_nonzero(row==i) for i in range(word_size) ]
  word_frequence_matrix.append(temp)
word_frequence_row = np.array(word_frequence_matrix)
print(word_frequence_row)
print('***** word frequence in matrix *****')
word_frequence_matrix = np.array([ np.count_nonzero(corpus==i) for i in range(word_size)])
print(word_frequence_matrix)

def frequence(x):
  if x >= word_size:
    return 0
  return np.count_nonzero(corpus==x) 

def katz_frequence(x):
  unseen = 1
  if x >= word_size:
    unseen = 4
    # x -> x+1
    x = np.random.choice(T)
    pdb.set_trace()
  cou = np.count_nonzero(corpus==x) 
  if cou < T:
    # N = r * n  
    # r ~ d  = (r+1) Nr+1  /N
    zinf = 1 / 3

    return int((cou+1) * zinf) / unseen
  else:
    return cou

def probability(x,y, f):
  count = 0
  for row in corpus:
    pre_word = row[0]
    for i in range(1,len(row)):
        if row[i] == y and pre_word == x:
          count += 1
        pre_word = row[i]
  return  count / f(y) if f(y) else 0 

def run(sentence, f):
  sentence_probability = f(sentence[0]) / np.sum(word_frequence_matrix)
  for word_index in range(1,len(sentence)):
    sentence_probability *= probability(sentence[word_index-1], sentence[word_index], frequence)
  print('句子 %s 的合理性 %f ( %f )' % (str(sentence), sentence_probability, 1000000*sentence_probability))

test = np.random.randint(10,size=(5,3))
for i in test:
  run(i, frequence)
  
print('以上是基础模型,如果计算的词并没有出现在语料语料库里就会出现问题')
sent = [12,3,35]
run(sent, frequence)
sent = [4,13,35]
run(sent, frequence)

print('使用katz backoff 后')
for i in test:
  run(i, katz_frequence)
sent = [12,3,35]
run(sent, katz_frequence)
sent = [4,13,35]
run(sent, katz_frequence)


  
