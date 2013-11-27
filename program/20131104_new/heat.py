from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.patches import Circle, Wedge
import math
#without changing interval

heat_array =  [[0 for x in xrange(X) ] for y in xrange (Y)]
ticks_labels = [ i for i in range(-15,16,5)]

def gen_exp(I):
  for x in xrange(X):
    for y in xrange(Y):
      heat_array[x][y] = int(math.log10(I[x][y]))
  return  heat_array 
def print_heat_exp_new2(I,X, Y, time,heat_array):
  for x in xrange(X):
    for y in xrange(Y):
      heat_array[x][y] = I[time][x][y]
  return  heat_array 

def gen_polygon_pt((x,y), rad):
  return [(x-rad, y), (x, y-rad),  (x+rad, y),(x, y+rad)]

def plot_cross(plt, (x,y), rad, color):
  pts=gen_polygon_pt((x,y), rad)
  plt.plot([pts[0][1], pts[2][1]], [pts[0][0], pts[2][0]], linewidth=1, linestyle="-", c = color, zorder = 30)
  plt.plot([pts[1][1], pts[3][1]], [pts[1][0], pts[3][0]], linewidth=1, linestyle="-", c = color, zorder = 30)

def plot_map_basic(I):
  data  = np.asarray(I)
  heatmap = plt.pcolor(data)
  plt.show()

def prepare_map(I, time, exp_flag):
  if (exp_flag):
    ar = gen_exp(I[time])
  else:
    ar = I[time]
  
  data = np.asarray(ar)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time) + ' targ: ' + str(targets_[0][time]) +' (black)'+ '\n' + 'dist: '+ str(distractors_[0][time]) + ' (transparent)', fontsize=10)
  plt.colorbar(heatmap)
  for i in xrange(len(targets_[0][time])):
    circle1 = matplotlib.patches.Circle((targets_[0][time][i][1]+1, targets_[0][time][i][0]+1), radius=0.5, color='k', zorder=10)
    gca().add_patch(circle1) 
  for i in xrange(len(distractors_[0][time])):
    circle1 = matplotlib.patches.Circle((distractors_[0][time][i][1]+1, distractors_[0][time][i][0]+1), radius=0.5, color='k', zorder=10,fill=False)
    gca().add_patch(circle1) 

def plot_map (I, time, exp_flag):
  prepare_map(I, time, exp_flag)

  a = plt.gca()

  a.set_xticklabels(ticks_labels)
  a.set_yticklabels(ticks_labels)
  
  plt.show()
  plt.clf()

def write_map(I, time, filename, exp_flag):
  prepare_map(I, time, exp_flag)
  a = plt.gca()

  a.set_xticklabels(ticks_labels)
  a.set_yticklabels(ticks_labels)
  
  
  plt.savefig(str(filename) + '.png')
  plt.clf()

def prepare_model(M, time, exp_flag):
  
  if(exp_flag):
    ar = gen_exp(M[time])
  else:
    ar = M[time]

  data = np.asarray(ar)
  heatmap = plt.pcolor(data)
  plt.xlabel('time: ' + str(time)+ ' gaze_position: [1]' + str(gaze_position[0][time]) + ' [2]'+ str(gaze_position[1][time]) + ' [3]' + str(gaze_position[2][time]) + ' [4]' + str(gaze_position[3][time]) + ' [5]' +  str(gaze_position[4][time]) + ' (black)'+'\n' +'targ (green)' + '\n' +'dist (red)', fontsize=10)
  plt.colorbar(heatmap)
  
  for b in xrange(blocks):
    #pts = gen_polygon_pt((gaze_position[b][time][1], gaze_position[b][time][0]), 0.7)
    #polygon1 = matplotlib.patches.Polygon(pts, color='k', fill =False, zorder=25)
    #gca().add_patch(polygon1)
    plot_cross(plt, (gaze_position[b][time][1], gaze_position[b][time][0]),0.3, 'k')   
  


  for i in xrange(len(targets_[0][time])):
    circle1 = matplotlib.patches.Circle((targets_[0][time][i][1], targets_[0][time][i][0]), radius=0.15, color='g', zorder=20)
    gca().add_patch(circle1) 
  for i in xrange(len(distractors_[0][time])):
    circle1 = matplotlib.patches.Circle((distractors_[0][time][i][1], distractors_[0][time][i][0]), radius=0.15, color='r', zorder=20)
    gca().add_patch(circle1) 
  pts = gen_polygon_pt((15,15),0.6)
  plg_center = matplotlib.patches.Polygon(pts, color='w',edgecolor='k', zorder=20)
  pts = gen_polygon_pt((centroid_targets[time][1], centroid_targets[time][0]), 0.6)
  plg_centroid_targ = matplotlib.patches.Polygon(pts, color='g', edgecolor='k', zorder=20)
  pts = gen_polygon_pt((centroid_objects[time][1], centroid_objects[time][0]), 0.6)
  plg_centroid_obj = matplotlib.patches.Polygon(pts, color='r', edgecolor='k', zorder=20)
  pts = gen_polygon_pt((crowding_objects[time][1], crowding_objects[time][0]), 0.6)
  plg_crowding = matplotlib.patches.Polygon(pts, color='orange', edgecolor='k', zorder=20)
  gca().add_patch(plg_center)
  gca().add_patch(plg_centroid_targ)
  gca().add_patch(plg_centroid_obj)
  gca().add_patch(plg_crowding)

def plot_model(M, time,exp_flag):
  prepare_model(M, time, exp_flag)

  a = plt.gca()

  a.set_xticklabels(ticks_labels)
  a.set_yticklabels(ticks_labels)
  plt.show()
  plt.clf()

def write_model(M, time, filename,exp_flag):
  prepare_model(M, time,exp_flag)

  a = plt.gca()

  a.set_xticklabels(ticks_labels)
  a.set_yticklabels(ticks_labels)
  
  plt.savefig(str(filename) + '.png')
  plt.clf()

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


#sudo ffmpeg -qscale 5 -r 20 -i %01d.png  movie.mp4
 
