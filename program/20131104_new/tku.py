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

def tku(b):
  print "Target knowledge update started ..."
  start_ = time.time()
  target_i= [[[0 for x in xrange(Y)] for y in xrange(X)] for i in xrange(targets)]

  target_it = []
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
              suma1 += (target_observation_model(b,t,i,j,k)*I[b][t][j][k])
          suma1 /= ant_size
          target_i[i][x][y] = suma1
    target_it.append(target_i)
    print "over targets ..."

    for x in xrange(X):
      for y in xrange(Y):
        suma2 = 0
        for i in xrange(targets):
          suma2 += target_i[i][x][y]#*I_T[t-1][x][y]
        suma2 /=targets
        I_T[b][t][x][y] = suma2
    min_max_normal(I_T[b][t], True)#normalize(b,t)
  
  end_ = time.time()
  print "Target knowledge update finished ..."
  print 'Elapsed time is ',(end_-start_)/60, 'minutes'
  
  return target_it

f = open('tku.out', 'w')
target_itb = []
target_tib = [ [ [0 for t in xrange(times+1)] for i in xrange(targets)] for b in xrange(blocks)]

for b in xrange(blocks):
  target_itb.append(tku(b))

for b in xrange(blocks):
  for i in xrange(targets):
    for t in xrange(times+1):
      target_tib[b][i][t] = target_itb[b][t][i]

f.close()

