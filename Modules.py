import random
import pyjokes

print(random.random())

print(random.randint(1, 99))

print(pyjokes.get_joke('en', 'neutral'))


d = {'a': 2}
d['b'] = 1
d['c'] = 4

d2 = {'a': 2}
d2['c'] = 4
d2['b'] = 1

print(d == d2)
