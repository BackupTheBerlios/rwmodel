from __future__ import division
import numpy
import time
from ku_methods import *
#definition of grid interface
class Grid:
	def __init__(self, time, blocks_size, anc_size=1, size=30, targ_size=4, dist_size=4):
		self.size = size
		self.X = size
		self.Y = size
		self.anc_size = anc_size
		self.blocks_size = blocks_size
		self.targ_size = targ_size;
		self.dist_size = dist_size;
		self.time = time
		self.flag_I = False
		self.flag_IT = False
		
		self.O = [ [ [ [ 0 for x in xrange(self.X) ]  
						for y in xrange(self.Y) ]  
							for t in xrange(self.time + 1) ] 
								for b in xrange(self.blocks_size) ] 
		
		self.I= [ [ [ [
					numpy.random.uniform() 
					for x in xrange(self.X)]
						for y in xrange(self.Y) ]
							for t in xrange(self.time +1)]
								for b in xrange(self.blocks_size)]
		
		self.IT= [ [ [ [
					numpy.random.uniform()
						for x in xrange(self.X)]
							for y in xrange(self.Y)]
								for t in xrange(self.time +1)]
									for b in xrange(self.blocks_size)]
									
		self.IT_bit = [ [ [ [ [
						0
						for x in xrange(self.X) ]
							for y in xrange(self.Y) ]
								for t in xrange(self.time+1) ]
									for i in xrange(self.targ_size) ]
										for b in xrange(self.blocks_size) ]

		
		self.targ = [ [ [ 
						(0,0)
							for i in xrange(self.targ_size) ] 
								for t in xrange(self.time+1) ] 
									for b in xrange(self.blocks_size)]
		self.dist  = [ [ [
						(0,0)
							for i in xrange(self.dist_size)] 
								for t in xrange(self.time+1) ] 
									for b in xrange(self.blocks_size)]
	
	
		
		self.gaze = [ [ 
						(0, 0)
							for t in xrange(self.time + 1)]
								for b in xrange(self.blocks_size)]
		
		#support for plotting device
		self.arr =  [[0 for x in xrange(self.X) ] for y in xrange (self.Y)]
		
		self.ticks_labels = [ i for i in range(-15,16,5)]
		
	def prepare_map(self, time, inference, block = 0, exp_flag = False):
		g = self.grid
		if inference ==1:
			M = g.I[block]
		else:
			M = g.IT[block]
			
		if (exp_flag):
			ar = gen_exp(M,time)
		else:
			ar = M[time]
	
		data = np.asarray(ar)
		heatmap = plt.pcolor(data)
		plt.xlabel('time: ' + str(time) + 
			 \' targ: ' + str(g.targ[0][time]) +' (black)'+ '\n' + 
			 \'dist: '+ str(g.dist[0][time]) + ' (transparent)', fontsize=10)
		plt.colorbar(heatmap)
		
		for i in xrange(g.targ_size):
			circle1 = matplotlib.patches.Circle((g.targ[0][time][i][1]+1,
													g.targ[0][time][i][0]+1), radius=0.5, 
														color='k', zorder=10)
			gca().add_patch(circle1) 
			
		for i in xrange(g.dist_size):
			circle1 = matplotlib.patches.Circle((g.dist[0][time][i][1]+1, 
													g.dist[0][time][i][0]+1), 
														radius=0.5, color='k', zorder=10,fill=False)
			gca().add_patch(circle1) 

	def plot_map (I, time, inference=1, exp_flag=False):
		prepare_map(I, time, inference, exp_flag)

		a = plt.gca()

		a.set_xticklabels(ticks_labels)
		a.set_yticklabels(ticks_labels)
		
		plt.show()
		plt.clf()

	def write_map(I, time, inference=1, filename, exp_flag=False):
		prepare_map(I, time, inference, exp_flag)
		a = plt.gca()

		a.set_xticklabels(ticks_labels)
		a.set_yticklabels(ticks_labels)
		
		
		plt.savefig(str(filename) + '.png')
		plt.clf()

								
	
	def oku(self, b):
		print "Object knowledge update started ...\n"
		_start = time.time()
		for t in xrange(2,self.time+1):    #!!!times+1
			#incremental phase
			print "Suma calculation started ...\n"
			
			for x in xrange(self.X):
				for y in xrange(self.Y):
					tmp1 =1
					mul1 =1
					suma =1
					(ant_size, xl, xr, yl, yr) = calc_antecedent_bounds(self,x,y)
					for j in range(xl, xr):
						for i in range(yl, yr):
							tmp1 *= self.I[b][t-1][j][i]
					tmp1 = tmp1**(1/ant_size)

					for i in range(xl, xr):
						for j in range(yl, yr):
							mul1 = tmp1 * dynamic_object_model(self, b,t,i,j)
							mul1 = mul1**(1/2)
							suma *= mul1
					suma = suma **(1/ant_size)
					suma*= observation_model(self, b,t,x,y)
					#suma /= ant_size
					self.I[b][t][x][y] = suma
			
			min_max_normal(self.I[b][t],b, False)#normalize(b,t)
			print "Time: ", t
		print "Object knowledge update successfully finished ..."
		self.flag_I = True

	def tku(self, b):
		print "Target knowledge update started ..."
		start_ = time.time()
		IT_i= [ [ [ 0
					for x in xrange(self.X) ]
						for y in xrange(self.Y) ]
							for i in xrange(self.targ_size) ]

		for t in range(2,self.time+1 ):  #times+1
			print 'time is:' , t
			for i in xrange(self.targ_size):
				for x in xrange(self.X):
					for y in xrange(self.Y):
						(ant_size, xl, xr, yl, yr) = calc_antecedent_bounds(self,x,y)
						suma1 = 0
					
						for j in range(xl, xr):
							for k in range(yl, yr):
								suma1 += (target_observation_model(self, b, t, i, j, k)*self.I[b][t][j][k])
						suma1 /= ant_size
						IT_i[i][x][y] = suma1
						self.IT_bit[b][i][t][x][y] = suma1
			print "over targets ..."

			for x in xrange(self.X):
				for y in xrange(self.Y):
					suma2 = 0
					for i in xrange(self.targ_size):
						suma2 += IT_i[i][x][y]#*I_T[t-1][x][y]
					suma2 /=self.targ_size
					self.IT[b][t][x][y] = suma2
			min_max_normal(self.IT[b][t],b , True)#normalize(b,t)
		
		self.flag_IT = True
		end_ = time.time()
		print "Target knowledge update finished ..."
		print 'Elapsed time is ',(end_-start_)/60, 'minutes'	
	