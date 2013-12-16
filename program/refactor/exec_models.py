from debug import *
import var
from kum import *
from grid import Grid
from model import Model

def run(track_id = '"446"',
		track_trials =['"26"', '"28"', '"42"', '"51"', '"65"'], 
		grid=None,
		flag_run_grid = True,
		flag_run_inference = True,
		flag_run_models = True):
			
	dprint('Starting execution of eye tracking models ..')
	
	if flag_run_grid:
		dprint('Running var.py ..') 
		grid = var.load_grid(track_id, track_trials)
		
	if flag_run_inference:
		dprint('Runnning oku.py ..')
		execfile('oku.py')
		dprint('Running tku.py ..')
		execfile('tku.py')
	
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