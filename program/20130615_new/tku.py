#-*- coding: utf-8 -*-
#! python
#name: target_knowledge_update
#author: Erik Lux
#date: 20130619
#purpose: incrementally update knowledge over targets
#modification: using my own class SmallFloat for working with very small or big probabilities probabilities

import imp
imp.load_source('grid', 'grid.py')

from grid import *
from datetime import datetime
from bigfloat import *

def tku():
  print 'Tku started ...'
  for t in range(2, times+1):
    suma1 = [Small(0) for i in xrange(targets)]
    suma2 = Small(0)
    for i in xrange(targets):
      mul1= Small(1)
      for x in xrange(X):
        for y in xrange(Y):
          mul1.init(I[t][x][y].m,I[t][x][y].e)
          mul1.mul(dynamic_target_model(t,i))
          suma1[i].add(mul1)
    for i in xrange(targets):   
      mul1.init(suma1[i].m, suma1[i].e)
      mul1.mul(I_T[t-1][i])
      suma2.add(mul1)
      I_T[t][i] = suma2

    print 't:', t, 'I_T[t][0]:', I_T[t][0]
    
