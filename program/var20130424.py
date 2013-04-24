#-*- coding: utf-8 -*-
#! python

#defines grid variables
times = 5 #number of timestamps
X = 5 #width of grid
Y = 4 #height of grid
O = [[[0 for x in xrange(X)] for y in xrange(Y)] for t in xrange(times)]#objects
V = [[[0 for x in xrange(X)] for y in xrange(Y)] for t in xrange(times)]#visual
M = [0 for t in xrange(times)]#past eye movement information

