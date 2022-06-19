
def calculator():
    user_condition = int(input('''
    please enter the operation that you want to do.
    your options are:-
    1 Addition
    2 Subtraction 
    3 Multiplication 
    4 Divison
    First think what operation you want to do and then select the operation type:-'''))

    num1 = int(input('Enter your first number:-'))
    num2 = int(input('Enter your second number:-'))

    if user_condition == 1:
        print(num1 + num2)

    elif user_condition == 2:
        print(num1 - num2)

    elif user_condition == 3:
        print(num1 * num2)

    elif user_condition == 4:
        print(num1 / num2)

    user_continues = input(
        '''if you wants to continue your calculation please type "yes" other wise type "bye":-''')

    if user_continues == "yes":
        calculator()
    else:
        print("Bye have a nice day")


calculator()
