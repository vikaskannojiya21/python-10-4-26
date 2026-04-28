def fibonaci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
fib=fibonaci(5)

for i in fib:
    print(i,end=" ")
