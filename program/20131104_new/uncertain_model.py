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
param= 0.075
bd = beta(param, param)
  
#P(I^t_(x,y)|C^t piC)
def symetrical_beta_dist(p):
  return bd.pdf(p)

def symetrical_beta_dist_arr(ar):
  res = [ bd.pdf(i) for i in ar ]
  sequence  = zip(ar, res)
  d = {key: value for (key, value) in sequence}
  return d

#transforms grid of small probabilities to grid of it exps
def grid_to_exp(grid):
  return [[ int(math.log10(grid[x][y])) for y in xrange(X) ] for x in xrange(X)]

#transforms grid of small probabilities to grid of probabilities
def grid_to_prob(grid):
  grid = grid_to_exp(grid)
  max_val = -20
  min_val = 0
  for x in xrange(X):
    for y in xrange(Y):
      if grid[x][y]<min_val:
        min_val = grid[x][y]
      if grid[x][y] > max_val:
        max_val = grid[x][y]
  
  return [[ map_int_to_int((min_val, max_val),(0,1),grid[x][y]) for y in xrange(Y)] for x in xrange(X)]

def um(TM):
  UM = []
  for t in range(2, times-2):
    print t    
    UM.append([ [bd.pdf((dynamic_object_model(0,t,x,y)* dynamic_object_model(1,t,x,y) * dynamic_object_model(2,t,x,y)*dynamic_object_model(3,t,x,y) * dynamic_object_model(4,t,x,y))**(1/blocks)) for y in xrange(X) ] for x in xrange(X)])
    UM[t-2] = mult_by_pos(UM[t-2], TM[t], 30)
  return UM

