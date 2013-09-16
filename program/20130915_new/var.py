# 2013.05.26 14:27:00 CEST
import csv
import os
import numpy
from  Small import Small
import time

def roundto(angle, precision = 0.5):
  correction = 0.5 if angle > 0 else -0.5
  return int(angle / precision + correction) * precision

def set_variables(rows):
  for t in xrange(len(rows)):
    x = roundto(float(rows[t][22]), 0.25)
    y = roundto(float(rows[t][23]), 0.25)
    x = int(x + 15)
    y = int(y + 15)
    gaze_position[t] = (x, y)
    counter = 0 #targets counter
    for i in range(6, 21, 2):
      x = roundto(float(rows[t][i]), 0.25)
      y = roundto(float(rows[t][(i + 1)]), 0.25)
      x = int(x + 15)
      y = int(y + 15)
      if counter < 4: 
        targets_[t][counter] = (x,y)
      else:
        distractors_[t][counter -4] = (x,y)
      counter +=1
      O[t][x][y] = 1
      if i>=6 and i<=12:
        T[t][(i-6)/2] =(x,y)
      
def readidblock(i, b):
  with open('../dataset/dataset_Erik.csv', 'rb') as csvfile:
    rows = []
    trial = []
    prev_trials = []
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for row in reader:
      if row[1]== i and row[2]== b:
        if row[3] not in prev_trials:
          prev_trials.append(row[3])
          if len(trial):
            rows.append(trial)
          trial =[]
          trial.append(row)
        else:
          trial.append(row)
    rows.append(trial)
  return rows

print "Starting execution ..."
print "Loading variables ... (objects, targets, antecedent,X,Y,bound1,bound2)\n"
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
#id1_b1 = readidblock('"1"','"1"')
id1_b2 = readidblock('"1"','"2"')
#id1_b3 = readidblock(1,3)
#id1_b4 = readidblock(1,4)
#id1_b5 = readidblock(1,5)
#d1_b6 = readidblock(1,6)

print 'len rows ...', len(id1_b2)
rows= id1_b2[0]

print "Initializing variables and arrays ..."
print "(times, O,V,T,M,I, I_T)\n"
_start = time.time()
times = len(rows) - 1
O = [ [ [ 0 for x in xrange(Y) ] for y in xrange(X) ] for t in xrange(times + 1) ]
T = [[ (0,0) for i in xrange(targets)] for t in xrange(times +1)]
M = [(0, 0) for t in xrange(times + 1) ]
targets_ = [[(0,0) for i in xrange(targets)] for t in xrange(times+1)]
distractors_  = [[(0,0) for i in xrange(objects - targets)] for t in xrange(times+1)]
print "(O,V,T,M) initialized ..."
I= [[[Small(numpy.random.uniform()) for x in xrange(Y)] for y in xrange(X)] for t in xrange(times +1)]
print "(I) initialized ..."
I_T = [[Small(numpy.random.uniform())  for i in xrange(targets)] for t in xrange(times+1)] #inference targets
print "(I_T) initialized ..."
print "Initialization took", (time.time() - _start)/60, "minutes ..."
print "Initializing variables and arrays ..."
print "(gaze_position, antecedent_cells, grid_inference, observation_matrix)\n"
gaze_position = [ (0, 0) for t in xrange(times + 1) ]
antecedent_cells = [ [(0, 0)] for t in xrange(times + 1) ]
grid_inference = [ [ 0 for x in xrange(Y) ] for y in xrange(X) ]
t1 = 0.95
t2 = 0.9
transition_matrix = ((t1, 1 - t1), (1 - t2, t2))

print "Initializing variables from csv data ...\n"
set_variables(rows)
print "Initialization successfull ..."
print "Process finished ..."
