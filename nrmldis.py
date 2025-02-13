import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 50)

plt.hist(x, 10)
plt.show()