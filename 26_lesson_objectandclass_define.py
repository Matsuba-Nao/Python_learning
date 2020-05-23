# python3では別にobjectを書かなくてもよい
# python2の名残で、継承するときは書いた方がよいということもある

#selfは自分自身のインスタンスを表す
class Person(object):
    # C++でいうコンストラクタ
    # クラスの場合はselfがないと保持されないので注意
    def __init__(self, name="Default"):
        self.name = name
        # print(self.name)

    def say_something(self):
        print("I am {}. Hello".format(self.name))
        self.run(10)

    def run(self, num= 0):
        print("run" * num)

    #デストラクタ
    def __del__(self):
        print("good bye")

person = Person("Mike")
person.say_something()

del person

print("#################")
