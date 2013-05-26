#-*- coding: utf-8 -*-
#! python
#name: testmodule
#author: Erik Lux
#date: 20130501
#purpose: test parts of program

import re #regular expresions
array = [0 for i in xrange(6)]
def load_data(file_name):
	f = open(file_name, 'r')
	for line in f:
		#print re.split(r'[, \n]+', line) 
		temp =line.split()	
		for i in xrange(len(temp)):
			array[i] = temp[i] 
	f.close()
print 'array', array
