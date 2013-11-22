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

param = 100
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

def dist_between_pos ((x1,y1), (x2,y2)):
  return math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)

def mult_by_pos (ar1, ar2, MAX):
  return [ [ar1[x][y] * ar2[x][y] for y in xrange(MAX)] for x in xrange(MAX)]

def add_by_pos (ar1, ar2, MAX):
  return [[ar1[x][y] + ar2[x][y] for y in xrange(MAX)] for x in xrange(MAX)]

def div_by_pos (ar1, val, MAX):
  return [[ ar1[x][y]/4 for y in xrange(MAX) ] for x in xrange(MAX) ]

def root_by_pos(ar1, root, MAX):
  return [[ ar1[x][y]**(1/root) for y in xrange(MAX)] for x in xrange(MAX)] 

def dirichlet_at_grid((px,py)):
  grid = [[ 0 for x in xrange(MAX)] for y in xrange(MAX)]
  for x in xrange(MAX):
    for y in xrange(MAX):
      dist = dist_between_pos ((px, py), (x,y))
      grid[x][y] = dirichlet_at_pos(dist)
      if grid[x][y] < 0.85:
        grid[x][y] += 0.15
  return grid


def compute_centroid(points):
  x = 0
  y = 0
  for p in points:
    x += p[0]
    y += p[1]
  x /= len(points)
  y /= len(points)
  x = int(round(x,0))
  y = int(round(y,0))
  
  return (x,y)


centroid_targets = [ compute_centroid(targets_[0][t]) for t in xrange(len(targets_[0]))]
objects_ = [ targets_[0][t]+ distractors_[0][t] for t in xrange(len(targets_[0]))]
centroid_objects = [ compute_centroid(objects_[t]) for t in xrange(len(objects_)) ]

crowding_objects = [ 0 for t in xrange(len(targets_[0]))]

min_v_default= 16*dist_between_pos((0,0), (29,29))
min_arg_default = (0,0)
min_v = min_v_default
min_arg = min_arg_default

for t in xrange(0, times):
  for x in xrange(MAX):
    for y in xrange(MAX):
      
      suma = 0
      for i in xrange(targets):
        for d in xrange(targets):
          suma += ( dist_between_pos ((x,y), targets_[0][t][i]) / dist_between_pos (targets_[0][t][i],distractors_[0][t][i]) ) **2
      
      if suma < min_v:
        min_v = suma
        min_arg = (x,y)

  crowding_objects[t] = min_arg
  min_v = min_v_default
  min_arg = min_arg_default
  
#const_model contains all blocks

#probability of gaze position

def cm():
  CM = [ [ [ 1 for y in xrange(Y) ] for x in xrange(X) ] for t in xrange(times+1) ]
  
  for b in xrange(blocks):
    (gx, gy) = gaze_position[b][0]
    temp = dirichlet_at_grid((gx, gy))
    CM[0] = mult_by_pos (CM[0], temp, X)
  
  for t in range(1,times+1):
      CM[t] = CM[t-1]
  return CM

def cm_alldiff():
  CM = [ [ [ 1 for y in xrange(Y) ] for x in xrange(X) ] for t in xrange(times+1) ]
  
  for t in range(1, times-1):
    print t
    for b in xrange(blocks):
      (gx, gy) = gaze_position[b][t]
      temp = dirichlet_at_grid((gx, gy))
      CM[t] = mult_by_pos (CM[t], temp, X)
  
  return CM

