from __future__ import division

from scipy.stats import beta

#targ_model contains all blocks
param=2 #2 
bd = beta(param, param)

def um(model):
	g = model.grid
  
	for t in range(3,g.time):#times-1
		print t
		arr = g.I[0][t]
    
		#domain specific code, remove if code changed
		for x in xrange(g.X):
			for y in xrange(g.Y):
				if arr[x][y] > 0.0120:
					arr[x][y] = 0.0120 
    
		interval = calc_max(arr)
		print interval[0], interval[1]
		for x in xrange(g.X):
			for y in xrange(g.Y):
				model.M[t][x][y] = bd.pdf(
							map_int_to_int(
									interval, (0,1),arr[x][y])) *g.TM[t][x][y]
       
		(arg_min, arg_max) = calc_max_grid(model.M[t], flag_max_val=True)
		
		model.M_traj[t] = arg_min
    
		

