from __future__ import division

from scipy.stats import beta
from ku_methods import *

#targ_model contains all blocks
param=2 #2 
bd = beta(param, param)

def um(self):
	g = self.grid
  
	arr = [ [
			0
			for x in xrange(g.X) ]
				for y in xrange(g.Y) ] 
				
	for t in range(3,g.time):#times-1
		print t
		
		#domain specific code, remove if code changed
		
		for x in xrange(g.X):
			for y in xrange(g.Y):
				arr[x][y] = g.I[0][t][x][y]
				
    
		interval = calc_max_grid(arr)
		print interval[0], interval[1]
		for x in xrange(g.X):
			for y in xrange(g.Y):
				
				#domain specific code, remove if code changed
				self.M[t][x][y] = (map_int_to_int(
									interval, (0,1),arr[x][y])) #*g.TM.M[t][x][y]
									
				if self.M[t][x][y] > 0.020:
					self.M[t][x][y] = 0.020
				
				
				self.M[t][x][y] = bd.pdf(map_int_to_int((0,0.02), (0,1), self.M[t][x][y]))*g.TM.M[t][x][y]
				#domain specific code, remove if code changed
				
		(arg_min, arg_max) = calc_max_grid(self.M[t], flag_arg_max=True)
		
		self.M_traj[t] = arg_max
    
		

