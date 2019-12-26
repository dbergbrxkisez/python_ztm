# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name  # attributes | Pieces of data that are dynamic
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Tom', 10)
# player2 = PlayerCharacter()
# player2.attack = 50

# print(player1.na`me)
# print(player1.run())
# print(player2.membership)
# print(player2.age)
# print(player2.attack)
print(player1.shout())
# print(player2.shout())
# print(player1.run('hello'))
