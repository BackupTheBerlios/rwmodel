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

#gaze position through the experiment
gaze_position = [(0,0) for t in xrange(times+1)]

#the inference over the whole grid
grid_inference = [[0 for x in xrange(Y)] for y in xrange(X)]

#in the representation model, observation model
o1=0.9
o2=0.9
observation_matrix = ((o1,1-o1),(1-o2,o2))

#in the dynamic model, transition matrix 
t1=0.95
t2=0.9
transition_matrix= ((t1,1-t1),(1-t2,t2))

