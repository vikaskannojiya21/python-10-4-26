numbers = [3, 5, 4]

for n in numbers:
    fib = []
    a= 0
    b= 1

    for i in range(n):
        fib.append(a)
        a,b=b,a+b

    print("Fibonacci for", n, ":", fib)
