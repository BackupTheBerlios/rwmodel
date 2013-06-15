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
  for t in xrange(2,times+1):
    x = gaze_position[t][0]
    y = gaze_position[t][1]
    multiplicant = 1
    suma = 0
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      multiplicant*=I[t-1][xx][yy]
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      suma += dynamic_object_model(t,xx,yy)*multiplicant
       
    I[t][x][y] = observation_model(t,x,y)*suma
    result = I[t][x][y]
    print 't: ',t
    print 'result: ', result

  return result
