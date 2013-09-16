#!/usr/bin/python
from Small import Small
import matplotlib.pyplot as plt
import numpy as np
import bigfloat
def print_heat(I,X, Y):
  minx = 1
  miny= 1
  maxx = 0
  maxy = 0

  time= 3

  maxv = Small(0)
  maxv.e = bigfloat.EMIN_MAX
  minv = Small(1)
  for x in xrange(X):
    for y in xrange(Y):
      val = I[time][x][y]
      if val.e <  maxv.e or (val.e == maxv.e and val.m > maxv.m):
        print 'a'
        maxv.e = val.e
        maxv.m = val.m
   
      
      if val.e > minv.e or (val.e == minv.e and val.m <  minv.m):
        print 'in'
        print x, y
        minv.e = val.e
        minv.m = val.m
      
  print 'max:'
  maxv.p()
  print 'min:'
  minv.p()


'''
data = np.asarray(data)
heatmap = plt.pcolor(data)
plt.colorbar(heatmap)
plt.show()
'''
