# 2013.05.26 14:27:00 CEST
import csv
import os
import time

def roundto(angle, precision = 0.5):
  correction = 0.5 if angle > 0 else -0.5
  return int(angle / precision + correction) * precision

def set_variables(rows, b):
  for t in xrange(len(rows)):
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
      if i>=6 and i<=12:
        T[b][t][(i-6)/2] =(x,y)
      
def read_block(trial, track):
  with open('../dataset/dataset_Erik.csv', 'rb') as csvfile:
    rws = []
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #next(reader)
    for r in reader:
      if r[3] == trial and r[5]==track:
        rws.append(r)
  return rws

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
blocks_.append(read_block('"10"', '"138"'))
blocks_.append(read_block('"24"','"138"'))
blocks_.append(read_block('"41"', '"138"'))
blocks_.append(read_block('"53"', '"138"'))
blocks_.append(read_block('"70"', '"138"'))

print 'len rows ...', len(blocks_[0]), len(blocks_[1]), len(blocks_[2]), len(blocks_[3]), len(blocks_[4])

print "Initializing variables and arrays ..."
print "(times, O,V,T,M,I, I_T)\n"
_start = time.time()
times = len(blocks_[4])
O = [ [ [ [ 0 for x in xrange(Y) ] for y in xrange(X) ] for t in xrange(times + 1) ] for b in xrange(blocks)] 
T = [ [ [ (0,0) for i in xrange(targets)] for t in xrange(times +1)] for b in xrange(blocks)]
M = [(0, 0) for t in xrange(times + 1) ]
targets_ = [ [ [ (0,0) for i in xrange(targets) ] for t in xrange(times+1) ] for b in xrange(blocks)]
distractors_  = [ [ [(0,0) for i in xrange(objects - targets) ] for t in xrange(times+1) ] for b in xrange(blocks)]
print "(O,V,T,M) initialized ..."
I= [ [ [ [0.5 for x in xrange(Y)] for y in xrange(X)] for t in xrange(times +1)] for b in xrange(blocks)]
print "(I) initialized ..."
I_T= [[[[0.5 for x in xrange(Y)] for y in xrange(X)] for t in xrange(times +1)] for b in xrange(blocks)]
print "(I_T) initialized ..."
print "Initialization took", (time.time() - _start)/60, "minutes ..."
print "Initializing variables and arrays ..."
print "(gaze_position, antecedent_cells, grid_inference, observation_matrix)\n"
gaze_position = [ [ (0, 0) for t in xrange(times + 1) ] for b in xrange(blocks)]
antecedent_cells = [ [ [(0, 0)] for t in xrange(times + 1) ] for b in xrange(blocks)]
#grid_inference = [ [ 0 for x in xrange(Y) ] for y in xrange(X) ]

print "Initializing variables from csv data ...\n"
for b in xrange(blocks):
  rows = blocks_[b]
  set_variables(rows, b)
times = 488 #according to the smallest block
print "Initialization successfull ..."
print "Process finished ..."
end_ = time.time()
print 'Elapsed time is ', (end_ - start_)/60, 'minutes'
