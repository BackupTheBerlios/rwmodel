from __future__ import division 
#-*- coding: utf-8 -*-
#! python
#name: target_knowledge_update
#author: Erik Lux
#date: 20130619
#purpose: incrementally update knowledge over targets
#modification: using my own class SmallFloat for working with very small or big probabilities probabilities

#import imp
#imp.load_source('grid', 'grid.py')

#from grid import *
import time
from bigfloat import *
import math


def normalize(t):
  maxv = 0
  minv =1
  for x in xrange(X):
    for y in xrange(Y):
      val = I_T[t][x][y]
      if val > maxv:
        maxv = val
        if val < minv:
          minv = val
  print 'max', maxv
  print 'min', minv
  normal = abs(int(math.log10(maxv)))
  print 'normal', normal
  if normal > 5:
    print 'normalized ...'
    for x in xrange(X):
      for y in xrange(Y):
        I_T[t][x][y] *= 10**normal

def tku():
  print "Target knowledge update started ..."
  start_ = time.time()
  for t in range(2, 15):  #times+1
    print 'time is:' , t
    for x in xrange(X):
      for y in xrange(Y):
        (ant_size, xl, xr, yl, yr) = calc_antecedent_bounds(x,y)
        
        for i in xrange(targets):
          suma1 = 0
          suma2 = 0
          dyn_model = dynamic_target_model(t,i,xl,xr,yl,yr, ant_size)

          for j in range(xl, xr):
            for k in range(yl, yr):
              suma1 += (I[t][j][k]*dyn_model)
          suma1 /= (ant_size)

          suma2 += (suma1*I_T[t-1][x][y])
        suma2 /= targets
        I_T[t][x][y] = suma2

    normalize(t)

  end_ = time.time()
  print "Target knowledge update finished ..."
  print 'Elapsed time is ',(end_-start_)/60, 'minutes'

f = open('tku.out', 'w')
tku()
f.close()

