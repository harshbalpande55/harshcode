fibtable =[]
n= int(input('enter the value to be known :'))
def fib(n):
    fibtable.append(0)
    fibtable.append(1)
    for i in range(2,n+1):
        fibtable.append(fibtable[i-1]+fibtable[i-2])
    return(fibtable[n])
t =fib(n)
print(t)