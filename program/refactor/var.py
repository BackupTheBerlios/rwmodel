# 2013.05.26 14:27:00 CEST
import csv
import os
import time
import numpy

def roundto(angle, precision = 0.5):
  correction = 0.5 if angle > 0 else -0.5
  return int(angle / precision + correction) * precision

def set_variables(rows, b):
	for t in xrange(times):
		x = roundto(float(rows[t][22]), 0.25)
		y = roundto(float(rows[t][23]), 0.25)
		x = int(x + 15)
		y = int(y + 15)
		gaze_position[b][t] = (x, y)
		counter = 0 #targets counter
		for i in range(6, 21, 2):
			x = roundto(float(rows[t][i]), 0.25)
			y = roundto(float(rows[t][(i + 1)]), 0.25)
			x = int(x + 15)
			y = int(y + 15)
			if counter < 4: 
				targets_[b][t][counter] = (x,y)
			else:
				distractors_[b][t][counter -4] = (x,y)
			counter +=1
			O[b][t][x][y] = 1
			
def read_block(trial, track):
  with open('../dataset/dataset_Erik.csv', 'rb') as csvfile:
    rws = []
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #next(reader)
    for r in reader:
      if r[3] == trial and r[5]==track:
        rws.append(r)
  return rws

def load_vars():
	start_ = time.time()
	print "Starting execution ..."
	print "Loading variables ... (objects, targets, antecedent,X,Y,bound1,bound2)\n"
	blocks =5 
	objects = 8
	targets = 4
	antecedent =1 
	X = 30
	Y = 30
	bound1 = 0
	bound2 = X
	"""
	row[1] ... person id 1-11
	row[2] ... block 1-6
	row[4] ... trials circa 6-48
	row[4] ... trial 2-0
	"""
	print "Reading CSV blocks ...\n"
	blocks_ = []
	block = 0
	blocks_.append(read_block('"26"', '"446"'))
	blocks_.append(read_block('"28"','"446"'))
	blocks_.append(read_block('"42"', '"446"'))
	blocks_.append(read_block('"51"', '"446"'))
	blocks_.append(read_block('"65"', '"446"'))

	print 'len rows ...', len(blocks_[0]), len(blocks_[1]), len(blocks_[2]), len(blocks_[3]), len(blocks_[4])

	times = 1000
	for i in len(blocks_):
		if len(blocks_[i]) < times:
			times = len(blocks_[i])
			
	print "Initializing variables and arrays ..."
	print "(times, O,V,T,M,I, I_T)\n"
	_start = time.time()
	O = [ [ [ [ 0 for x in xrange(Y) ] for y in xrange(X) ] for t in xrange(times + 1) ] for b in xrange(blocks)] 
	targets_ = [ [ [ (0,0) for i in xrange(targets) ] for t in xrange(times+1) ] for b in xrange(blocks)]
	distractors_  = [ [ [(0,0) for i in xrange(objects - targets) ] for t in xrange(times+1) ] for b in xrange(blocks)]
	print "(O,V) initialized ..."
	I= [ [ [ [numpy.random.uniform() for x in xrange(Y)] for y in xrange(X)] for t in xrange(times +1)] for b in xrange(blocks)]
	#print "(I) initialized ..."
	I_T= [[[[numpy.random.uniform() for x in xrange(Y)] for y in xrange(X)] for t in xrange(times +1)] for b in xrange(blocks)]
	print "(I_T) initialized ..."
	print "Initialization took", (time.time() - _start)/60, "minutes ..."
	print "Initializing variables and arrays ..."
	print "(gaze_position, grid_inference, observation_matrix)\n"
	gaze_position = [ [ (0, 0) for t in xrange(times + 1) ] for b in xrange(blocks)]
	
	print "Initializing variables from csv data ...\n"
	for b in xrange(1):#blocks
		rows = blocks_[b]
		set_variables(rows, b)
	print "Initialization successfull ..."
	print "Process finished ..."
	end_ = time.time()
	print 'Elapsed time is ', (end_ - start_)/60, 'minutes'
