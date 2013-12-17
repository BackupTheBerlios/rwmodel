centroid_targets = [ compute_centroid(targets_[0][t]) for t in xrange(len(targets_[0]))]
objects_ = [ targets_[0][t]+ distractors_[0][t] for t in xrange(len(targets_[0]))]
centroid_objects = [ compute_centroid(objects_[t]) for t in xrange(len(objects_)) ]
crowding_objects = [ 0 for t in xrange(len(targets_[0]))]
min_v_default= 16*dist_between_pos((0,0), (29,29))
min_arg_default = (0,0)
min_v = min_v_default
min_arg = min_arg_default

for t in xrange(0, times):
	for x in xrange(MAX):
		for y in xrange(MAX):
			
			suma = 0
			for i in xrange(targets):
				for d in xrange(targets):
					suma += ( dist_between_pos ((x,y), targets_[0][t][i]) / dist_between_pos (targets_[0][t][i],distractors_[0][t][i]) ) **2
					
			if suma < min_v:
				min_v = suma
				min_arg = (x,y)
						
	crowding_objects[t] = min_arg
	min_v = min_v_default
	min_arg = min_arg_default