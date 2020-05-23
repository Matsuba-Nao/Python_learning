def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        # ここのfuncでadd_numを実行している
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print("func:", func.__name__)
        print("args:", args)
        print("kwargs:", kwargs)
        # ここのfuncでadd_numを実行している
        result = func(*args, **kwargs)
        print("result:", result)
        return result
    return wrapper

#@をつけることでaddnumを呼び出した時にprintinfoが呼び出されるようになる
@print_info
@print_more
def add_num(a,b):
    return a + b

#add_num(1,2)

#イメージとしては以下の包み込んでいる感じ
#f = print_info(print_more(add_num))
#r = f(10,20)

r = add_num(10,20)
print(r)
print(type(r))

# #関数を引数として渡す
# f = print_info(add_num)
# r = f(10,20)
# print(r)
