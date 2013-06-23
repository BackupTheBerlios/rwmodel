#-*- coding: utf-8 -*-
#! python
#name: object_knowledge_update
#author: Erik Lux
#date: 20130615
#purpose: incrementally update knowledge over the grid
#modification: using my own class SmallFloat for working with very small probabilities

#import imp
#mod = imp.load_source('grid', 'grid.py')

#from grid import *
from datetime import datetime
from bigfloat import *
def oku():
  result = 0
  print >> f, 'Oku started ...'
  for t in xrange(2,times+1):
    multiplicant = Small(1)
    multiplicant1 = Small(1)
    suma = Small(0)
#incremental phase
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      multiplicant.mul(I[t-1][xx][yy])
    print >>f, 'multiplicant', multiplicant.m, multiplicant.e
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      
      multiplicant1.init(multiplicant.m, multiplicant.e)
      multiplicant1.mul(dynamic_object_model(t,xx,yy))
      suma.add(multiplicant1)
      print >> f, 'mul1:', multiplicant1.m, multiplicant1.e
      print >>f, 'suma:', suma.m, suma.e
      
      #print 'dyn_obj_model:', dynamic_object_model(t,xx,yy)
    print >> f, 'suma', suma.m, suma.e
    x = gaze_position[t][0]
    y = gaze_position[t][1]
       
    for x in xrange(X):
      for y in xrange(Y):
        multiplicant1.init(suma.m, suma.e)
        multiplicant1.mul(observation_model(t,x,y))
        I[t][x][y] = multiplicant1
        
    
    print >>f, 't: ',t, I[t][x][y].m, I[t][x][y].e
  return result
      
  for x in xrange(X):
    for y in xrange(Y):
      print >>f, x,' ',y,' ', I[times][x][y].m, I[times][x][y].e

f = open('oku.out', 'w')
oku()
f.close()
