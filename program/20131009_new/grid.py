from __future__ import division
#-*- coding: utf-8 -*-
#! python
#name: gridmodule
#author: Erik Lux
#date: 20130615
#purpose: occupancy grid
import os
os.chdir('/home/luxe/Tracking/program/20131009_new')
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
  if O[t][x][y] == 0:
    return 0.1
  else:
    return 0.9

#P(O^t_(x,y)|M^t O^(t-1))
def dynamic_object_model(t, x, y):
  x_prev = gaze_position[t-1][0]
  y_prev = gaze_position[t-1][1]
  x_curr = gaze_position[t][0]
  y_curr = gaze_position[t][1]
  if x_curr == x_prev  and y_curr == y_prev:
    if O[t][x][y] == 1:
      return 0.95
    else:
      return 0.1
  else:
    return numpy.random.uniform()
      

#d((x,y),T^t_i) distance between target and (x,y)
def distance(t,i,x,y):
  dx = abs(x - T[t][i][0])
  dy = abs(y - T[t][i][1])
  return math.sqrt(dx**2 + dy**2)

#P(O^t_(x,y)|T^t_i)
def target_observation_model(t,i,x,y):
  result =0.25/((distance(t,i,x,y)/0.02)**2 +1)#/0.02
  return result
  if O[t][x][y] == 1:
    return 0.5+result
  else:
    return 0.5-result

#P(T^t_i|M^t O^t T^(t-1)_i)
def dynamic_target_model(t,i,xl, xr, yl, yr, ant_size):
  result = 1
  for x in range(xl,xr):
    for y in xrange(yl,yr):
      result *= target_observation_model(t,i, x,y)

  result = result **(1/(ant_size))
  return result

def calc_antecedent_bounds(x,y):
  x1 = min(x-bound1, antecedent)
  x2 = min(bound2 -x, antecedent+1)
  y1 = min(y -bound1, antecedent)
  y2 = min(bound2 - y, antecedent+1)

  ant_size = (x1+x2)*(y1+y2) #size of antecedent cells

  xl = x-int(x1)
  xr = x+int(x2)
  yl = y-int(y1)
  yr = y+int(y2)

  return (ant_size, xl, xr, yl, yr)


