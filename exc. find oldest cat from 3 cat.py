class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


sweety = Cat('sweety', 2)
jeney = Cat('jeney', 5)
clary = Cat('clary', 3)


def get_old_cat(*args):
    return max(args)


print(
    f'The oldest cat is {get_old_cat(sweety.age,jeney.age,clary.age)} years old.')
