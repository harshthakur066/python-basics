# Only two types of looping in python

games = ['Football', 'Cricket', 'Vollyball', 'Basketball']

# For
for name in games:
    print(name)

print()

for i in range(0, 20, 2):
    print(i)

print()

for i, char in enumerate([1, 2, 4, 5, 7, 54, 6]):
    print(i, char)

print()

# While
index = 0
while index < len(games):
    print(games[index])
    index = index + 1
