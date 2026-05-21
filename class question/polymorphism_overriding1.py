class A:
    def show(self):
        print("hello")
class B:
    def show(self):
        super(.show())
        print("world")
b1=B()
b1.show()
