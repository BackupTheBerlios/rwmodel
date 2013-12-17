from __future__ import division
#-*- coding: utf-8 -*-
#!/usr/bin/python
#name: object_knowledge_update
#author: Erik Lux
#date: 20130615
#purpose: incrementally update knowledge over the grid


def oku(grid, b):
  print "Object knowledge update started ...\n"
  _start = time.time()
  for t in xrange(2,grid.time+1):    #!!!times+1
    #incremental phase
    print "Suma calculation started ...\n"
     
    for x in xrange(grid.X):
      for y in xrange(grid.Y):
        multiplicant =1
        multiplicant1 =1
        suma =1
        (ant_size, xl, xr, yl, yr) = calc_antecedent_bounds(x,y)
        for j in range(xl, xr):
          for i in range(yl, yr):
            multiplicant *= grid.I[b][t-1][j][i]
        multiplicant = multiplicant**(1/ant_size)

        for j in range(x-x1, x+x2):
          for i in range(y-y1, y+y2):
            multiplicant1 = multiplicant * dynamic_object_model(b,t,j, i)
            multiplicant1 = multiplicant1**(1/2)
            suma *= multiplicant1
        suma = suma **(1/ant_size)
        suma*= observation_model(b,t,x,y)
        #suma /= ant_size
        grid.I[b][t][x][y] = suma
    
    min_max_normal(grid.I[b][t], False)#normalize(b,t)
    print "Time: ", t
  print "Object knowledge update successfully finished ..."
  grid.flag_I = True

