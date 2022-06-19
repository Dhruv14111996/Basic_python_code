class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):  # run is object
        print('run')
        return self

# In this @classmethod it same work like the previous but here we need to write cls insted of self.
# cls  define PlayerCharater.

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Minesh', num1 + num2)

# In this @staticmethod it same work like the previous but here we don't need to write anything.
# In this method we don't care about the attributes.

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Dhruv', 25)
player2 = PlayerCharacter('Priti', 50)
player3 = PlayerCharacter.adding_things(10, 5)
player4 = PlayerCharacter.adding_things2(15, 5)

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player3.name, player3.age)
print(player4)
