#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: genetic.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 背包问题遗传算法
# @Create: 2018-11-17 15:53:16
# @Last Modified: 2018-11-17 15:53:16


import random, pdb
X = [
   [10, 15],
   [15, 25],
   [20, 35],
   [25, 45],
   [30, 55],
   [35, 70]
  ]


WEIGHT_LIMIT = 80
SELECT_NUMBER = 4
CHROMOSOME_SIZE = 6

def init():
  population = [
    '100110',
    '011010',
    '101010',
    '101101'
  ]
  return population


def fitnesses(population):
  fit = []
  for i in population:
    fit.append(fitness(i))
  return fit

def fitness(individual):
  weight = 0
  values = 0
  for i,v in enumerate(individual):
    if v == '1':
      weight += X[i][0]
      values += X[i][1]
  return (weight, values)

def filtor(population , fit):
  index = len(population) - 1
  while index >= 0:
    index -= 1
    if fit[index][0] > 80:
      fit.pop(index)
      population.pop(index)
    
def crossover(population):
  choices = random.choices(population, k=SELECT_NUMBER)
  temp = production(choices[0], choices[1])
  if temp not in population:
    population.append(temp)
  temp = production(choices[2], choices[3])
  if temp not in population:
    population.append(temp)

def production(a, b):
  pos =  random.choice(range(1, CHROMOSOME_SIZE -1))
  return a[:pos] + b[pos:]

  
  


if __name__ == "__main__":
  population = init()
  n = 100
  pdb.set_trace()
  while n > 0:
    n -= 1
    fit = fitnesses(population)
    filtor(population, fit)
    print('after filter:')
    print(population)
    print(fit)
    crossover(population)
    print('after crossover:')
    print(population)

