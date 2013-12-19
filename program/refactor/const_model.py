from __future__ import division

from scipy.stats import beta
from ku_methods import *

param =75
bd = beta(param, param)


def dirichlet_at_pos (g,dist):
	X = map_dist_to_in (dist)
	Y = bd.pdf(g.X)
	return map_out_to_prob(g.Y)

def dirichlet_at_grid(g,(px,py)):
	grid = [[ 0 for x in xrange(g.X)] for y in xrange(g.Y)]
	for x in xrange(g.X):
		for y in xrange(g.Y):
			dist = dist_between_pos ((px, py), (x,y))
			grid[x][y] = dirichlet_at_pos(g,dist)
			if grid[x][y] < 0.85:
				grid[x][y] += 0.15
	return grid


#const_model contains all blocks
def cm(self):
	g = self.grid
  
	for b in xrange(self.ku_blocks_size):
		(gx, gy) = g.gaze[b][0]
		temp = dirichlet_at_grid(g,(gx, gy))
		self.M[0] = mult_by_pos (self.M[0], temp, g.size)
		
	for t in range(1,g.time):
		self.M[t] = self.M[t-1]
	
