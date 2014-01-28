import serialize as sr
import math
import numpy
import sys
import scipy.stats

class Space:
	def __init__(self, scanpath, size, time, xystep = 1, tstep = 10):
		self.xystep = xystep
		self.tstep = tstep
		#size of binned trajectory xystep is 0.25deg, tstep is 10ms
		self.tsize = int(scanpath[len(scanpath)-1][2]) / tstep + 2
		#cm compare method 
		self.data = [ [ [
			0 
			for y in xrange(size) ]
				for x in xrange(size) ]
					for t in xrange(tsize) ]
		
		for t in xrange(time):
			time_in_ms = scanpath[1]
			tindex = int(round(time_in_ms,-1))
			x = scanpath[0][0]
			y = scanpath[0][1]
			self.data[x][y][tindex] +=1
		

class Nss:
	def __init__(self, grid):
		self.grid = grid
		self.blocks_size = grid.blocks_size
		self.dx = grid.size
		self.dy = grid.size
		self.time = grid.time
	
	def compute_nss(self, index):
		return 0
		
	
	def get_scanpath(self, index):
		scanpath = []
		for t in range(0, self.time):
			scanpath.append((self.grid.gaze[index][t], 
								float(self.grid.time_eye[index][t])))
		return scanpath
		
	def prepare_spaces(self):
		for b in xrange(self.blocks_size):
			scanpath = get_scanpath(b)
			space = Space(scanpath, self.size, self.time)
			sr.serialize(space, str(self.grid.track_id) + '_'
				+ str(self.grid.track_trials[b]) + '.ser')
				

def print_gaussian(g):
	tsize = len(g)
	xysize = len(g[0])
	for t in xrange(tsize):
		print t
		for x in xrange(xysize):
			for y in xrange(xysize):
				sys.stdout.write(str(g[t][x][y])+ ' ')
			print ''
			
				
def create_gaussian(xystep=1, tstep=1, xsd=1.2, ysd=1.2, tsd=2.65):
	xsd3 = int(math.ceil(3 * xsd / xystep) * xystep)
	ysd3 = int(math.ceil(3 * ysd / xystep) * xystep)
	tsd3 = int(math.ceil(3 * tsd / tstep) * tstep)
	
	xsize = xsd3*2+1
	ysize = ysd3*2+1
	tsize = tsd3*2+1
	
	g = [ [ [
		100*scipy.stats.norm(0, ysd).pdf(y-ysd3) \
			* scipy.stats.norm(0, xsd).pdf(x-xsd3) \
				* scipy.stats.norm(0, tsd).pdf(t-tsd3) 
		
		for y in xrange(ysize) ]
			for x in xrange(xsize) ]
				for t in xrange(tsize) ]
				
	
	
	return g
			
			
		
			
	
		

