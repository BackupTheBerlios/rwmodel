from __future__ import division

from scipy.stats import beta
import math

param =75
MAX = 30
bd = beta(param, param)
def map_int_to_int ( (a, b), (c,d), X):
  return c + (((X-a) / (b-a)) *(d-c))

def map_dist_to_in (X):
  return map_int_to_int ((0,29), (0.5,1), X)

def map_out_to_prob (X):
  return map_int_to_int ((0,13), (0,1), X)

def dirichlet_at_pos (dist):
  X = map_dist_to_in (dist)
  Y = bd.pdf(X)
  return map_out_to_prob(Y)

def dirichlet_at_grid((px,py)):
  grid = [[ 0 for x in xrange(MAX)] for y in xrange(MAX)]
  for x in xrange(MAX):
    for y in xrange(MAX):
      dist = dist_between_pos ((px, py), (x,y))
      grid[x][y] = dirichlet_at_pos(dist)
      if grid[x][y] < 0.85:
        grid[x][y] += 0.15
  return grid


#const_model contains all blocks
def cm(self, grid):
  
  for b in xrange(grid_blocks_size):
    (gx, gy) = grid.gaze[b][0]
    temp = dirichlet_at_grid((gx, gy))
    self.CM[0] = mult_by_pos (self.CM[0], temp, X)
  
  for t in range(1,grid.time):
      self.CM[t] = self.CM[t-1]
  return self.CM

