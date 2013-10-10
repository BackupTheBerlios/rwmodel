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
from bigfloat import *
def oku():
  print "Object knowledge update started ...\n"
  _start = time.time()
  for t in xrange(2,5):    #!!!times+1
    #incremental phase
    print "Suma calculation started ...\n"
     
    for x in xrange(X):
      for y in xrange(Y):
        multiplicant = Small(1)
        multiplicant1 = Small(1)
        suma = Small(0)

        x1 = min(x-bound1, antecedent)
        x2 = min(bound2 -x, antecedent+1)
        y1 = min(y -bound1, antecedent)
        y2 = min(bound2 - y, antecedent+1)

        for j  in range(x-x1, x+x2):
          for i in range(y -y1, y+y2):
            multiplicant.mul(I[t-1][j][i])
            #I[t-1][j][i].p()
        #print "Multiplied inference from time ", t-1, ":"
        #multiplicant.p()
        for j in range(x-x1, x+x2):
          for i in range(y-y1, y+y2):
            multiplicant1.init(multiplicant.m, multiplicant.e)
            #multiplicant1.mul(dynamic_object_model(t,j, i))
            suma.add(multiplicant1)
          #print "Partial sum: "
           # suma.p()


        suma.mul(observation_model(t,x,y))
        suma.divide_by_int((x1+x2)*(y1+y2))
        I[t][x][y] = suma
    print "Time: ", t
    if t == times:
      for x in xrange(X):
        for y in xrange(Y):
          print "at position ", x,",", y,": \n"
          I[t][x][y].p()
  print "Object knowledge update successfully finished ..."
#f = open('oku.out', 'w')
oku()
#f.close()
