from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: target_model
#author Erik Lux
#date: 20131017
#purpose: depict users gaze position 
#modified: file will be execed

import math
from const_model import * 

#targ_model contains all blocks
TM = [ [ [ 1 for y in xrange(Y) ] for x in xrange(X) ] for t in xrange(times+1) ]

#P(T^t_i|C^t)
def gaze_target_model((x,y), t, i):
  g_x = gaze_position[0][t][0]
  g_y = gaze_position[0][t][1]
  result = math.exp( -(dist_between_pos((x,y), targets_[0][t][i]))**2 / 0.25)
  result /=900
  return result

#P(T^t_i|C^t)
def gaze_target_model_pt((x,y),(x2,y2)) :
  result = math.exp( -(dist_between_pos((x,y),(x2,y2)))**2 / 0.25)
  return result/900



def set_min_arr(ar, m):
  L = len(ar)
  result = [[ar[x][y] for y in xrange(L)] for x in xrange(L)]
  for x in xrange(L):
    for y in xrange(L):
      if result[x][y] < m:
        result[x][y] = m
  return result

#probability of gaze position
def tm():
  MAX = 30
  #const
  #targ
  for t in range(2, times-1):#times -1
    temp = [[1 for y in xrange(MAX) ] for x in xrange(MAX)]
    targ = [0,1,2,3]
    for ind in xrange(len(targ)):#targets
      i = targ[ind]
      GTM = [[ gaze_target_model((x,y),t,i) for y in xrange(MAX) ] for x in xrange(MAX)] 
      #temp =  mult_by_pos(GTM, temp, MAX)
      TM[t] = mult_by_pos(TM[t], target_tib[0][i][t],MAX)
      TM[t] = mult_by_pos(TM[t], GTM, MAX)

    
    #TM[t] = root_by_pos(TM[t], len(targets_), MAX)
    TM[t] = mult_by_pos(TM[t], CM[t], MAX)
    
    (minm, maxm) = calc_max(TM[t])
    for x in xrnage(MAX):
      for y in xrange(MAX):
        if TM[t][x][y] != maxm:
          TM[t][x][y] = 0

  return TM

