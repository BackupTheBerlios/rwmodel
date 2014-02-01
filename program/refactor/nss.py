import serialize as sr
import math
import numpy
import sys
import scipy.stats
import numpy as np
from pylab import *

def online_variance(data):
	tsize = len(data)
	xysize = len(data[0])
	mean = float(0)
	mymean = float(0)
	mysize = tsize*xysize*xysize
	M2 = float(0)
	n = 0

	for t in xrange(tsize):
		for x in xrange(xysize):
			for y in xrange(xysize):
				n = n + 1
				delta = data[t][x][y] - mean
				mean = mean + delta/n
				M2 = M2 + delta*(data[t][x][y]-mean)
				
				mymean +=data[t][x][y]

	mymean /= mysize
	print 'm2', M2, 'mean', mean, 'mymean', mymean
	sd = math.sqrt((M2/(n-1)))
	return (mean,sd)

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
	def __init__(self,size, scanpath = [], xystep = 1, tstep = 10):
		self.xystep = xystep
		self.tstep = tstep
		self.xysize = size
		#size of binned trajectory xystep is 0.25deg, tstep is 10ms
		self.tsize = 5000
		#self.tsize = int(scanpath[len(scanpath)-1][2])
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
		
		#bin trajectory if scanpath
		if len(scanpath)!=0:
			t2=0
			xprev = 0
			yprev = 0
			for t in xrange(self.tsize):
				#print 't', t, 't2', t2
				time_in_ms = scanpath[t2][2]
				tindex = int(math.floor(time_in_ms))
				
				if (tindex -t) > 1:
					#self.scanpath.append((xprev, yprev, 1))
					#self.data[t][xprev][yprev] +=1
					#print tindex, ' ', x, ' ' , y, ' ', t, ' ', self.data[t][xprev][yprev]
					continue
				else:
					x = scanpath[t2][0]
					y = scanpath[t2][1]
					xprev = x
					yprev = y
					self.scanpath.append((x, y, tindex,1))
					self.data[t][x][y] +=1
					#print '1'
					#print tindex, ' ', x, ' ' , y, ' ', t, ' ', self.data[t][x][y]
				t2+=1
			
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
		#print 'dt', dt, 'dx', dx
		for t in xrange(len(self.scanpath)):
			sx = self.scanpath[t][0]
			sy = self.scanpath[t][1]
			st = self.scanpath[t][2]
			#print 't', st, 'x', sx, 'y', sy
			(lbx, ubx) = self.compute_bounds(sx, self.xysize, dx)
			(lby, uby) = self.compute_bounds(sy, self.xysize, dx)
			(lbt, ubt) = self.compute_bounds(st, self.tsize, dt)
			
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
		
	def normalize(self):
		(mean,sd) = online_variance(self.data)
		for t in xrange(self.tsize):
			for x in xrange(self.xysize):
				for y in xrange(self.xysize):
					self.data[t][x][y] = (self.data[t][x][y] - mean) / sd
		
		

class Nss:
	def __init__(self, grid):
		self.grid = grid
		self.size = grid.size
		self.blocks_size = grid.blocks_size
		self.dx = grid.size
		self.dy = grid.size
		self.time = grid.time
	
	def compute_nss(self, index= 0, flag_model= True):
		result = []
		for index in xrange(self.blocks_size):
			scanpath = []
			if(flag_model == False):
				scanpath = self.get_scanpath_from_trial_traj(index)
			else:
				scanpath = self.get_scanpath_from_model_traj(self.grid.TM.M_traj)
				
			nss_space = Space(self.size, scanpath)
			print 'Nss space'
			
			gaussian_space = self.compute_nss_subroutine(index, flag_model)
			print 'Gaussian space'
			
			suma = 0
			for t in xrange(nss_space.tsize):
				for x in xrange(nss_space.xysize):
					for y in xrange(nss_space.xysize):
						suma += nss_space.data[t][x][y] * gaussian_space.data[t][x][y]
			
			print 'Result'
			
			result.append((suma / nss_space.tsize))
		
		for r in result:
			print r
	
	def compute_nss_subroutine(self, index, flag_model = True):
		
		s = Space(self.size)
		G = create_gaussian()
		
		for b in xrange(self.blocks_size):
			print 'b', b
			scanpath = []
			if b != index:
				scanpath = self.get_scanpath_from_trial_traj(b)
			
				space = Space(self.size, scanpath)
				#space.show()
				space.smooth(G)
				
				#add to s space
				print 'Add to space'
				for t in xrange(s.tsize):
					for x in xrange(s.xysize):
						for y in xrange(s.xysize):
							s.data[t][x][y] += space.data[t][x][y]
							
							
		s.normalize()
		
		return s
		
	
	def get_scanpath_from_trial_traj(self, index):
		scanpath = []
		for t in range(0, self.time):
			scanpath.append( (self.grid.gaze[index][t][0],
								self.grid.gaze[index][t][1],
									float(self.grid.time_eye[index][t])) )
		return scanpath
	
	def get_scanpath_from_model_traj(self,M_traj):
		#index eye time for the first trial
		index = 0
		scanpath = []
		for t in range(0, self.time):
			scanpath.append( (M_traj[t][0],
								M_traj[t][1],
									float(self.grid.time_eye[index][t])) )
		return scanpath
		
		
	def prepare_spaces(self):
		G = create_gaussian()
		
		for b in xrange(self.blocks_size):
			
			scanpath = self.get_scanpath_from_trial_traj(b)
			if  len(scanpath) == 0:
				print 'Zero scanpath'
			
			space = Space(self.size, scanpath)
			
			(mean,sd) = online_variance(space.data)
			print 'mean', mean, 'sd', sd
			
			space.smooth(G)
			
			#space.reindex()
			
			
			#to_show = np.asarray(space.datax[14])
			#plt.pcolor(to_show)
			#plt.show()
			#sr.serialize(space, str(self.grid.track_id) + '_'
			#	+ str(self.grid.track_trials[b]) + '.ser')
				
	
				


			
			
		
			
	
		

