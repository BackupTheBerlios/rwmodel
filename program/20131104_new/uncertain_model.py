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

def calc_traj_dist(t1, t2):
  suma = 0
  count = 0
  for t in range(3,449):
    count = count+1
    suma += dist_between_pos(t1[t], t2[t])

  return suma/count
    


def um(TM, show_traj):
  UM =[[[ 0 for y in xrange(MAX)] for x in xrange(MAX)] for t in xrange(times+1)]
  UM_trajectory = [ (0,0) for t in xrange(times+1)]
  for t in range(3,times -1):
    print t
    arr = I[0][t]
    
    #domain specific code, remove if code changed
    
    for x in xrange(MAX):
      for y in xrange(MAX):
        if arr[x][y] > 0.0120:
          arr[x][y] = 0.0120 
    
    interval = calc_max(arr)
    print interval[0], interval[1]
    for x in xrange(MAX):
      for y in xrange(MAX):
        UM[t][x][y] = bd.pdf(map_int_to_int(interval, (0,1),arr[x][y]))*TM[t][x][y]
       
    (minm, maxm) = calc_max(UM[t])
    
    if show_traj:
      for x in xrange(MAX):
        for y in xrange(MAX):
          if UM[t][x][y] != maxm:
            UM[t][x][y] = 0
          else:
            UM_trajectory[t] = (x,y)

   #UM[t-2] = mult_by_pos(UM[t-2], TM[t], 30)
  return UM

