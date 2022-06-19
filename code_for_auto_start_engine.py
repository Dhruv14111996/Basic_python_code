# This code write for car company who make auto cars. Like "Tesla".

age = input('what is your age')

if int(age) < 18:
    print('your age is not enough to drive car. engine off')

elif int(age) > 18:
    print('your age is enough to drive car. engine On')

elif int(age) == 18:
    print('Congratulation you are young enough to drive car. enjoy on your first ride')
