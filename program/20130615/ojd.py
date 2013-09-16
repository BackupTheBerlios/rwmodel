#-*- coding: utf-8 -*-
#! python
#name: object_joint_distribution
#author: Erik Lux
#date: 20130615
#purpose:joint distribution in object model without diff between targets and distractors 
#import imp
#mod = imp.load_source('grid', 'grid.py')
#from grid import *
from datetime import datetime
from bigfloat import *

#P(OVM)
def ojd():
  start_ = datetime.now()
  result =BigFloat(1)
  for t in range(1,times+1):
    result1 =BigFloat(pmt(t)) 
    for x in xrange(X):
      for y in xrange(Y):
        result1*= ( observation_model(t,x,y)\
        *dynamic_object_model(t,x,y))		
    
    result *=result1

    print >> f, 't: ', t,', result1: ', result1
  
  result *= occupancy_vs()*result1
  print >> f, 'occupancy:', occupancy_vs(), 'result:', result1
  end_ = datetime.now()
  print >> f, 'Elapsed time is ',(end_-start_).microseconds
  return result

f = open('ojd.out', 'w')
ojd()
f.flush()
f.close()
