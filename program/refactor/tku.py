from __future__ import division 
#-*- coding: utf-8 -*-
#! python
#name: target_knowledge_update
#author: Erik Lux
#date: 20130619
#purpose: incrementally update knowledge over targets
#modification: using my own class SmallFloat for working with very small or big probabilities probabilities


def tku(grid, b):
  print "Target knowledge update started ..."
  start_ = time.time()
  IT_i= [ [ [ 0
			for x in xrange(grid.X) ]
				for y in xrange(grid.Y) ]
					for i in xrange(grid.targ_size) ]

  for t in range(2,grid.time+1 ):  #times+1
    print 'time is:' , t
    for i in xrange(grid.targ_size):
      for x in xrange(grid.X):
        for y in xrange(grid.Y):
          (ant_size, xl, xr, yl, yr) = calc_antecedent_bounds(x,y)
          suma1 = 0
          
          for j in range(xl, xr):
            for k in range(yl, yr):
              suma1 += (target_observation_model(b,t,i,j,k)*grid.I[b][t][j][k])
          suma1 /= ant_size
          IT_i[i][x][y] = suma1
          grid.IT_bit[b][i][t][x][y] = suma1
    print "over targets ..."

    for x in xrange(grid.X):
      for y in xrange(grid.Y):
        suma2 = 0
        for i in xrange(grid.targ_size):
          suma2 += IT_i[i][x][y]#*I_T[t-1][x][y]
        suma2 /=grid.targ_size
        grid.IT[b][t][x][y] = suma2
    min_max_normal(grid.IT[b][t], True)#normalize(b,t)
  
  grid.flag_IT = True
  end_ = time.time()
  print "Target knowledge update finished ..."
  print 'Elapsed time is ',(end_-start_)/60, 'minutes'
  



