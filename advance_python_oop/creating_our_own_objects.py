# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name  # attributes | Pieces of data that are dynamic
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1+num2)

    @staticmethod
    def adding_thing(num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Tom', 10)
# player2 = PlayerCharacter()
# player2.attack = 50

# print(player1.na`me)
# print(player1.run())
# print(player2.membership)
# print(player2.age)
# print(player2.attack)
# print(player1.shout())
# print(player2.shout())
# print(player1.run('hello'))


player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)
