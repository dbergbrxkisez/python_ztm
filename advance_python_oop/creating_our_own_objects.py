# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name  # attributes | Pieces of data that are dynamic
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

# print(player1.name)
# print(player1.run())
# print(player2.membership)
# print(player2.age)
# print(player2.attack)
# print(player1.shout())
# print(player2.shout())
print(player1.run('hello'))
