def my_decorator(my_function):    # <-- (4)
    def inner_decorator():        # <-- (5)
        print("This happened before!")  # <-- (6)
        my_function()             # <-- (7)
        print("This happens after ")    # <-- (10)
        print("This happened at the end!")    # <-- (11)
    return inner_decorator
    # return None


@my_decorator       # <-- (3)
def my_decorated():    # <-- (2) <-- (8)
    print("This happened!")   # <-- (9)


my_decorated()    # <-- (1)


# Décorer une fonction avec des arguments
def cap_decorator(func):
    def wrapper(name):
        name = name.capitalize()
        func(name)
    return wrapper

@cap_decorator
def print_my_name(name):
    print("Hello world from",name)

@cap_decorator
def say_hello_to_me(name):
    print("Hello to",name)

print_my_name("eyal")
say_hello_to_me("eyal")
# >> Hello world from Eyal
# >> Hello to Eyal

# Décorer une fonction avec un nombre inconnu d'arguments
def cap_decorator(func):
    def wrapper(*args, **kwargs):
        args = [arg.capitalize() for arg in args]
        func(*args, **kwargs)
    return wrapper

@cap_decorator
def describe_me(first_name, last_name, favourite_activity):
    print("I am {} {} and I love {}".format(first_name, last_name, favourite_activity))

@cap_decorator
def describe_my_family(father_name, mother_name, brother_name, sister_name):
    print("The name of my father is", father_name)
    print("The name of my mother is", mother_name)
    print("The name of my brother is", brother_name)
    print("The name of my sister is", sister_name)

describe_me("john", "ricotta", "coding")
describe_my_family("John","Valentina","mario","luigi")



class MyClass:
  def __init__(self, first_name, last_name):
    self.__first_name = first_name
    self.__last_name = last_name

  @property # Permet d'accéder à un attribut privé
  def email(self): 
    return f"{self.__first_name}.{self.__last_name}@gmail.com"

  @email.setter # Permet de modifier un attribut privé 
  def email(self, name): 
    self.__first_name = name

newClass = MyClass("John", "Doe")
newClass.email = "Sarah"
print(newClass.email)
# >> Sarah.Doe@gmail.com