class Person(object):

    # クラスで共有される変数
    # 違うインスタンスでも等しい
    kind = "human"

    def __init__(self, name):
        #self.kind = "human"
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person("A")
a.who_are_you()
b = Person("B")
b.who_are_you()

class T(object):

    #クラス変数でリストを作ると意図しない結果が出ることになる
    #words = []
    def __init__(self):
        self.words = []


    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word("add 1")
c.add_word("add 2")

d = T()
d.add_word("add 3")
d.add_word("add 4")

print(c.words)