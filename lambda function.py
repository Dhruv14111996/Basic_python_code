
from functools import reduce


my_list = [1, 2, 3, 4, 5]
your_list = [10, 20, 30, 40, 50]


# def multiply_by2(items):
#     return items*2
# Insted of above function here we use "Lambda Function" which make our code clean.
print(list(map(lambda items: items*2, my_list)))


# def only_odd(items):
#     return items % 2 != 0
# Same here we also use "Lambda Function" in filter option.
print(list(filter(lambda items: items % 2 != 0, my_list)))


# def accumulator(acc, items):
#     print(acc, items)
#     return acc + items
# We can also use "Lambda Function" in reduce.
print(reduce(lambda acc, items: acc + items, my_list))
