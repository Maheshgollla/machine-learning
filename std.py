import numpy
def std_dev(x):
    speed= numpy.std(x)
    return speed
def vari(x):
    z=numpy.var(x)
    return z
if __name__=="__main__":
    x=[]
    n=int(input('enter array size: '))
    for i in range(n):
        a=int(input(f"Enter element number {i}: "))
        x.append(a)
    print(x)
    print(vari(x),std_dev(x))