class user():
    # now here if i want to print wizerd email so i need to use 'super()'.
    def __init__(self, email):
        self.email = email

    def log_in():
        print('you logged in.')

# inheritance means how we know that wizerd is log in or not so for that we need to define user.


class wizerd(user):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(
            f'Your email is: {self.email}. \nyou attaking with power of: {self.power}.')


class Archer(user):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(
            f'your email is: {self.email}. \nyou attaking with num_arrowa-left_arrows: {self.num_arrows}')


wizerd1 = wizerd('priti', 60, 'priti@yahoo.com')
Archer1 = Archer('Dhruv', 100, 'dhruv1@gmail.com')


wizerd.log_in()
print(wizerd1.name)
# print(wizerd1.email)
wizerd1.attack()

Archer.log_in()
print(Archer1.name)
Archer1.attack()
