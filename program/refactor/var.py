import csv
import numpy
from debug import *
from ku_methods import *
from grid import *

def set_variables(grid, rows, b, time):
	for t in xrange(time):
		x = float(rows[t][22])
		y = float(rows[t][23])
		x = int(round(x))
		y = int(round(y))
		x += 15
		y += 15
		grid.gaze[b][t] = (x, y)
		grid.time_eye[b][t] = rows[t][24]
		counter = 0 #targets counter
		for i in range(6, 21, 2):
			x = roundto(float(rows[t][i]), 0.25)
			y = roundto(float(rows[t][(i + 1)]), 0.25)
			x = int(x + 15)
			y = int(y + 15)
			if counter < 4: 
				grid.targ[b][t][counter] = (x,y)
			else:
				grid.dist[b][t][counter -4] = (x,y)
			counter +=1
			grid.O[b][t][x][y] = 1
			
def read_block(trial, track):
  with open('../dataset/dataset_Erik.csv', 'rb') as csvfile:
    rws = []
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #next(reader)
    for r in reader:
      if r[3] == trial and r[5]==track:
        rws.append(r)
  return rws

def load_grid(track_id, track_trials):
	dprint("Starting ..");
	
	blocks_ = []
	for trial in track_trials:
		blocks_.append(read_block(trial, track_id))
	
	time=1000
	blocks_size = len(blocks_)
	
	for b in blocks_:
		if len(b) < time:
			time = len(b)

	print 'time', time
	grid = Grid(time, track_id, track_trials)
	
	for b in xrange(blocks_size):#blocks
		rows = blocks_[b]
		set_variables(grid, rows, b, time)
	
	dprint("Finished ..")
	return grid
