from __future__ import division

import time
import math

from debug import *

import var
from ku_methods import *

from grid import Grid
from model import Model

from const_model import cm
from targ_model import tm
from uncertain_model import um


def run(track_id = '"446"',
		track_trials =['"26"', '"28"', '"42"', '"51"', '"65"'], 
		grid=None,
		ku_blocks_size = 1,
		flag_run_grid = True,
		flag_run_inference1 = True,
		flag_run_inference2 = True,
		flag_run_models = True,
		flag_exit_loaded = False,
		flag_exit_inference1 = False,
		flag_exit_inference2 = False
		):
	
	dprint('Starting execution of eye tracking models ..')
	
	if flag_run_grid:
		dprint('Running var.py ..') 
		grid = var.load_grid(track_id, track_trials)
	
	if flag_exit_loaded:
		return grid
	
	assert grid!= None, 'Grid was not loaded ..'
	
	if flag_run_inference1:
		dprint('Runnning oku.py ..')
		for b in xrange(ku_blocks_size):
			grid.oku(b)
	
	if flag_exit_inference1:
		return grid
	
	assert grid.flag_I != False, 'Inference1 has not run ..'
	
	if flag_run_inference2:
		dprint('Running tku.py ..')
		for b in xrange(ku_blocks_size):
			grid.tku(b)
			
	if flag_exit_inference2:
		return grid

	assert grid.flag_IT != False, 'Inference2 has not run ..'
	
	if flag_run_models:
		dprint('Running model.py ..')
		grid.CM = Model(grid, ku_blocks_size,cm)
		dprint('Computing trajectories of naive strategies')
		grid.CM.naive_strategy_traj()
		
		dprint('Running const_model.py ..')
		grid.CM.compute()
		
		dprint('Running targ_model.py ..')
		grid.TM = Model(grid, ku_blocks_size, tm)
		grid.TM.compute()
		
		dprint('Running uncertain_model.py ..')
		grid.UM = Model(grid, ku_blocks_size, um)
		grid.UM.compute()
		
	dprint('Execution of eye tracking models finished ..')
	
	return grid