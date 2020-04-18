# default mode parameter of open is r for read but to read and write we pass r+

with open('test.txt', mode='r+') as file:
    print(file.readlines())
    text = file.write('\nEdit max. ')

with open('auto.txt', mode='w') as file:
    # print(file.readlines())
    text = file.write('New file made through command')

with open('dir/in.txt', mode='r') as file:
    print(file.read())
