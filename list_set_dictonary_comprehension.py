# If i wants to creat one list and in fast way what i need to do ?

# my_list = []

# for chr in 'hellloooo':
#     my_list.append(chr)

# print(my_list)

# using this code i generate my_list like['h', 'e', .......] but insted of this we use comprehemsion.

# it generate same list and its called list comprehension its so clean and easy way to generate list.
my_list = [chr for chr in 'hellloooo']

# If i want to generate list from 0 to 100 then its very simple.

my_list1 = [num for num in range(0, 101)]

# If i want to generate list but all list is multipy by 2 then how i can write?

my_list2 = [num*2 for num in range(0, 101)]

# If i wants only even number in range of 0 to 100 then how i can write code.

my_list3 = [num for num in range(0, 101) if num % 2 == 0]

# print(list(range(0, 101))) # this is also one way to generate fast list.
print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)

print('----------------------------------------------------------------------------------------')

# Set Comprehension
# It same like List but in Set we need to write same things in {} this brecket\
# But in set we need to remeber one thing that it only gives uniqe number he didnt give duplicates.

# it generate same Set and its called Set comprehension its so clean and easy way to generate list.
my_set = {chr for chr in 'hellloooo'}

# If i want to generate Set from 0 to 100 then its very simple.

my_set1 = {num for num in range(0, 101)}

# If i want to generate Set but all Set is multipy by 2 then how i can write?

my_set2 = {num*2 for num in range(0, 101)}

# If i wants only even number in range of 0 to 100 then how i can write code.

my_set3 = {num for num in range(0, 101) if num % 2 == 0}

print(my_set)
print(my_set1)
print(my_set2)
print(my_set3)

print('----------------------------------------------------------------------------------------')

# Dictonary Comprehesion
# In Dictonary we need Key and Valuse so its little tricky.
# for example i want to creat dictonary and its value is multiply by 2 the how i can do?

simple_dict = {
    'a': 2,
    'b': 4
}

my_dict = {key: value*2 for key, value in simple_dict.items()}

print(my_dict)

# Insted of this we can write like this also.

my_dict = {num: num*2 for num in [1, 2, 3, 4]}

print(my_dict)

# Excersice
# If i have some duplicates in list and i want to find which is duplicate string thw how I can find?

Some_list = ['a', 'b', 'd', 'b', 'm', 'n', 'n']

duplicates = list(set([x for x in Some_list if Some_list.count(x) > 1]))

print(duplicates)
