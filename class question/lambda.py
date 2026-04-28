x=lambda a,b,c:a+b+c
print("Addition:",x(10,20,30))

result = lambda num: "even" if num%2==0 else"odd"
print(result(12))

result = lambda num: num*num
print("square:",result(5))

result = lambda num: num*num*num
print("cube:",result(2))

result = lambda a,b: "a is max" if a>b else"b is max"
print("minandmax:",result(4,5))
