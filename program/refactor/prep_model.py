def calc_max(I):
	maxm = 0
	minm = 1
	for x in xrange(MAX):
		for y in xrange(MAX):
			if I[x][y] > maxm:
				maxm = I[x][y]
			if I[x][y] < minm:
				minm = I[x][y]
	return (minm, maxm)


def compute_centroid(points):
	x = 0
	y = 0
	for p in points:
		x += p[0]
		y += p[1]
		x /= len(points)
		y /= len(points)
		x = int(round(x,0))
		y = int(round(y,0))
		
		return (x,y)
	
def dist_between_pos ((x1,y1), (x2,y2)):
	return math.sqrt(abs((x2-x1)/4)**2 + abs((y2-y1)/4)**2)

def mult_by_pos (ar1, ar2, MAX):
	return [ [ar1[x][y] * ar2[x][y] for y in xrange(MAX)] for x in xrange(MAX)]

def add_by_pos (ar1, ar2, MAX):
	return [[ar1[x][y] + ar2[x][y] for y in xrange(MAX)] for x in xrange(MAX)]

def div_by_pos (ar1, val, MAX):
	return [[ ar1[x][y]/4 for y in xrange(MAX) ] for x in xrange(MAX) ]

def root_by_pos(ar1, root, MAX):
	return [[ ar1[x][y]**(1/root) for y in xrange(MAX)] for x in xrange(MAX)] 

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