from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import copy
import math
def print_heat(I,X, Y, time):
  maxv =0
  minv =1
  for x in xrange(X):
    for y in xrange(Y):
      val = I[time][x][y]
      if val > maxv:
        maxv = val 
      if val < minv: 
        minv = val
      
  print 'max:', maxv
  print 'min:', minv
  
  interval_diff = maxv - minv
  print 'interval: ', interval_diff
  heat_array = [[0 for y in xrange(Y)] for x in xrange(X)]

  for x in xrange(X):
    for y in xrange(Y):
      tmp = I[time][x][y] - minv
      
      heat_array[x][y] = float(tmp /  interval_diff)
      #print heat_array[x][y] 
  return  heat_array 

def print_heat_exp(I,X, Y, time):
  maxv =10000
  minv =0
  heat_array = [[0 for y in xrange(Y)] for x in xrange(X)]
  for x in xrange(X):
    for y in xrange(Y):
      heat_array[x][y] = abs(int(math.log10(I[time][x][y])))
      if heat_array[x][y] > minv:
        minv = heat_array[x][y]
      if heat_array[x][y] < maxv: 
        maxv = heat_array[x][y]
      
  maxv = -maxv
  minv = -minv
      
  print 'max:', maxv
  print 'min:', minv
  
  interval_diff = maxv - minv
  print 'interval: ', interval_diff

  for x in xrange(X):
    for y in xrange(Y):
      tmp = -heat_array[x][y] - minv
      
      heat_array[x][y] = float(tmp /  interval_diff)
      #print heat_array[x][y] 
  return  heat_array 

#without changing interval
def print_heat_exp_new(I,X, Y, time,heat_array):
  for x in xrange(X):
    for y in xrange(Y):
      heat_array[x][y] = int(math.log10(I[time][x][y]))
  return  heat_array 


def plot_map(I, X, Y, time, targets_, distractors_, array):
  heat_array = print_heat_exp_new(I, X, Y, time, array)
  data = np.asarray(heat_array)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time) + ' targ: ' + str(targets_[time]) + '\n' + 'dist: '+ str(distractors_[time]), fontsize=10)
  plt.colorbar(heatmap)
  plt.show()

def write_map(I, X, Y, time, targets_, distractors_, filename, heat_array):
  heat_array = print_heat_exp_new(I, X, Y, time,heat_array)
  data = np.asarray(heat_array)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time) + ' targ: ' + str(targets_[time]) + '\n' + 'dist: ' + str(distractors_[time]), fontsize=10)
  plt.savefig(str(filename)+'.png')
  
#sudo ffmpeg -qscale 5 -r 20 -i %01d.png  movie.mp4
 
