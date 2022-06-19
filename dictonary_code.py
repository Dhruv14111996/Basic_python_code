user = {
    'age': 22,
    'username': 'Dhruv',
    'weapons': ['AWM'],
    'is_active': True,
    'clan': 'Pochionki'
}

user['weapons'].append('mini')
user['weapons'].append('M24')
# update is use to add something in dictornary or in set.
user.update({'is_banned': False})
user['is_banned'] = True
print(user.values())  # this line help us to find only Values parameters
print(user.keys())  # this line help us to find only key parameters
print(user)
