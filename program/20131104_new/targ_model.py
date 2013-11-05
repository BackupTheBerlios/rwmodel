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
  if result < 0.75:
    result += 0.25
  return result

#probability of gaze position
def tm():
  MAX = 30
  #const
  #targ
  for t in range(2, times-1):
    for i in xrange(targets):
      suma = [ [ 0 for y in xrange(MAX) ] for x in xrange(MAX)]
      for b in xrange(blocks):
        GTM = [[ gaze_target_model((x,y),t,i) for y in xrange(MAX) ] for x in xrange(MAX)] 
        temp = mult_by_pos(GTM, target_itb[b][t][i], MAX)
        suma = add_by_pos(suma, temp, MAX)
      
      suma = div_by_pos(suma, blocks, MAX)
      TM[t] = mult_by_pos(TM[t], suma, MAX)
    
    TM[t] = root_by_pos(TM[t], len(targets_), MAX)
    TM[t] = mult_by_pos(TM[t], CM[t], MAX)
  return TM

