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

#targ_model contains all blocks
UM = []

#P(I^t_(x,y)|C^t piC)
def symetrical_beta_dist(t, x, y):
  result = 1
  param= 0.075
  
  if g_x == x and g_y == y:
    return beta.cdf(I_T,:0.075, 0.075)
  else:
    return numpy.random.uniform()
  return result
#probability of gaze position
def tm(TM):
  UM = TM
  for t in range(2, times+1):
    print 'time', t
    for x in xrange(X):
      for y in xrange(Y):
        UM[t][x][y] *= symetrical_beta_dist(t, x, y)
  
  return UM

