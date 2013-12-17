import time
import math

from debug import *

import var
from kum import *

from grid import Grid
from model import Model

from oku import *

def run(track_id = '"446"',
		track_trials =['"26"', '"28"', '"42"', '"51"', '"65"'], 
		grid=None,
		ku_blocks_size = 1,
		flag_run_grid = True,
		flag_run_inference1 = True,
		flag_run_inference2 = True,
		flag_run_models = True):
			
	dprint('Starting execution of eye tracking models ..')
	
	if flag_run_grid:
		dprint('Running var.py ..') 
		grid = var.load_grid(track_id, track_trials)
	
	assert grid!= None, 'Grid was not loaded ..'
	
	if flag_run_inference1:
		dprint('Runnning oku.py ..')
		for b in xrange(ku_blocks_size):
			oku(grid, b)
	
	assert grid.flag_I != False, 'Inference1 has not run ..'
	
	if flag_run_inference2:
		dprint('Running tku.py ..')
		for b in xrange(ku_blocks_size):
			tku(grid, b)

	assert grid.flag_IT != False, 'Inference2 has not run ..'
	
	if flag_run_models:
		dprint('Running prep_model.py ..')
		execfile('prep_model.py')
		dprint('Runnign const_model.py ..')
		execfile('const_model.py')
		dprint('Running targ_model.py ..')
		execfile('targ_model.py')
		dprint('Running uncertain_model.py  ..')
		execfile('uncertain_model.py')
		
	dprint('Execution of eye tracking models finished ..')