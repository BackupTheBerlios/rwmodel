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

def um(TM):
  UM = TM
  for t in range(2, 50):#times+1):
    print t
    UM[t] =  [ [symetrical_beta_dist(I[0][t][x][y]) for y in xrange(X) ] for x in xrange(X)]
  
  return UM

