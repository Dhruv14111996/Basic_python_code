from functools import reduce


my_list = [1, 2, 3, 4, 5]
your_list = [10, 20, 30, 40, 50]


def multiply_by2(items):
    return items*2


def only_odd(items):
    return items % 2 != 0


def accumulator(acc, items):
    print(acc, items)
    return acc + items


print(list(map(multiply_by2, my_list)))
print(list(filter(only_odd, my_list)))
# In zip if we need to def zip we need two list.
print(list(zip(my_list, your_list)))
# Reduce function reduce the num in the end we get only final number
print(reduce(accumulator, my_list, 10))
