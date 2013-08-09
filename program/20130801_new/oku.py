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
import time
from bigfloat import *
def oku():
  print "Object knowledge update started ...\n"
  _start = time.time()
  for t in xrange(2,3):    #!!!times+1
    multiplicant = Small(1)
    multiplicant1 = Small(1)
    suma = Small(0)
#incremental phase
    print "Suma calculation started ...\n"
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      multiplicant.mul(I[t-1][xx][yy])
    for i in xrange(len(antecedent_cells[t])):
      xx = antecedent_cells[t][i][0]
      yy = antecedent_cells[t][i][1]
      
      multiplicant1.init(multiplicant.m, multiplicant.e)
      print "Inference from time", t-1, ":"
      multiplicant.p()
      multiplicant1.mul(dynamic_object_model(t,xx,yy))
      print "Old partial sum: "
      suma.p()
      suma.add(multiplicant1)
      print "Dynamic object model: ", dynamic_object_model(t,xx,yy)
      print "New partial sum:"
      suma.p()
    
    print "Multiplicantion calculation started ..."
    x = gaze_position[t][0]
    y = gaze_position[t][1]
       
    print "Inference of object knowledge update is ..."
    print "at time: ", t
    for x in xrange(X):
      for y in xrange(Y):
        multiplicant1.init(suma.m, suma.e)
        multiplicant1.mul(observation_model(t,x,y))
        multiplicant1.div_by_int((antecedent*2+1)**2)
        I[t][x][y] = multiplicant1
        if t == times:
          print "at position ", x,",", y,": \n"
          I[t][x][y].p()
    print "\n"
        
      
  print "Object knowledge update successfully finished ..."
f = open('oku.out', 'w')
oku()
f.close()
