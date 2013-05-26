#-*- coding: utf-8 -*-
#! python
#name: gridmodule
#author: Erik Lux
#date: 20130424
#purpose: occupancy grid
import os
os.chdir('/home/luxe/Tracking/program')
import imp
mod = imp.load_source('vars', 'var20130520.py')
from vars import *
from datetime import datetime

#P(O^0_(x,y)) foreach (x,y)
def occupancy_vs():
	oxy= objects /float(X*Y) #an arbitrary prior on the occupancy_vs
	return oxy**(X*Y)

def occupancy_vs_targets():
  oxy = targets /float(X*Y)
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

			result = result + numpy.random.uniform()*result_partial
	return result

#d((x,y),T^t_i) distance between target and (x,y)
def distance(t,i,x,y):
  return 1

#P(O^t_(x,y)|T^t_i)
def target_observation_model(t,i,x,y):
  result =0.25/((distance(t,i,x,y)/0.02)**2 +1)
  if O[t][x][y] == 1:
    return 0.5+result
  else:
    return 0.5-result

#P(T^t_i|M^t O^t T^(t-1)_i)
def dynamic_target_model(t,i):
  setsize = 1 #size of set of polar positions
  result = 1
  for x in xrange(X):
    for y in xrange(Y):
      result *= target_observation_model(t,i, x,y)

  return result * setsize

#P(OVMT)
def joint_distribution_targets():
  start_= datetime.now()

  result = 1
  for t in range(1,times+1):
    
    result1 = 1
    for x in xrange(X):
      for y in xrange(Y):
        result1 *=(observation_model(t,x,y)
					*dynamic_object_model(t,x,y))		
    result2 = 1
    for i in xrange(targets):
      result2 *= dynamic_target_model(t,i)
    result *= (result1*result2*pmt(t)) 
  
  result *=(occupancy_vs_targets()*occupancy_vs())
  end_ = datetime.now()
  print 'Elapsed time: ', (end_-start_).microseconds
  return result

#P(OVM)
def joint_distribution():
	start_ = datetime.now()
	result2 =1 
	for t in range(1,times+1):
		
		result= 1
		for x in xrange(X):
			for y in xrange(Y):
				result = result * ( observation_model(t,x,y)
					*dynamic_object_model(t,x,y))		
		result2 = result2 * pmt(t) * result 
		
	result2 = occupancy_vs()*result2
	end_ = datetime.now()
	print 'Elapsed time is ',(end_-start_).microseconds
	return result2

#P(O^t|V^(1->t) M^(1->t)
def knowledge_update():
  start_ = datetime.now()
  t = times
  for x in xrange(X):
    for y in xrange(Y):
      grid_inference[x][y] = knowledge_update_recursive(t,x,y)
      end_ = datetime.now()
      print 'Elapsed time is ',(end_-start_).microseconds

def knowledge_update_recursive(t,x,y):
	#P(O^1_(x,y)|V^1 M^1) value at the end of recursion
	result = 1
	if t != 2:
		for i in xrange(len(antecedent_cells[t])):
			result = result*\
			knowledge_update_recursive(t-1,antecedent_cells[t][i][0],antecedent_cells[t][i][1])
		
	result2 = 0
	for i in xrange(len(antecedent_cells[t])):
		result2 = result2+\
		dynamic_object_model(t, antecedent_cells[t][i][0], antecedent_cells[t][i][1])*result
	
	result2 = result2*observation_model(t,x,y)
	#print "Result2:", result2
	return result2

def knowledge_update_incremental():
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
