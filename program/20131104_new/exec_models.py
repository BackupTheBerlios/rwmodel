import inspect

def dprint(msg):
	callerframerecord = inspect.stack()[1]    # 0 represents this line
	# 1 represents line at caller
	frame = callerframerecord[0]
	info = inspect.getframeinfo(frame)
	print '[',info.filename,'->',info.function,'->',info.lineno, ']: ', msg                       # __FILE__     -> Test.py
	
def run(flag_run_grid = True, flag_run_inference = True, flag_run_models = True):
	dprint('Starting execution of eye tracking models ..')
	
	if flag_run_grid:
		print 'Running var.py ..' 
		execfile('var.py')
		print 'Running grid.py ..'
		execfile('grid.py')
	
	if flag_run_inference:
		print 'Runnning oku.py ..'
		execfile('oku.py')
		print 'Running tku.py ..'
		execfile('tku.py')
	
	if flag_run_models:
		print 'Running prep_model.py ..'
		execfile('prep_model.py')
		print 'Runnign const_model.py ..'
		execfile('const_model.py')
		print 'Running targ_model.py ..'
		execfile('targ_model.py')
		print 'Running uncertain_model.py  ..'
		execfile('uncertain_model.py')
		
	print 'Execution of eye tracking models finished ..' 