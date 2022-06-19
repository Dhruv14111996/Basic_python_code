# OOP (Object Oriented Program.)
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):  # run is object
        print('run')
        return self


player1 = PlayerCharacter('Dhruv', 25)
player2 = PlayerCharacter('Priti', 50)

print(player1.name, player1.age)
print(player2.name, player2.age)
