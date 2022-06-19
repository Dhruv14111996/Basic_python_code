# While Loop example 1
i = 0
while i < 6:
    print(i)
    i += 1
    break
    i += 1

else:
    print('Done with all work')

# Example 2

while True:
    responce = input('say something: ')
    if(responce == 'bye'):
        break

# Example 3

z = 0

while z < 3:
    if z == 0:
        print("z is", z)
        z += 1
    elif z == 1:
        print("z is", z)
        z += 1
    else:
        print("z is", z)
        z += 1

# Example 4

fruitsList = ["Mango", "Apple", "Orange", "Guava"]

while fruitsList:
    print(fruitsList.pop())

print(fruitsList)
