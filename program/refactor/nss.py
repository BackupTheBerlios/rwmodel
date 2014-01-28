import serialize as sr
import math
import numpy
import sys
import scipy.stats
import numpy as np
from pylab import *

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

class Space:
	def __init__(self,scanpath, size, time, xystep = 1, tstep = 10):
		self.xystep = xystep
		self.tstep = tstep
		self.xysize = size
		#size of binned trajectory xystep is 0.25deg, tstep is 10ms
		self.tsize = int(scanpath[len(scanpath)-1][2]) / tstep
		#cm compare method 
		self.data = [ [ [
			0 
			for y in xrange(self.xysize) ]
				for x in xrange(self.xysize) ]
					for t in xrange(self.tsize) ]
		
		self.datax = [ [ [
			0 
			for t in xrange(self.tsize) ]
				for y in xrange(self.xysize) ]
					for x in xrange(self.xysize) ]
					
		
		self.datay = [ [ [
			0 
			for t in xrange(self.tsize) ]
				for x in xrange(self.xysize) ]
					for y in xrange(self.xysize) ]
					
					
		
		self.scanpath = []
		
		t2=0
		xprev = 0
		yprev = 0
		for t in xrange(self.tsize):
			time_in_ms = scanpath[t2][2]
			tindex = int(math.floor(time_in_ms/10))
			
			if (tindex -t) > 1:
				self.scanpath.append((xprev, yprev, 1))
				#print tindex, ' ', x, ' ' , y, ' ', t, ' ', self.data[t][xprev][yprev]
				continue
			else:
				x = scanpath[t2][0]
				y = scanpath[t2][1]
				xprev = x
				yprev = y
				self.scanpath.append((x, y, 1))
				#print tindex, ' ', x, ' ' , y, ' ', t, ' ', self.data[t][x][y]
			t2+=1
			
			
			
		print('\n')
		print 'tsize', self.tsize
	
	def reindex(self):
		for t in xrange(self.tsize):
			for x in xrange(self.xysize):
				for y in xrange(self.xysize):
					self.datax[x][y][t] = self.data[t][x][y]
					self.datay[y][x][t] = self.data[t][x][y]
	
	def smooth(self,G):
		dt = len(G)/2
		dx = len(G[0])/2
		print 'dt', dt, 'dx', dx
		for t in xrange(self.tsize):
			x = self.scanpath[t][0]
			y = self.scanpath[t][1]
			print 't', t, 'x', x, 'y', y
			(lbx, ubx) = self.compute_bounds(x, self.xysize, dx)
			(lby, uby) = self.compute_bounds(y, self.xysize, dx)
			(lbt, ubt) = self.compute_bounds(t, self.tsize, dt)
			
			factor = self.scanpath[t][2]
			for tt in range(lbt, ubt):
				for xx in range(lbx, ubx):
					for yy in range(lby, uby):
						self.data[tt][xx][yy] += \
							factor * G [tt-lbt][xx-lbx][yy -lby]
							
	def show(self):
		tsize = len(self.data)
		xysize = len(self.data[0])
		for t in xrange(tsize):
			print t
			for x in xrange(self.xysize):
				for y in xrange(self.xysize):
					sys.stdout.write(str(self.data[t][x][y])+ ' ')
				print ''
			
		
	#ind - index
	#ubind upperbound for index
	#dind difference
	def compute_bounds(self, ind, ubind, dind):
		lb = max(0, ind - dind)
		ub = min(ubind, ind + dind +1)
		return (lb, ub)
		

class Nss:
	def __init__(self, grid):
		self.grid = grid
		self.size = grid.size
		self.blocks_size = grid.blocks_size
		self.dx = grid.size
		self.dy = grid.size
		self.time = grid.time
	
	def compute_nss(self, index):
		return 0
		
	
	def get_scanpath(self, index):
		scanpath = []
		for t in range(0, self.time):
			scanpath.append((self.grid.gaze[index][t][0],
								self.grid.gaze[index][t][1],
									float(self.grid.time_eye[index][t])))
		return scanpath
		
	def prepare_spaces(self):
		G = create_gaussian()
		
		for b in xrange(self.blocks_size):
			
			scanpath = self.get_scanpath(b)
			
			space = Space(scanpath, self.size, self.time)
			
			space.smooth(G)
			
			space.reindex()
			
			to_show = np.asarray(space.datax[14])
			plt.pcolor(to_show)
			plt.show()
			#sr.serialize(space, str(self.grid.track_id) + '_'
			#	+ str(self.grid.track_trials[b]) + '.ser')
				
	
				


			
			
		
			
	
		

