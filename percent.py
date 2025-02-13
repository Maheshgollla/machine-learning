import numpy
def percentile(x,y):
    return numpy.percentile(x,y)
if __name__=="__main__":
    arr=[]
    n=int(input('enter array size: '))
    for i in range(n):
        a=int(input(f"Enter element number {i}: "))
        arr.append(a)
    z=int(input("Enter percnetage: "))
    print(arr)
    print(percentile(arr,z))