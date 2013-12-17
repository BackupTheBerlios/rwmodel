from __future__ import division

import math
import numpy
#kum = knowledge update methods

def dist_between_pos ((x1,y1), (x2,y2)):
	return math.sqrt(abs((x2-x1)/4)**2 + abs((y2-y1)/4)**2)
	
def roundto(angle, precision = 0.5):
	correction = 0.5 if angle > 0 else -0.5
	return int(angle / precision + correction) * precision
    
def calc_max_grid(I, flag_arg_max=False):
	size = len(I)
	max_val = 0
	arg_max_val = (0,0)
	min_val = 1
	arg_max_val = (0,0)
	
	for x in xrange(size):
		for y in xrange(size):
			if I[x][y] > max_val:
				max_val = I[x][y]
				arg_max_val = (x,y)
			if I[x][y] < min_val:
				min_val = I[x][y]
				arg_min_val = (x,y)
	if flag_arg_max == False:
		return (min_val, max_val)
	else:
		return (arg_min_val, arg_max_val)
	
def compute_centroid(points):
	x = 0
	y = 0
	for p in points:
		x += p[0]
		y += p[1]
	x /= len(points)
	y /= len(points)
	x = int(round(x,0))
	y = int(round(y,0))
		
	return (x,y)
	
def map_int_to_int ( (a, b), (c,d), X):
	return c + (((X-a) / (b-a)) *(d-c))

def map_dist_to_in (X):
	return map_int_to_int ((0,29), (0.5,1), X)

def map_out_to_prob (X):
	return map_int_to_int ((0,13), (0,1), X)

def mult_by_pos (ar1, ar2, MAX):
	return [ [ar1[x][y] * ar2[x][y] for y in xrange(MAX)] for x in xrange(MAX)]

def add_by_pos (ar1, ar2, MAX):
	return [[ar1[x][y] + ar2[x][y] for y in xrange(MAX)] for x in xrange(MAX)]

def div_by_pos (ar1, val, MAX):
	return [[ ar1[x][y]/4 for y in xrange(MAX) ] for x in xrange(MAX) ]

def root_by_pos(ar1, root, MAX):
	return [[ ar1[x][y]**(1/root) for y in xrange(MAX)] for x in xrange(MAX)] 


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
def observation_model(g, b,t, x, y):
	if g.O[b][t][x][y] == 0:
		return 0.1
	else:
		return 0.9

#P(O^t_(x,y)|M^t O^(t-1))
def dynamic_object_model(g,b,t, x, y):
	x_prev = g.gaze[b][t-1][0]
	y_prev = g.gaze[b][t-1][1]
	x_curr = g.gaze[b][t][0]
	y_curr = g.gaze[b][t][1]
	if x_curr == x_prev  and y_curr == y_prev:
		if g.O[b][t][x][y] == 1:
			return 0.95
		else:
			return 0.1
	else:
		return numpy.random.uniform() #0.5 
      

#P(O^t_(x,y)|T^t_i)
def target_observation_model(g,b,t,i,x,y):
	
	result =0.25/((dist_between_pos(g.targ[b][t][i],(x,y))/0.02)**2 +1)#/0.02
	return result
	if g.O[b][t][x][y] == 1:
		return 0.5+result
	else:
		return 0.5-result

def calc_antecedent_bounds(g, x,y):
	min_bound = 0
	max_bound = g.size
	x1 = min(x-min_bound, g.anc_size)
	x2 = min(max_bound -x, g.anc_size+1)
	y1 = min(y -min_bound, g.anc_size)
	y2 = min(max_bound - y, g.anc_size+1)

	ant_size = (x1+x2)*(y1+y2) #size of antecedent cells

	xl = x-int(x1)
	xr = x+int(x2)
	yl = y-int(y1)
	yr = y+int(y2)

	return (ant_size, xl, xr, yl, yr)

def min_max_normal(I, b, I_T_flag):
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
  
  
