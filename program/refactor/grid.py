import numpy
#definition of grid interface
class Grid:
	def __init__(self, time, blocks_size, anc_size=1, size=30, targ_size=4, dist_size=4):
		self.size = size
		self.X = size
		self.Y = size
		self.anc_size = anc_size
		self.blocks_size = blocks_size
		self.targ_size = targ_size;
		self.dist_size = dist_size;
		self.time = time
		
		self.O = [ [ [ [ 
					0 
					for x in xrange(Y) ]
						for y in xrange(X) ] 
							for t in xrange(time + 1) ]
								for b in xrange(blocks_size) ] 
		
		self.I= [ [ [ [
					numpy.random.uniform() 
					for x in xrange(Y)]
						for y in xrange(X) ]
							for t in xrange(time +1)]
								for b in xrange(blocks_size)]
		
		self.IT= [ [ [ [
					numpy.random.uniform()
						for x in xrange(Y)]
							for y in xrange(X)]
								for t in xrange(time +1)]
									for b in xrange(blocks_size)]
		
		self.targ = [ [ [ 
						(0,0)
							for i in xrange(targ_size) ] 
								for t in xrange(time+1) ] 
									for b in xrange(blocks_size)]
		self.dist  = [ [ [
						(0,0)
							for i in xrange(dist_size)] 
								for t in xrange(time+1) ] 
									for b in xrange(blocks_size)]
	
	
		
		self.gaze = [ [ 
						(0, 0)
							for t in xrange(time + 1)]
								for b in xrange(blocks_size)]
	
