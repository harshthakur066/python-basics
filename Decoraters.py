# decoraters give extra functionality to the functions in python


def my_decorater(func):             # decorater pattern
    def wrap_func(*args, **kwargs):
        print('************')
        func(*args, **kwargs)
        print('************')
    return wrap_func


@my_decorater
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('hiiii')
