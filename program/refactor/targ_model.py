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

#P(T^t_i|C^t)
def gaze_target_model(g, (x,y), t, i):
  g_x = g.gaze[0][t][0]
  g_y = g.gaze[0][t][1]
  result = math.exp( -(dist_between_pos((x,y), g.targ[0][t][i]))**2 / 0.25)
  result /=900
  return result

def set_min_arr(ar, m):
  L = len(ar)
  result = [[ar[x][y] for y in xrange(L)] for x in xrange(L)]
  for x in xrange(L):
    for y in xrange(L):
      if result[x][y] < m:
        result[x][y] = m
  return result

#probability of gaze position
def tm(self, show_traj):
  g = self.grid
  for t in range(2, g.time):#times -1
    temp = [[1 for x in xrange(g.X) ] for y in xrange(g.Y)]
    targ = [0,1,2,3]
    for ind in xrange(len(targ)):#targets
      i = targ[ind]
      GTM = [ [ 
				gaze_target_model(g, (x,y),t,i)
					for y in xrange(g.Y) ]
						for x in xrange(g.X)] 
      #temp =  mult_by_pos(GTM, temp, MAX)
      self.TM[t] = mult_by_pos(self.TM[t], g.IT_bit[0][i][t],g.size)
      self.TM[t] = mult_by_pos(self.TM[t], GTM, g.size)

    
    #TM[t] = root_by_pos(TM[t], len(targets_), MAX)
    self.TM[t] = mult_by_pos(self.TM[t], self.CM[t], g.size)
     
    (minm, maxm) = calc_max(self.TM[t])
     
    if show_traj:
      for x in xrange(g.size):
        for y in xrange(g.size):
          if self.TM[t][x][y] != maxm:
            self.TM[t][x][y] = 0
          else:
            self.TM_trajectory[t] = (x,y)
  return TM

