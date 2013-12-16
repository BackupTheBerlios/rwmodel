import numpy
#definition of grid interface
class Model:
	def __init__(self, size, time):
		self.size = size
		self.X = size
		self.Y = size
		self.time = time
		
		self.CM = [ [ [ 
					0 
					for y in xrange(Y) ]
						for x in xrange(X) ]
							for t in xrange(time+1) ]
		
  
		self.TM = [ [ [
					1
					for y in xrange(Y) ]
						for x in xrange(X) ]
							for t in xrange(time+1) ]
		
		self.TM_traj = [ 
						(0,0)
							for t in xrange(time+1) ]
		
		self.UM = [ [ [ 
					0
					for y in xrange(MAX) ]
						for x in xrange(MAX) ]
							for t in xrange(times+1) ]
  
		self.UM_traj = [
						(0,0)
						for t in xrange(times+1) ]
  

