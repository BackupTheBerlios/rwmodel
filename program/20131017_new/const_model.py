from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: constant_model
#author Erik Lux
#date: 20131017
#purpose: depict users gaze position 
#modified: file will be loaded

#const_model contains all blocks
CM = [ [ [ 0.01 for y in xrange(Y) ] for x in xrange(X) ] for t in xrange(times+1) ]

#probability of gaze position
def cm():
  p = 1/blocks
  for b in xrange(blocks):
    (x, y) = gaze_position[b][0]
    for t in xrange(times+1):
      CM[t][x][y] += p
  return CM

