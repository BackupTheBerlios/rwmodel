import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.patches import Circle, Wedge
import math

from ku_methods import *

from const_model import *
from targ_model import *
from uncertain_model import *

import types

#definition of grid interface
class Abstract_model(object):
	def __init__(self, grid, ku_blocks_size):
		self.grid = grid
		self.ku_blocks_size = ku_blocks_size
		
		self.M = [ [ [ 
					1 
					for y in xrange(grid.X) ]
						for x in xrange(grid.Y) ]
							for t in xrange(grid.time+1) ]
							
		self.M_traj = [ 
						(0,0)
							for t in xrange(grid.time+1) ]
							
		self.arr = [ [
						0
						for x in xrange(grid.X) ]
							for y in xrange(grid.Y) ] 
	
	def naive_strategy_traj(self):
		g = self.grid
		self.centroid_targets_traj = [
								compute_centroid(g.targ[0][t])
									for t in xrange(g.time)]
									
		obj = [ 
				g.targ[0][t]+ g.dist[0][t]
					for t in xrange(g.time)]

		self.centroid_objects_traj = [
								compute_centroid(obj[t])
									for t in xrange(len(obj)) ]

		self.crowding_objects_traj = [ 
								0 
									for t in xrange(g.time)]
		
		min_v_default= 16*dist_between_pos((0,0), (29,29))
		min_arg_default = (0,0)
		min_v = min_v_default
		min_arg = min_arg_default

		for t in xrange(0, g.time):
			for x in xrange(g.X):
				for y in xrange(g.Y):
					suma = 0
					for i in xrange(g.targ_size):
						for d in xrange(g.targ_size):
							suma += ( dist_between_pos ((x,y),
									g.targ[0][t][i]) / dist_between_pos (g.targ[0][t][i],g.dist[0][t][i]) ) **2
					if suma < min_v:
						min_v = suma
						min_arg = (x,y)
								
			self.crowding_objects_traj[t] = min_arg
			min_v = min_v_default
			min_arg = min_arg_default
			
	def gen_polygon_pt(self, (x,y), rad):
		return [(x-rad, y), (x, y-rad),  (x+rad, y),(x, y+rad)]

	def plot_cross(self, plt, (x,y), rad, color, cross_ord):
		pts=self.gen_polygon_pt((x,y), rad)
		plt.plot([pts[0][1], pts[2][1]], [pts[0][0], pts[2][0]], linewidth=1, linestyle="-", c = color, zorder = cross_ord)
		plt.plot([pts[1][1], pts[3][1]], [pts[1][0], pts[3][0]], linewidth=1, linestyle="-", c = color, zorder = cross_ord)
	
	def prepare_model(self, time, exp_flag, flag_traj=False):
		
		g = self.grid
		
		if flag_traj:
			self.arr[self.M_traj[time][0]][self.M_traj[time][1]] = 1
			self.arr[g.UM.M_traj[time][0]][g.UM.M_traj[time][1]] = 1
			ar = self.arr
			
		else:
			if(exp_flag):
				ar = gen_exp(self.M, time)
			else:
				ar = self.M[time]

		data = np.asarray(ar)
		
		if flag_traj:
			self.arr[self.M_traj[time][0]][self.M_traj[time][1]] = 0
			self.arr[g.UM.M_traj[time][0]][g.UM.M_traj[time][1]] = 0
			
		heatmap = plt.pcolor(data)
		
		label = 'gaze: '
		for i in xrange(g.blocks_size):
			label += str(i) + '('+str(g.gaze[i][time][1]-15)+','+str(g.gaze[i][time][0]-15)+')' + ' '
		
		plt.xlabel(label +' (black)'+'\n' +'targ (green)' + '\n' +'dist (red)', fontsize=10)
		
		plt.colorbar(heatmap)
	
		obj_ord = 30
		cross_ord = 25
		obj_rad = 0.15
		
		for b in xrange(g.blocks_size):
			print g.gaze[b][time]
			self.plot_cross(plt, (g.gaze[b][time][0], g.gaze[b][time][1]),0.3, 'k', cross_ord)   
		
		for i in xrange(g.targ_size):
			circle1 = matplotlib.patches.Circle((g.targ[0][time][i][1], 
													g.targ[0][time][i][0]), 
														radius=obj_rad, color='g', zorder=obj_ord)
			gca().add_patch(circle1)
			
		for i in xrange(g.dist_size):
			circle1 = matplotlib.patches.Circle((g.dist[0][time][i][1],
													g.dist[0][time][i][0]), 
														radius=obj_rad, color='r', zorder=obj_ord)
			gca().add_patch(circle1) 
			
		pol_ord = 20
		pol_rad = 0.6
		pts = self.gen_polygon_pt((15,15),pol_rad)
		plg_center = matplotlib.patches.Polygon(pts, color='w',edgecolor='k', zorder=pol_ord)
		pts = self.gen_polygon_pt((g.CM.centroid_targets_traj[time][1], 
								g.CM.centroid_targets_traj[time][0]), 
									pol_rad)
		plg_centroid_targ = matplotlib.patches.Polygon(pts, color='g', edgecolor='k', zorder=pol_ord)
		pts = self.gen_polygon_pt((g.CM.centroid_objects_traj[time][1],
								g.CM.centroid_objects_traj[time][0]), 
									pol_rad)
		plg_centroid_obj = matplotlib.patches.Polygon(pts, color='r', edgecolor='k', zorder=pol_ord)
		pts = self.gen_polygon_pt((g.CM.crowding_objects_traj[time][1], 
								g.CM.crowding_objects_traj[time][0]),
									pol_rad)
		plg_crowding = matplotlib.patches.Polygon(pts, color='orange', edgecolor='k', zorder=pol_ord)
		
		gca().add_patch(plg_center)
		gca().add_patch(plg_centroid_targ)
		gca().add_patch(plg_centroid_obj)
		gca().add_patch(plg_crowding)
	
	def plot_time(self, time,exp_flag=False):
		self.prepare_model(time, exp_flag)

		a = plt.gca()

		a.set_xticklabels(self.grid.ticks_labels)
		a.set_yticklabels(self.grid.ticks_labels)
		
		plt.show()
		plt.clf()
		
	def plot_traj_time(self, time,exp_flag=False):
		self.prepare_model(time, exp_flag, flag_traj=True)

		a = plt.gca()

		a.set_xticklabels(self.grid.ticks_labels)
		a.set_yticklabels(self.grid.ticks_labels)
		
		plt.show()
		plt.clf()
	
	def write_traj_time(self, time,filename, exp_flag=False):
		self.prepare_model(time,exp_flag, flag_traj = True)

		a = plt.gca()

		a.set_xticklabels(self.grid.ticks_labels)
		a.set_yticklabels(self.grid.ticks_labels)
		
		
		plt.savefig(str(filename) + '.png')
		plt.clf()
	
	def write_traj(self, file_num, exp_flag=False):
		for t in xrange(self.grid.time):
			print t
			self.write_traj_time(t, int(file_num)+t, exp_flag) 
			

	def write_time(self, time, filename,exp_flag=False):
		self.prepare_model(time,exp_flag)

		a = plt.gca()

		a.set_xticklabels(self.grid.ticks_labels)
		a.set_yticklabels(self.grid.ticks_labels)
		
		
		plt.savefig(str(filename) + '.png')
		plt.clf()
		
	
class Model(Abstract_model):
	def __init__(self, grid, ku_blocks_size, compute_method):
		super(Model, self).__init__(grid, ku_blocks_size)
		self.compute = types.MethodType(compute_method, self)
		
	def compute(self):
		return self.compute(self)
	
		
						
						
  

