# def do_ten(func):
#     for i in range(10):
#         func()


# def hello_world():
#     print('hello world')


# do_ten(hello_world)

###############################

# def do_ten(func):
#     def wrapper():
#         for i in range(10):
#             func()
#     return wrapper


# @do_ten
# def hello_world():
#     print('hello world')


# hello_world()

###################################

def do_ten(word):
    def wrapper1(func):
        def wrapper2():
            for i in range(10):
                func(word)
        return wrapper2
    return wrapper1


@do_ten('word')
def hello_world(word='world'):
    print(f'hello {word}')


hello_world()

# Page to help
# https://realpython.com/primer-on-python-decorators/
