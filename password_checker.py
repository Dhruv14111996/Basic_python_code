username = input('what is your username?')
password = input('what is your password?')
password_lenght = len(password)
hidden_password = '*' * (password_lenght)

print(
    f'Helllooo {username},\nyour password {hidden_password} is {password_lenght} letters long')
