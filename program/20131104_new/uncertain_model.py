from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: uncertain_model
#author Erik Lux
#date: 20131017
#purpose: depict users gaze position 
#modified: file will be execed

import math
import numpy
from scipy.stats import beta
from const_model import *
#targ_model contains all blocks
UM = []
MAX = 30
param= 2
bd = beta(param, param)

ar = [[ 0 for x in xrange(X)] for y in xrange(Y)]

def calc_max(I):
  maxm = 0
  minm = 1
  for x in xrange(MAX):
    for y in xrange(MAX):
      if I[x][y] > maxm:
        maxm = I[x][y]
      if I[x][y] < minm:
        minm = I[x][y]
  return (minm, maxm)

def gen_exp_ar(I):
  for x in xrange(X):
    for y in xrange(Y):
      ar[x][y] = int(math.log10(I[x][y]))
  return  ar 


def um(TM):
  UM =[[[ 0 for y in xrange(MAX)] for x in xrange(MAX)] for t in xrange(times+1)] 
  for t in range(2,times -1):
    print t
    arr = gen_exp_ar(I[0][t])
    interval = calc_max(arr)
    for x in xrange(MAX):
      for y in xrange(MAX):
        UM[t][x][y] = bd.pdf(map_int_to_int(interval, (0,1), arr[x][y]))
        '''
        if I[0][t][x][y] > 0.011:
          UM[t][x][y] = 0.9
        else:
          UM[t][x][y] = I[0][t][x][y]
        '''
    #UM[t-2] = mult_by_pos(UM[t-2], TM[t], 30)
  return UM

