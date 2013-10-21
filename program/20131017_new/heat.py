from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.patches import Circle, Wedge
import math
#without changing interval
def print_heat_exp_new(I,X, Y, time,heat_array):
  for x in xrange(X):
    for y in xrange(Y):
      heat_array[x][y] = int(math.log10(I[time][x][y]))
  return  heat_array 
def print_heat_exp_new2(I,X, Y, time,heat_array):
  for x in xrange(X):
    for y in xrange(Y):
      heat_array[x][y] = I[time][x][y]
  return  heat_array 



def plot_map(I, X, Y, time, targets_, distractors_, array):
  heat_array = print_heat_exp_new(I, X, Y, time, array)
  data = np.asarray(heat_array)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time) + ' targ: ' + str(targets_[time]) +' (black)'+ '\n' + 'dist: '+ str(distractors_[time]) + ' (transparent)', fontsize=10)
  plt.colorbar(heatmap)
  for i in xrange(len(targets_[time])):
    circle1 = matplotlib.patches.Circle((targets_[time][i][1]+1, targets_[time][i][0]+1), radius=0.5, color='k', zorder=10)
    gca().add_patch(circle1) 
  for i in xrange(len(distractors_[time])):
    circle1 = matplotlib.patches.Circle((distractors_[time][i][1]+1, distractors_[time][i][0]+1), radius=0.5, color='k', zorder=10,fill=False)
    gca().add_patch(circle1) 
  plt.show()

def plot_model(M, X, Y, time, gaze_position, targets_, distractors_, array, blocks):
  heat_array = print_heat_exp_new(M, X, Y, time, array)
  data = np.asarray(heat_array)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time)+ ' gaze_position: [1]' + str(gaze_position[0][time]) + ' [2]'+ str(gaze_position[1][time]) + ' [3]' + str(gaze_position[2][time]) + ' [4]' + str(gaze_position[3][time]) + ' [5]' +  str(gaze_position[4][time]) + ' [6]' + str(gaze_position[5][time]) + ' (black)'+'\n' +'targ (green)' + '\n' +'dist (red)', fontsize=10)
  plt.colorbar(heatmap)
  
  for b in xrange(blocks):
    circle1 = matplotlib.patches.Circle((gaze_position[b][time][1]+1, gaze_position[b][time][0]+1), radius=0.5, color='k', zorder=10,fill=False)
    gca().add_patch(circle1) 
    
    for i in xrange(len(targets_[b][time])):
      circle1 = matplotlib.patches.Circle((targets_[b][time][i][1]+1, targets_[b][time][i][0]+1), radius=0.15, color='g', zorder=20)
      gca().add_patch(circle1) 
    for i in xrange(len(distractors_[b][time])):
      circle1 = matplotlib.patches.Circle((distractors_[b][time][i][1]+1, distractors_[b][time][i][0]+1), radius=0.15, color='r', zorder=20,)
      gca().add_patch(circle1) 
     
  plt.show()


def write_map(I, X, Y, time, targets_, distractors_, filename, heat_array):
  heat_array = print_heat_exp_new(I, X, Y, time,heat_array)
  data = np.asarray(heat_array)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time) + ' targ: ' + str(targets_[time]) +' (black)'+ '\n' + 'dist: '+ str(distractors_[time]) + ' (transparent)', fontsize=10)
  for i in xrange(len(targets_[time])):
    circle1 = matplotlib.patches.Circle((targets_[time][i][1]+1, targets_[time][i][0]+1), radius=0.5, color='k', zorder=10)
    gca().add_patch(circle1) 
  for i in xrange(len(distractors_[time])):
    circle1 = matplotlib.patches.Circle((distractors_[time][i][1]+1, distractors_[time][i][0]+1), radius=0.5, color='k', zorder=10,fill=False)
    gca().add_patch(circle1)
  plt.savefig(str(filename)+'.png')
  plt.clf()

def write_model(M, X, Y, time, gaze_position, targets_, distractors_, filename, array, blocks):
  heat_array = print_heat_exp_new(M, X, Y, time, array)
  data = np.asarray(heat_array)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time)+ ' gaze_position: [1]' + str(gaze_position[0][time]) + ' [2]'+ str(gaze_position[1][time]) + ' [3]' + str(gaze_position[2][time]) + ' [4]' + str(gaze_position[3][time]) + ' [5]' +  str(gaze_position[4][time]) + ' [6]' + str(gaze_position[5][time]) + ' (black)'+'\n' +'targ (green)' + '\n' +'dist (red)', fontsize=10)
  plt.colorbar(heatmap)
  
  for b in xrange(blocks):
    circle1 = matplotlib.patches.Circle((gaze_position[b][time][1]+1, gaze_position[b][time][0]+1), radius=0.5, color='k', zorder=10,fill=False)
    gca().add_patch(circle1) 
    
    for i in xrange(len(targets_[b][time])):
      circle1 = matplotlib.patches.Circle((targets_[b][time][i][1]+1, targets_[b][time][i][0]+1), radius=0.15, color='g', zorder=20)
      gca().add_patch(circle1) 
    for i in xrange(len(distractors_[b][time])):
      circle1 = matplotlib.patches.Circle((distractors_[b][time][i][1]+1, distractors_[b][time][i][0]+1), radius=0.15, color='r', zorder=20,)
      gca().add_patch(circle1) 
     
  plt.savefig(str(filename)+'.png')
  plt.clf()

 
#sudo ffmpeg -qscale 5 -r 20 -i %01d.png  movie.mp4
 
