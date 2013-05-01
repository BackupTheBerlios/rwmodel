#-*- coding: utf-8 -*-
#! python
#defines grid variables
from datetime import datetime
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
gaze_position = [[(2,2),(1,1)] for t in xrange(times+1)]


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

def dynamic_object_model(t,x,y):
	return 0.5
def observation_model(t,x,y):
	return 0.5

def knowledge_update():
	start_ = datetime.now()
	t = times
	for x in xrange(X):
		for y in xrange(Y):
			#fixed x and y
			grid_inference[x][y] = knowledge_update_recursive(t,x,y)


	end_ = datetime.now()
	print 'Elapsed time is ',(end_-start_).microseconds
	
def knowledge_update_recursive(t,x,y):
	#P(O^1_(x,y)|V^1 M^1) value at the end of recursion
	result = 1
	print "Gaze position:", gaze_position
	print "Time:", t, "end"
	print "Gaze position length:", len(gaze_position[t])
		
	if t != 2:
		for i in xrange(len(gaze_position[t])):
			result = result*\
			knowledge_update_recursive(t-1,gaze_position[t][i][0], gaze_position[t][i][1])
		
	print "Result:", result	
	
	result2 = 0
	for i in xrange(len(gaze_position[t])):
		result2 = result2+\
		dynamic_object_model(t, gaze_position[t][i][0], gaze_position[t][i][1])*result
	
	result2 = result2*observation_model(t,x,y)
	print "Result2:", result2
	return result2

knowledge_update()
print grid_inference
