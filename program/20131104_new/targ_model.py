from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: target_model
#author Erik Lux
#date: 20131017
#purpose: depict users gaze position 
#modified: file will be execed

import math

#targ_model contains all blocks
TM = [ [ [ 1e-28 for y in xrange(Y) ] for x in xrange(X) ] for t in xrange(times+1) ]

#P(T^t_i|C^t)
def gaze_target_model(b, t,i):
  g_x = gaze_position[b][t][0]
  g_y = gaze_position[b][t][1]
  result = math.exp( -( distance(b, t, i,g_x, g_y)**2 / 0.25) )
  if result < 0.75:
    result += 0.25
  return result

#probability of gaze position
def tm():
  p = 1/blocks
  #const
  for b in xrange(blocks):
    for t in xrange(times+1):
      (x, y) = gaze_position[b][t]
      TM[t][x][y] += p
  
  #targ
  for b in xrange(blocks):
    for t in range(2, times+1):
      for x in xrange(X):
        for y in xrange(Y):
          TM[t][x][y] *= (I_T[b][t][x][y] * gaze_target_model(b, t, i))
  return TM

