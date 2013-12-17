import numpy
from kum import *

from const_model import *
from targ_model import *
from uncertain_model import *

#definition of grid interface
class Model:
	def __init__(self, grid):
		self.grid = grid
		
		self.CM = [ [ [ 
					0 
					for y in xrange(grid.X) ]
						for x in xrange(grid.Y) ]
							for t in xrange(grid.time+1) ]
							
		self.CM_traj = [ 
						(0,0)
							for t in xrange(grid.time+1) ]
		
  
		self.TM = [ [ [
					1
					for x in xrange(grid.X) ]
						for y in xrange(grid.Y) ]
							for t in xrange(grid.time+1) ]
		
		self.TM_traj = [ 
						(0,0)
							for t in xrange(grid.time+1) ]
		
		self.UM = [ [ [ 
					0
					for y in xrange(grid.X) ]
						for x in xrange(grid.Y) ]
							for t in xrange(grid.time+1) ]
  
		self.UM_traj = [
						(0,0)
						for t in xrange(grid.time+1) ]
						
		self.centroid_targets = [
								compute_centroid(grid.targ[0][t])
									for t in xrange(grid.time)]
									
		obj = [ 
				grid.targ[0][t]+ grid.dist[0][t]
					for t in xrange(grid.time)]

		self.centroid_objects = [
								compute_centroid(obj[t])
									for t in xrange(len(obj)) ]

		self.crowding_objects = [ 
								0 
									for t in xrange(grid.time)]
		
		min_v_default= 16*dist_between_pos((0,0), (29,29))
		min_arg_default = (0,0)
		min_v = min_v_default
		min_arg = min_arg_default

		for t in xrange(0, grid.time):
			for x in xrange(grid.X):
				for y in xrange(grid.Y):
					suma = 0
					for i in xrange(grid.targ_size):
						for d in xrange(grid.targ_size):
							suma += ( dist_between_pos ((x,y),
									grid.targ[0][t][i]) / dist_between_pos (grid.targ[0][t][i],grid.dist[0][t][i]) ) **2
					if suma < min_v:
						min_v = suma
						min_arg = (x,y)
								
			self.crowding_objects[t] = min_arg
			min_v = min_v_default
			min_arg = min_arg_default
			
		self.cm = cm
		
		self.tm = tm
		
		self.um = um
						
						
  

