class Player:
    def __init__(self, name, age):
        membership = True  # class object attribute --> static
        self.name = name  # attributes or properties --> dynamic
        self.age = age

    def run(self):  # methods
        return 'done'

    def test(self):
        return self
    # staticmethod are for methods for class just like class object attributess
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    # classmethods are for intantiating new objects giving certain default attributes
    # and can be use as same as staticmethods with an extra argument
    @classmethod
    def add_player(cls, num1, num2):
        return cls('Tom', num1 + num2)


player1 = Player('Bob', '22')
player2 = Player('Jhon', '34')
player2.score = 122

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player2.score)
print(player1.run())

print('static', Player.add(2, 3))  # staticmethod

player3 = Player.add_player(10, 13)  # classmethod

print(player3.name, player3.age)

player4 = Player('Mark', '26')

print(player4.test())
