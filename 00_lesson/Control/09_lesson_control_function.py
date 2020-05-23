# def say_something():
#     #print("hi")
#     s = "hi"
#     return s

# say_something()
# # print(type(say_something))
# # f = say_something
# # f()
# result = say_something()
# print(result)


def what_is_this(color):
    # print(color)
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green pepper"
    else:
        return "I don't know"


# result = what_is_this("red")
# print(result)

# # num: int = 10


# def add_num(a: int, b: int) -> int:
#     return a + b

# r = add_num(10, 20)
# # 間違えたものを入れてもそのまま返してはくれる
# # r = add_num("a", "b")

# print(r)

# デフォルト引数
def menu(entree="beef", drink="wine", dessert="ice"):
    print(entree)
    print(drink)
    print(dessert)


# キーワードアーギュメント
# 順序を間違えても正しく入る
#menu(entree="beef", drink="beer", dessert="ice")
# menu("chicken")

# デフォルト引数で気を付けること
# リストや辞書はデフォルト引数で渡すべきでない
# 参照渡しとなるためスコープが関数内で終わらないリストになる
# 引数に何も入っていないときはNoneとして処理
# def test_func(x, l=[]):
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

# y = [1,2,3]
# r = test_func(100,y)
# print(y)


r = test_func(100)
print(r)
r = test_func(100)
print(r)
r = test_func(100)
print(r)
