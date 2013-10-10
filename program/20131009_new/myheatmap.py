from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
from Small import Small
import matplotlib.pyplot as plt
import numpy as np
import copy
import bigfloat
def print_heat(I,X, Y, time):
  minx = 1
  miny= 1
  maxx = 0
  maxy = 0

  maxv = Small(0)
  maxv.e = bigfloat.EMIN_MAX
  minv = Small(1)
  for x in xrange(X):
    for y in xrange(Y):
      val = I[time][x][y]
      if val.e <  maxv.e or (val.e == maxv.e and val.m > maxv.m):
        maxv.e = val.e
        maxv.m = val.m
   
      if val.e > minv.e or (val.e == minv.e and val.m < minv.m): 
        minv.e = val.e
        minv.m = val.m
      
  print 'max:', maxv.e
  print 'min:', minv.e
  
  interval_diff = minv.e - maxv.e
  print 'interval: ', interval_diff
  heat_array = [[0 for y in xrange(Y)] for x in xrange(X)]

  for x in xrange(X):
    for y in xrange(Y):
      tmp = I[time][x][y].e - minv.e
      
      heat_array[x][y] = float(-tmp /  interval_diff)
  
  return  heat_array 
  '''
  data = np.asarray(heat_array)
  heatmap = plt.pcolor(data)
  plt.colorbar(heatmap)
  plt.show()
  '''
'''
data = np.asarray(data)
heatmap = plt.pcolor(data)
plt.colorbar(heatmap)
plt.show()
'''
