#-*- coding: utf-8 -*-
#! python
#name: object_joint_distribution
#author: Erik Lux
#date: 20130615
#purpose:joint distribution in object model without diff between targets and distractors 
import imp
mod = imp.load_source('grid', 'grid.py')
from grid import *
from datetime import datetime
from bigfloat import *

#P(OVM)
def ojd():
  start_ = datetime.now()
  result =1
  for t in range(1,times+1):
    print 't: ', t,', result: ', result
    result1= 1
    for x in xrange(X):
      for y in xrange(Y):
        result1*= ( observation_model(t,x,y)\
        *dynamic_object_model(t,x,y))		
    
    with precision(100):
      result *= pmt(t) * result1
  
  with precision(100):	
	  result *= occupancy_vs()
  end_ = datetime.now()
  print 'Elapsed time is ',(end_-start_).microseconds
  return result


