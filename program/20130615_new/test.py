import numpy
execfile('SmallFloat.py')
r = numpy.random.uniform()
print r
a = Small(r)
print 'a created ...'
a.p()
b = Small(1)
c = Small(0.1)
b.p()
c.p()

