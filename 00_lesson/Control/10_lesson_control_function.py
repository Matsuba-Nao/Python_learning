# def say_something(word):
# 入力を自動でタプル型に入れる
# def say_something(*args):
#     print(args)
#     for arg in args:
#         print(arg)

# say_something("Hi", "Mike", "Nance")

# アンパッキング化してから入れることもできる


def say_something(word, *args):
    print(args)
    for arg in args:
        print(arg)


t = ("Mike", "Nancy")
say_something("Hi", *t)

# def menu(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#     print(kwargs)

# d = {
#     "entree": "beef",
#     "drink": "ice coffee",
#     "dessert": "ice"
# }
# #menu(entree = "beef", drink = "coffee")
# menu(**d)

# def menu(food, *args, **kwargs):
#     print(food)
#     print(args)
#     print(kwargs)

# menu("banana", "apple", "orange", entree="beef", drink="coffee")

# docstringの記述方法
# def example_func(param1, param2):
#     """Example docstring
#     Args:
#     Returns:
#     """
#     print(param1)
#     print(param2)
#     return True

# print(example_func.__doc__)

# 関数内関数innerfunction
def outer(a, b):
    def plus():
        return a + b
    r1 = plus()
    #関数内関数でも外側の関数の変数を使える
    #r2 = plus(b,a)
    print(r1)

outer(1, 2)

