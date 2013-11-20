from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: object_knowledge_update
#author: Erik Lux
#date: 20130615
#purpose: incrementally update knowledge over the grid

import time

def oku(b):
  print "Object knowledge update started ...\n"
  _start = time.time()
  for t in xrange(2,times+1):    #!!!times+1
    #incremental phase
    print "Suma calculation started ...\n"
     
    for x in xrange(X):
      for y in xrange(Y):
        multiplicant =1
        multiplicant1 =1
        suma =0

        x1 = min(x-bound1, antecedent)
        x2 = min(bound2 -x, antecedent+1)
        y1 = min(y -bound1, antecedent)
        y2 = min(bound2 - y, antecedent+1)
          
        ant_size = (x1+x2)*(y1+y2) #size of antecedent cells
        
        xl = x-int(x1)
        xr = x+int(x2)
        yl = y-int(y1)
        yr = y+int(y2)
        for j in range(xl, xr):
          for i in range(yl, yr):
            multiplicant *= I[b][t-1][j][i]
        multiplicant = multiplicant**(1/ant_size)

        for j in range(x-x1, x+x2):
          for i in range(y-y1, y+y2):
            multiplicant *= dynamic_object_model(b,t,j, i)
            suma += multiplicant
        suma *= observation_model(b,t,x,y)
        suma /= ant_size
        I[b][t][x][y] = suma
    
    min_max_normal(I[b][t], False)#normalize(b,t)
    print "Time: ", t
  print "Object knowledge update successfully finished ..."
#f = open('oku.out', 'w')
for b in xrange(blocks):
  oku(b)
#f.close()
