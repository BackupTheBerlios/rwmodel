from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
from Small import Small
import matplotlib.pyplot as plt
import numpy as np
import copy
import bigfloat
def print_heat(I,X, Y, time):
  maxv =0
  minv =1
  for x in xrange(X):
    for y in xrange(Y):
      val = I[time][x][y]
      if val > maxv:
        maxv = val 
      if val < minv: 
        minv = val
      
  print 'max:', maxv
  print 'min:', minv
  
  interval_diff = maxv - minv
  print 'interval: ', interval_diff
  heat_array = [[0 for y in xrange(Y)] for x in xrange(X)]

  for x in xrange(X):
    for y in xrange(Y):
      tmp = I[time][x][y] - minv
      
      heat_array[x][y] = float(tmp /  interval_diff)
  
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
