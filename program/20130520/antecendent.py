cells = [[(0,0) for i in xrange(5)] for j in xrange(5)]

antecedent = 2
bound1 = 0
bound2 =len(cells)

x = 1 
y = 3

x1 = min(x -bound1, antecedent)
x2 = min(bound2 -x, antecedent+1)

y1 = min(y - bound1, antecedent)
y2 = min(bound2 - y, antecedent+1)
print x-x1,y-y1,x+x2,y+y2

for j in range(x-x1, x+x2):
  for i in range(y-y1, y+y2):
    if j!=x or i!=y:
      cells[j][i] = (j,i) 

print cells[0]
print cells[1]
print cells[2]
print cells[3]
print cells[4]

