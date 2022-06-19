from multiprocessing.sharedctypes import Value


def fizzbuss(num):

    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')

    elif num % 3 == 0:
        print('Fizz')

    elif num % 5 == 0:
        print('Buzz')


fizzbuss(60)

''' Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
 between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated
sequence on a single line.'''

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=',')

'''Write a program which can compute the factorial of a given numbers.The results should be printed
in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320'''

num = int(input('\nyou want to find factorial of which number:-'))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1
print(fact)

# Other way to find factorial by using for loop.

n = int(input('\nyou want to find factorial of which number:-'))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)

'''With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such
that is an integral number between 1 and n (both included). and then the program should print
the dictionary.Suppose the following input is supplied to the program: 8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

n = int(input('\nnumber:-'))

my_dict = {i: i*i for i in range(1, n+1)}
print(my_dict)

'''Write a program which accepts a sequence of comma-separated numbers from console and generate
a list and a tuple which contains every number.Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

print = (tuple(input("Enter a series of numbers separated by a comma :").split(',')))

''' '''
