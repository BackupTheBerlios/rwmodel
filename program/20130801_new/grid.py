from __future__ import division
#-*- coding: utf-8 -*-
#! python
#name: gridmodule
#author: Erik Lux
#date: 20130615
#purpose: occupancy grid
import os
os.chdir('/home/luxe/Tracking/program/20130801_new')
import imp
imp.load_source('vars', 'var.py')
from vars import *
from datetime import datetime
from bigfloat import *
import math
#P(O^0_(x,y)) foreach (x,y)
def occupancy_vs():
  oxy= (BigFloat(objects /float(X*Y))**(X*Y)) #an arbitrary prior 
  return oxy

def occupancy_vs_targets():
  oxy = BigFloat(targets /float(X*Y))
  return oxy**(X*Y)
	
#P(M^t)
def pmt(t):
	return numpy.random.uniform()

#P(V^t_(x,y)|O^t_(x,y))
def observation_model(t, x, y):
	return  observation_matrix[V[t][x][y]][O[t][x][y]]

#P(O^t_(x,y)|M^t O^(t-1))
def dynamic_object_model(t, x, y):
  result = 0
  for x in xrange(X):
    for y in xrange(Y):
      result_partial = 0
      x_prev = gaze_position[t-1][0]
      y_prev = gaze_position[t-1][1]
      if x == x_prev  and y == y_prev:
        result_partial = transition_matrix[O[t][x][y]][O[t-1][x][y]]
      else:
        result_partial = numpy.random.uniform()
      result+= numpy.random.uniform()*result_partial
  result /= X*Y
      
      #print 'partial:', numpy.random.uniform()*result_partial, 'sum:', result

  return result

#d((x,y),T^t_i) distance between target and (x,y)
def distance(t,i,x,y):
  dx = abs(x - T[t][i][0])
  dy = abs(y - T[t][i][1])
  return math.sqrt(dx**2 + dy**2)

#P(O^t_(x,y)|T^t_i)
def target_observation_model(t,i,x,y):
  result =0.25/((distance(t,i,x,y)/0.02)**2 +1)
  if O[t][x][y] == 1:
    return 0.5+result
  else:
    return 0.5-result

#P(T^t_i|M^t O^t T^(t-1)_i)
def dynamic_target_model(t,i):
  set_size = 1 #size of set of polar positions
  result = 1
  for x in xrange(X):
    for y in xrange(Y):
      result *= target_observation_model(t,i, x,y)
  
  result *= set_size
  result /= (X*Y)
  
