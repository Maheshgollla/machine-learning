import numpy
import matplotlib.pyplot as plt
def histogram(x,y,z):
    return numpy.random.uniform(x,y,z)
if __name__=="__main__":
    lwr=int(input("Enter lower limit: "))
    upr=int(input("Enter upper limit: "))
    rge =int(input("Enter range: "))
    arr=numpy.random.uniform(lwr,upr,rge)
    plt.hist(arr,10)
    plt.show()    