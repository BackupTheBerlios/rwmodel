from __future__ import division

from datetime import datetime
import math

def calc_max_grid(I):
	maxm = 0
	minm = 1
	for x in xrange(MAX):
		for y in xrange(MAX):
			if I[x][y] > maxm:
				maxm = I[x][y]
			if I[x][y] < minm:
				minm = I[x][y]
	return (minm, maxm)


#P(O^0_(x,y)) foreach (x,y)
def occupancy_vs():
	oxy= (BigFloat(objects /float(X*Y))**(X*Y)) #an arbitrary prior 
	return oxy

def occupancy_vs_targets():
	oxy = BigFloat(targets /float(X*Y))
	return oxy**(X*Y)
	
#P(M^t)
def pmt(t):
	return 0.5 

#P(V^t_(x,y)|O^t_(x,y))
def observation_model(b,t, x, y):
	if O[b][t][x][y] == 0:
		return 0.1
	else:
		return 0.9

#P(O^t_(x,y)|M^t O^(t-1))
def dynamic_object_model(b,t, x, y):
	x_prev = gaze_position[b][t-1][0]
	y_prev = gaze_position[b][t-1][1]
	x_curr = gaze_position[b][t][0]
	y_curr = gaze_position[b][t][1]
	if x_curr == x_prev  and y_curr == y_prev:
		if O[b][t][x][y] == 1:
			return 0.95
		else:
			return 0.1
	else:
		return numpy.random.uniform() #0.5 
      

#P(O^t_(x,y)|T^t_i)
def target_observation_model(b,t,i,x,y):
	
	result =0.25/((dist_between_pos(targets_[b][t][i],(x,y))/0.02)**2 +1)#/0.02
	#return result
	if O[b][t][x][y] == 1:
		return 0.5+result
	else:
		return 0.5-result

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

def min_max_normal(I, I_T_flag):
	maxv = 0
	minv = 1
	L = len(I)
	for x in xrange(L):
		for y in xrange(L):
		val = I[x][y]
		if val > maxv:
			maxv = val
		if val < minv:
			minv = val
	print 'block', b
	print 'max', maxv
	print 'min', minv
	normal = abs(int(math.log10(maxv)))
	print 'normal', normal
	if normal > 1:
		for x in xrange(L):
			for y in xrange(L):
				I[x][y] *= 10**(normal)

				#eliminate small values if I_T flag is set 
				if I_T_flag:
					diff_ = abs(int(math.log10(I[x][y]))) -280
				if diff_ > 0:
					I[x][y] *= 10**diff_
	return (minv, maxv, normal)
  
  
