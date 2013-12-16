from debug import *
import var
from kum import *

def run(flag_run_grid = True, flag_run_inference = True, flag_run_models = True):
	dprint('Starting execution of eye tracking models ..')
	
	if flag_run_grid:
		dprint('Running var.py ..') 
		var.load_vars()
		
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