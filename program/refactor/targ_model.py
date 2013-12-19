from __future__ import division
import math
from ku_methods import *

#P(T^t_i|C^t)
def gaze_target_model(g, (x,y), t, i):
	g_x = g.gaze[0][t][0]
	g_y = g.gaze[0][t][1]
	result = math.exp( -(dist_between_pos((x,y), g.targ[0][t][i]))**2 / 0.25)
	result /=900
	return result

def set_min_arr(ar, m):
	L = len(ar)
	result = [[ar[x][y] for y in xrange(L)] for x in xrange(L)]
	for x in xrange(L):
		for y in xrange(L):
			if result[x][y] < m:
				result[x][y] = m
	return result

#probability of gaze position
def tm(self):
	g = self.grid
	for t in range(2, g.time):#times -1
		temp = [[1 for x in xrange(g.X) ] for y in xrange(g.Y)]
		targ = [0,1,2,3]
		for ind in xrange(len(targ)):#targets
			i = targ[ind]
			GTM = [ [ 
						gaze_target_model(g, (x,y),t,i)
							for y in xrange(g.Y) ]
								for x in xrange(g.X)] 
			#temp =  mult_by_pos(GTM, temp, MAX)
			self.M[t] = mult_by_pos(self.M[t], g.IT_bit[0][i][t],g.size)
			self.M[t] = mult_by_pos(self.M[t], GTM, g.size)

		#TM[t] = root_by_pos(TM[t], len(targets_), MAX)
		self.M[t] = mult_by_pos(self.M[t], g.CM.M[t], g.size)
		
		(arg_min, arg_max) = calc_max_grid(self.M[t], flag_arg_max=True)
     
		self.M_traj[t] = arg_min