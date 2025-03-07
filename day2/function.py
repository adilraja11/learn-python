# Reusable Function with Return

def sum(x,y):
    return x + y

result_a = sum(1,2)
result_b = sum(result_a, 5)

# *args
def say_name(*args):
    name_2, name_1, name_3 = args # destructure
    print(f'Name: {name_1}')

say_name("Adil", "Raja", "Doni") # result: Raja

# *kwargs = Keyword Args
def say_my_name(**kwargs):
    # name_a = kwargs['name_a'] UNSAFE
    name = kwargs.get("name_x", None)
    print(name)
    pass

say_my_name(name_a='Adil', name_b='Doni') # None

# default args rules

def sample(regular, with_default="value", *args, **kwargs):
    print(regular)
    print(with_default)
    print(args[0])
    print(kwargs.get("my_input"))
    pass

