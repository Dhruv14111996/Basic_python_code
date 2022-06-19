# range

for i in range(2):  # it generate 0 to 10 list twice.
    print(list(range(0, 11)))

# enumerate

for i, chr in enumerate(list(range(1, 100))):
    print(i, chr)
    if chr == 37:
        print(f'index of 37 is: {i}')
