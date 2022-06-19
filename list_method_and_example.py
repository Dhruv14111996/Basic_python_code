# List Method
# .append # to add somthing in end od list
# .insert # add something between list or end of list
# .pop # for remove
# .remove # use to remove some specific things
# .clear # clear the whole index
# .index # use to count the place
# .count # it count how many same latter in list
# .sort # it make in correct place
# .reverse # it reverse the whole list

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
bucket.append('x')
print(bucket)

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
bucket.insert(2, 'x')
print(bucket)

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
bucket.pop()  # pop remove last variable from list.
print(bucket)

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
bucket.remove('d')  # remove is removing perticular variable.
print(bucket)

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
bucket.clear()
print(bucket)

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
print(bucket.index('c'))

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
print(bucket.count('d'))

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
bucket.sort()
print(bucket)

bucket = ['a', 'b', 'c', 'd', 'e', 'b']
bucket.reverse()
print(bucket)
