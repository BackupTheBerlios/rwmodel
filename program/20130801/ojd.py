#-*- coding: utf-8 -*-
#! python
#name: object_joint_distribution
#author: Erik Lux
#date: 20130615
#purpose:joint distribution in object model without diff between targets and distractors 
#import imp
#mod = imp.load_source('grid', 'grid.py')
#from grid import *
import time
from bigfloat import *

#P(OVM)
def ojd():
  print "Object Joint Distribution started ...\n"
  start_ = time.time()
  result =BigFloat(1)
  for t in range(1,times+1):
    result1 =BigFloat(pmt(t)) 
    for x in xrange(X):
      for y in xrange(Y):
        result1*= ( observation_model(t,x,y)\
        *dynamic_object_model(t,x,y))		
    
    result *=result1
    print "Partial result for time ", t, "is ", result1, " ...\n"
  
  result *= occupancy_vs()*result1
  end_ = time.time()
  print "Object Joint Distribution: ", result
  print 'Elapsed time is ',(end_-start_)/60, "minutes"
  return result

f = open('ojd.out', 'w')
ojd()
f.flush()
f.close()
