class User:

    def login(self):
        return 'logged in'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} is Attacking with {self.power} power')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name} is Attacking with {self.num_arrows}')



wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

