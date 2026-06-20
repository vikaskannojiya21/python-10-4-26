def deco_vikas(func):
         def wrapper():
             print("before calling the function")
             func()
             print("After calling the function")

        return wrapper
        
@deco_vikas
def say_hello():
    print("hello world")

say_hello()
