import re

pattern = re.compile('[a-zA-z0-9#$@%]{8,}\d')

# Password must be 8 letter long
# Password contain minimum 2 capital latter.
# Password contain one uniq sign like #$@%
# Password end with any digit from 0-9

password = 'DhruvP@1411'

a = pattern.fullmatch(password)
print(a)
