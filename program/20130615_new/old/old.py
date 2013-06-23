#-*- coding: utf-8 -*-
#! python
#name: old
#author: Erik Lux
#date: 20130615
#purpose: old source code

#P(O^t|V^(1->t) M^(1->t)
def knowledge_update():
  start_ = datetime.now()
  t = times
  for x in xrange(X):
    for y in xrange(Y):
      grid_inference[x][y] = knowledge_update_recursive(t,x,y)
      end_ = datetime.now()
      print 'Elapsed time is ',(end_-start_).microseconds

def knowledge_update_recursive(t,x,y):
	#P(O^1_(x,y)|V^1 M^1) value at the end of recursion
	result = 1
	if t != 2:
		for i in xrange(len(antecedent_cells[t])):
			result = result*\
			knowledge_update_recursive(t-1,antecedent_cells[t][i][0],antecedent_cells[t][i][1])
		
	result2 = 0
	for i in xrange(len(antecedent_cells[t])):
		result2 = result2+\
		dynamic_object_model(t, antecedent_cells[t][i][0], antecedent_cells[t][i][1])*result
	
	result2 = result2*observation_model(t,x,y)
	#print "Result2:", result2
	return result2


