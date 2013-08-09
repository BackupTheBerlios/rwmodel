#-*- coding: utf-8 -*-
#! python
#name: object_knowledge_update
#author: Erik Lux
#date: 20130615
#purpose: incrementally update knowledge over the grid
import imp
mod = imp.load_source('grid', 'grid.py')
from grid import *
from datetime import datetime
from bigfloat import *

def oku():
  result = 0
  for t in xrange(2,20):
    multiplicant = BigFloat(1)
    suma = BigFloat(0)
#incremental phase
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      multiplicant*=I[t-1][xx][yy]
      
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      suma += dynamic_object_model(t,xx,yy)*multiplicant
      #print 'suma:', multiplicant
      #print 'dyn_obj_model:', dynamic_object_model(t,xx,yy)
    x = gaze_position[t][0]
    y = gaze_position[t][1]
       
    for x in xrange(X):
      for y in xrange(Y):
        I[t][x][y] = observation_model(t,x,y)*suma
        
    
    print 't: ',t, 'I at gaze_position:',I[t][x][y]
  return result
      
'''  for x in xrange(X):
    for y in xrange(Y):
      print x,' ',y,' ', I[times][x][y]'''

