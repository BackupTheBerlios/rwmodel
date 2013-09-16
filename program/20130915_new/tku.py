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

"""
TODO heatmaps to depict inference in each timestamp
"""
def tku():
  print "Target knowledge update started ..."
  _start = time.time()
  for t in range(2, times+1):
    for i in xrange(targets):
      suma = Small(0)
      suma2 = Small(0)
      mul1= Small(1)
      mul2 = Small(1)
      
      for x in xrange(X):
        for y in xrange(Y):
          mul1.init(I[t][x][y].m,I[t][x][y].e)
          mul1.mul(dynamic_target_model(t,i))
          suma1.add(mul1)

      for j in xrange(targets):
        mul2.init(suma1[i].m, suma1[i].e)
        mul2.mul(I_T[t-1][i])
        suma2.add(mul1)
      I_T[t][i] = suma2
  print "Target knowledge update finished ..."
f = open('tku.out', 'w')
tku()
f.close()
