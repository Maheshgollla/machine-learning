import numpy
from scipy import stats
def avg(x):
    return numpy.mean(x)
def med(Y):
    return numpy.median(Y)
def mod(z):
    return stats.mode(z)
if __name__=="__main__":
    arr=[]
    n=int(input('enter array size: '))
    for i in range(n):
        a=int(input(f"Enter element number {i}: "))
        arr.append(a)
    print(arr)
    print(avg(arr),med(arr),mod(arr))
    
           