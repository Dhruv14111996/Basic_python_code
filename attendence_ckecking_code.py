# We write this program to check who is absent in classroom so techer call their perents.
school = {'Dhruv', 'Priti', 'minesh', 'mansi', 'Hiren',
          'Kuldeep', 'Arjun', 'Medha', 'Nandu', 'dhruv', 'priti'}
attendance_list = {'Dhruv', 'Priti', 'minesh', 'mansi',
                   'Hiren', 'Arjun', 'Nandu', 'dhruv', 'priti'}

print(school.difference(attendance_list))
