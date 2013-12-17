import numpy
from ku_methods import *

from const_model import *
from targ_model import *
from uncertain_model import *

#definition of grid interface
class Abstract_model(object):
	def __init__(self, grid, ku_blocks_size):
		self.grid = grid
		self.ku_blocks_size = ku_blocks_size
		
		self.M = [ [ [ 
					0 
					for y in xrange(grid.X) ]
						for x in xrange(grid.Y) ]
							for t in xrange(grid.time+1) ]
							
		self.M_traj = [ 
						(0,0)
							for t in xrange(grid.time+1) ]
							
		
	
	def naive_strategy_traj(self):
		g = self.grid
		self.centroid_targets_traj = [
								compute_centroid(g.targ[0][t])
									for t in xrange(g.time)]
									
		obj = [ 
				g.targ[0][t]+ g.dist[0][t]
					for t in xrange(g.time)]

		self.centroid_objects_traj = [
								compute_centroid(obj[t])
									for t in xrange(len(obj)) ]

		self.crowding_objects_traj = [ 
								0 
									for t in xrange(g.time)]
		
		min_v_default= 16*dist_between_pos((0,0), (29,29))
		min_arg_default = (0,0)
		min_v = min_v_default
		min_arg = min_arg_default

		for t in xrange(0, g.time):
			for x in xrange(g.X):
				for y in xrange(g.Y):
					suma = 0
					for i in xrange(g.targ_size):
						for d in xrange(g.targ_size):
							suma += ( dist_between_pos ((x,y),
									g.targ[0][t][i]) / dist_between_pos (g.targ[0][t][i],g.dist[0][t][i]) ) **2
					if suma < min_v:
						min_v = suma
						min_arg = (x,y)
								
			self.crowding_objects_traj[t] = min_arg
			min_v = min_v_default
			min_arg = min_arg_default
			
	def compute(self):
		print 'Computing model ..'

class Model(Abstract_model):
	def __init__(self, grid, ku_blocks_size, compute_method):
		super(Model, self).__init__(grid, ku_blocks_size)
		self.compute = compute_method
		
	def compute(self):
		return self.compute()
	
		
						
						
  

