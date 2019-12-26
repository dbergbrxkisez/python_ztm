# It abstracts the data so that we don't need to think about it
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def run(self):
    print('run')


def speak(self):
    print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('andrei', 100)
print((1, 2, 3, 1).count(1))
print(len(1, 2, 3, 1))

player1.name = "!!!"
player1.speak = 'Boooo'

print(player1.speak)
