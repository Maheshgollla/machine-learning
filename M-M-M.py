import numpy
from scipy import stats
x=[99,86,87,88,111,86,103,87,94,78,77,85,86]
y=numpy.mean(x)
z=numpy.median(x)
v=stats.mode(x)
print(y,z,v)