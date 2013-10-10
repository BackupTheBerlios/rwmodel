# 2013.05.26 14:27:00 CEST
import csv
import os
import numpy

def roundto(angle, precision = 0.5):
    correction = 0.5 if angle > 0 else -0.5
    return int(angle / precision + correction) * precision

def readcsv():
  for t in xrange(len(rows)):
      x = roundto(float(rows[t][22]), 0.25)
      y = roundto(float(rows[t][23]), 0.25)
      x = int(x + 15)
      y = int(y + 15)
      gaze_position[t] = (x, y)
      x1 = min(x - bound1, antecedent)
      x2 = min(bound2 - x, antecedent + 1)
      y1 = min(y - bound1, antecedent)
      y2 = min(bound2 - y, antecedent + 1)
      antecedent_list = []
      for j in range(x - x1, x + x2):
          for i in range(y - y1, y + y2):
            antecedent_list.append((j, i))


      antecedent_cells[t] = antecedent_list
      for i in range(6, 21, 2):
          x = roundto(float(rows[t][i]), 0.25)
          y = roundto(float(rows[t][(i + 1)]), 0.25)
          x = int(x + 15)
          y = int(y + 15)
          O[t][x][y] = 1
          V[t][x][y] = 1


objects = 8
targets = 4
antecedent =1 
X = 30
Y = 30
bound1 = 0
bound2 = X
with open('../dataset/dataset_Erik.csv', 'rb') as csvfile:
    rows = []
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for row in reader:
        if row[1] == '"1"' and row[2] == '"1"' and row[3] == '"6"':
            rows.append(row)

times = len(rows) - 1
O = [ [ [ 0 for x in xrange(Y) ] for y in xrange(X) ] for t in xrange(times + 1) ]
V = [ [ [ 0 for x in xrange(Y) ] for y in xrange(X) ] for t in xrange(times + 1) ]
T = [[ (0,0) for i in xrange(targets)] for t in xrange(times +1)]

M = [ (0, 0) for t in xrange(times + 1) ]
I= [[[numpy.random.uniform() for x in xrange(Y)] for y in xrange(X)] for t in xrange(times +1)] 
I_T = [[numpy.random.uniform()  for i in xrange(targets)] for t in xrange(times+1)] #inference targets
gaze_position = [ (0, 0) for t in xrange(times + 1) ]
antecedent_cells = [ [(0, 0)] for t in xrange(times + 1) ]
grid_inference = [ [ 0 for x in xrange(Y) ] for y in xrange(X) ]
o1 = 0.9
o2 = 0.9
observation_matrix = ((o1, 1 - o1), (1 - o2, o2))
t1 = 0.95
t2 = 0.9
transition_matrix = ((t1, 1 - t1), (1 - t2, t2))

readcsv()
