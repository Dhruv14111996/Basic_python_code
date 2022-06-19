my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9}

print(my_set.difference(your_set))

my_set.discard(your_set)
print(my_set)

print(my_set.difference_update(your_set))
print(my_set)

print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(my_set | (your_set))  # This is union. it also indicate like | .
