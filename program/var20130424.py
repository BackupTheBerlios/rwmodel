#-*- coding: utf-8 -*-
#! python

#defines grid variables
objects = 2 #number of objects
times = 4 #number of timestamps
X = 2 #width of grid
Y = 3 #height of grid

#O[t][x][y]
O = [[[0 for x in xrange(Y)] for y in xrange(X)] for t in xrange(times+1)]#objects
#V[t][x][y]
V = [[[0 for x in xrange(Y)] for y in xrange(X)] for t in xrange(times+1)]#visual
#M[t]
M = [(0,0) for t in xrange(times+1)]#past eye movement information
#the inference over the whole grid
grid_inference = [[0 for x in xrange(Y)] for y in xrange(X)]

o1=0.1
o2=0.05

