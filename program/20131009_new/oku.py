from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: object_knowledge_update
#author: Erik Lux
#date: 20130615
#purpose: incrementally update knowledge over the grid
#modification: using my own class SmallFloat for working with very small probabilities

#import imp
#mod = imp.load_source('grid', 'grid.py')

#from grid import *
import time

def normalize(t):
  maxv = 0
  minv = 1
  for x in xrange(X):
    for y in xrange(Y):
      val = I[t][x][y]
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
        I[t][x][y] *= 10**normal

def oku():
  print "Object knowledge update started ...\n"
  _start = time.time()
  for t in xrange(2,times+1):    #!!!times+1
    #incremental phase
    print "Suma calculation started ...\n"
    
    tmp1 = 1 
    for i in xrange(X):
      for j in xrange(Y):
        tmp1 *= I[t-1][i][j]
        tmp1 = tmp1**(1/X*Y)

    suma = 0
    for x in xrange(X):
      for y in xrange(Y):
        tmp2=1 

        for i in xrange(X):
          for j in xrange(Y):
	    tmp2= tmp1
            tmp2 *= dynamic_object_model(t,i, j)
            suma += tmp2 
        suma *= observation_model(t,x,y)
        suma /= X*Y
        I[t][x][y] = suma
    
    normalize(t)
    print "Time: ", t
  print "Object knowledge update successfully finished ..."
#f = open('oku.out', 'w')
oku()
#f.close()
