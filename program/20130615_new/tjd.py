#-*- coding: utf-8 -*-
#! python
#name: itarget_joint_distribution 
#author: Erik Lux
#date: 20130615
#purpose: joint distribution in target model, distinguishing between targets and objects
mod = imp.load_source('grid', 'grid.py')
from grid import *
from datetime import datetime
from bigfloat import *

#P(OVMT)
def tjd():
  start_= datetime.now()

  result = 1
  for t in range(1,times+1):
    
    result1 = 1
    for x in xrange(X):
      for y in xrange(Y):
        result1 *=(observation_model(t,x,y)
					*dynamic_object_model(t,x,y))		
    result2 = 1
    for i in xrange(targets):
      result2 *= dynamic_target_model(t,i)
    result *= (result1*result2*pmt(t)) 
  
  result *=(occupancy_vs_targets()*occupancy_vs())
  end_ = datetime.now()
  print 'Elapsed time: ', (end_-start_).microseconds
  return result


