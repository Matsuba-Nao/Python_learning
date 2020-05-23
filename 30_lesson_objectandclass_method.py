class Person(object):

    kind = "human"

    def __init__(self):
        self.x = 100


    # def what_is_your_kind(self):
    #     return self.kind
    #オブジェクトselfではなくクラスclsメソッドとして定義できる
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    #外においてもいい関数を中に入れる。あまり使う機会はないかも
    @staticmethod
    def about(year):
        print("about human {}".format(year))

a = Person()
print(a.what_is_your_kind())
#print(a.x)
#b = Person
#()を付けないとオブジェクトを作っていない
#print(b.x)
#ただしクラス変数は見れる
#print(b.kind)

#クラスメソッドはオブジェクトを作らなくてもアクセスできる
print(Person.kind)
print(Person.what_is_your_kind())

Person.about(1999)