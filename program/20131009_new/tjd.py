#-*- coding: utf-8 -*-
#! python
#name: itarget_joint_distribution 
#author: Erik Lux
#date: 20130615
#purpose: joint distribution in target model, distinguishing between targets and objects
#import imp
#imp.load_source('grid', 'grid.py')
#from grid import *
import time
from bigfloat import *

#P(OVMT)
def tjd():
  print "Target Joint Distribution started ...\n"
  start_= time.time()

  result = BigFloat(1)
  for t in range(1,times+1):
    
    result1 = BigFloat(1)
    for x in xrange(X):
      for y in xrange(Y):
        result1 *=(observation_model(t,x,y)
					*dynamic_object_model(t,x,y))

    result2 = BigFloat(1)
    for i in xrange(targets):
      result2 *= dynamic_target_model(t,i)
    result *= (result1*result2*pmt(t)) 
  
    print "Partial result for time: ", t, "is dynamic_target_model ", result2
    print "and observation_model ", result1, "\n"
  result *=(occupancy_vs_targets()*occupancy_vs())
  end_ = time.time()
  print "Target Joint Distribution: ", result
  print 'Elapsed time: ', (end_-start_)/60, "minutes"
  return result

f = open('tjd.out', 'w')
tjd()
f.flush()
f.close()
