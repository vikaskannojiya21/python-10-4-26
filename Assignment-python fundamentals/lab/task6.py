def even_numbers():
    num = 2
    for i in range(10):
        yield num
        num += 2


for value in even_numbers():
    print(value)
print("*"*50)
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


numbers = [10, 20, 30, 40, 50]

it = MyIterator(numbers)

for num in it:
    print(num)
