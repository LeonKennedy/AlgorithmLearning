#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: katz_backoff.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 描述Katz backoff 卡茨退避法
# @Create: 2018-05-25 21:53:24
# @Last Modified: 2018-05-25 21:53:24
#

import numpy as np

#data
corpus = np.random.randint(10,size=(25,20))
print('****** data dict *******')
print(corpus)
print('***** word frequence in a row *****')
word_frequence_matrix = list() 
for row in corpus:
  temp = [ np.count_nonzero(row==i) for i in range(10) ]
  word_frequence_matrix.append(temp)
word_frequence_row = np.array(word_frequence_matrix)
print(word_frequence_row)
print('***** word frequence in matrix *****')
word_frequence_matrix = np.array([ np.count_nonzero(corpus==i) for i in range(10)])
print(word_frequence_matrix)

def probability(x,y):
  count = 0
  for row in corpus:
    pre_word = row[0]
    for i in range(1,len(row)):
        if row[i] == y and pre_word == x:
          count += 1
        pre_word = row[i]
  return count / word_frequence_matrix[y]

def run(sentence):
  sentence_probability = word_frequence_matrix[sentence[0]] / np.sum(word_frequence_matrix)
  for word_index in range(1,len(sentence)):
    sentence_probability *= probability(sentence[word_index-1], sentence[word_index])
  print('句子 %s 的合理性 %f' % (str(sentence), sentence_probability))

test = np.random.randint(10,size=(4,5))
for i in test:
  run(i)
  



  
