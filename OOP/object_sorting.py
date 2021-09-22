class Toy:
    def __init__(self, name, price):
        # instance variables
        self.name = name
        self.price = price

    # Method
    def sort_priority(self):
        return self.price


def print_toy_objects(toy_list):
    for obj in toy_list:
        print(f'Toy: {obj.name}, Price: {obj.price}')


toy_1 = Toy('Woody', 1000)
toy_2 = Toy('Aot-wheels', 200)
toy_3 = Toy('abc', 10)

toys = [toy_1, toy_2, toy_3]

# Using sort function, key= keyword argument, we can pass function here
toys.sort(key=Toy.sort_priority, reverse=True)

print_toy_objects(toys)

# Using sorted function
sorted_toys = sorted(toys, key=Toy.sort_priority)

print_toy_objects(sorted_toys)

# lambda Function

result = lambda x, y, z: x + y + z

print(result(1, 2, 3))

new_toys = [toy_1, toy_2, toy_3]
# using lambda function with sort()
new_toys.sort(key=lambda x: x.price)

print_toy_objects(new_toys)

# Using the sorted function with lambda function

Sorted_toys_again = sorted(toys, key=lambda x: x.price)
print_toy_objects(Sorted_toys_again)
