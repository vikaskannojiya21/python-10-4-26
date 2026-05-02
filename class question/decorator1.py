def my_deco(func):
    def wrapper():
        print("before calling the function")
        func()
        print("after calling the function")
    return wrapper
@my_deco
def vikas():
    print("hello world")
vikas()
