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
  if normal > 1:
    print 'normalized ...'
    for x in xrange(X):
      for y in xrange(Y):
        I_T[t][x][y] *= 10**normal
        
        
        #eliminate very small values
        diff_ = abs(int(math.log10(I_T[t][x][y])))-280
        if diff_ > 0:
          I_T[t][x][y] *= 10**diff_
        

def tku():
  print "Target knowledge update started ..."
  start_ = time.time()
  target_i= [[[0 for x in xrange(Y)] for y in xrange(X)] for i in xrange(targets)]

  for t in range(2,times+1 ):  #times+1
    print 'time is:' , t
    for i in xrange(targets):
      for x in xrange(X):
        for y in xrange(Y):
          (ant_size, xl, xr, yl, yr) = calc_antecedent_bounds(x,y)
          suma1 = 0
          #dyn_model = dynamic_target_model(t,i,xl,xr,yl,yr, ant_size)

          for j in range(xl, xr):
            for k in range(yl, yr):
              suma1 += (target_observation_model(t,i,j,k)*I[t][j][k])
          suma1 /= ant_size
          target_i[i][x][y] = suma1
    print "over targets ..."

    for x in xrange(X):
      for y in xrange(Y):
        suma2 = 0
        for i in xrange(targets):
          suma2 += target_i[i][x][y]#*I_T[t-1][x][y]
        suma2 /=targets 
        I_T[t][x][y] = suma2
    normalize(t)
  
  end_ = time.time()
  print "Target knowledge update finished ..."
  print 'Elapsed time is ',(end_-start_)/60, 'minutes'

f = open('tku.out', 'w')
tku()
f.close()
