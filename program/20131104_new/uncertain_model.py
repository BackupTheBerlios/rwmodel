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
def symetrical_beta_dist(TM, t, x, y):
  param= 0.075
  
  for b in xrange(blocks):
    if (x,y) not in gaze_position[b][t]:
      continue
    else:
      return beta.cdf(TM[t][x][y],0.075, 0.075)
  return numpy.random.uniform()
#probability of gaze position
def um(TM):
  UM = TM
  for t in range(2, times+1):
    for x in xrange(X):
      for y in xrange(Y):
        UM[t][x][y] *= symetrical_beta_dist(TM, t, x, y)
  
  return UM

