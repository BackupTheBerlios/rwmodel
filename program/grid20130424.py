#-*- coding: utf-8 -*-
#! python
import os
os.chdir('/home/luxe/Tracking/program')
import imp
mod = imp.load_source('vars', 'var20130424.py')
from vars import *
from datetime import datetime
import numpy

#P(O^0_(x,y)) foreach (x,y)
def occupancy_vs():
	oxy= objects /float(X*Y) #an arbitrary prior on the occupancy_vs
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
 			if x == x_prev && y == y_prev:
				result_partial = transition_matrix[O[t][x][y]][O[t-1][x][y]]
			else:
				result_partial = numpy.random.uniform()

			result = result + numpy.random.uniform()*result_partial

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
	result = 0
	t = times
	#for xrange(X):
		#for y in xrange(Y):
				


	end_ = datetime.now()
	print 'Elapsed time is ',(end_-start_).microseconds
	return result
	
