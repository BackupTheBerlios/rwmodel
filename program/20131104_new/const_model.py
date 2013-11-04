from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: constant_model
#author Erik Lux
#date: 20131017
#purpose: depict users gaze position 
#modified: file will be loaded

from scipy.stats import beta
import math

param = 25
MAX = 30
bd = beta(param, param)

def map_int_to_int ( (a, b), (c,d), X):
  return c + (((X-a) / (b-a)) *(d-c))

def map_dist_to_in (X):
  return map_int_to_int ((0,29), (0.5,1), X)

def map_out_to_prob (X):
  return map_int_to_int ((0,5.7), (0,1), X)

def dirichlet_at_pos (dist):
  X = map_dist_to_in (dist)
  Y = bd.pdf(X)
  return map_out_to_prob(Y)

def dist_between_pos ((x1,y1), (x2,y2)):
  return math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)

def dirichlet_at_grid((px,py)):
  grid = [[ 0 for x in xrange(MAX)] for y in xrange(MAX)]
  for x in xrange(MAX):
    for y in xrange(MAX):
      dist = dist_between_pos ((px, py), (x,y))
      grid[x][y] = dirichlet_at_pos(dist)
  return grid



#const_model contains all blocks
'''
CM = [ [ [ 0.01 for y in xrange(Y) ] for x in xrange(X) ] for t in xrange(times+1) ]
until var.py is fixed
'''
#probability of gaze position
'''
def cm():
  p = 1/blocks
  for b in xrange(blocks):
    (x, y) = gaze_position[b][0]
    for t in xrange(times+1):
      CM[t][x][y] += p
  return CM
'''
