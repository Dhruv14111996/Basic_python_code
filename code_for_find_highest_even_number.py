def highest_even(li):
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)


print(highest_even([2, 4, 6, 8, 4, 5, 10, 20, 15, 11, 28]))
