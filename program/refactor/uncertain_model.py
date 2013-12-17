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
param=2 #2 
bd = beta(param, param)

def um(self,TM, show_traj):
  g = self.grid
  
  for t in range(3,g.time):#times-1
    print t
    arr = g.I[0][t]
    
    #domain specific code, remove if code changed
    
    for x in xrange(g.X):
      for y in xrange(g.Y):
        if arr[x][y] > 0.0120:
          arr[x][y] = 0.0120 
    
    interval = calc_max(arr)
    print interval[0], interval[1]
    for x in xrange(g.X):
      for y in xrange(g.Y):
        self.UM[t][x][y] = bd.pdf(
						map_int_to_int(
									interval, (0,1),arr[x][y])) *self.TM[t][x][y]
       
    (minm, maxm) = calc_max(self.UM[t])
    
    if show_traj:
      for x in xrange(g.size):
        for y in xrange(g.size):
          if self.UM[t][x][y] != maxm:
            self.UM[t][x][y] = 0
          else:
            self.UM_trajectory[t] = (x,y)

   #UM[t-2] = mult_by_pos(UM[t-2], TM[t], 30)
  return self.UM

