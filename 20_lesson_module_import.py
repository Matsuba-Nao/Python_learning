#これはフルパス
#import lesson_package.utils

#モジュールからインポート
# from lesson_package.talk import animal
# from lesson_package.talk import human

#*にすると__init__の__all__に書いてあるリストを読み込む
#あまり多いと勧められない
#from lesson_package.talk import *

#名前を変えて読み込めるがあまり多用はしない方がよい
#from lesson_package import utils as u

#どこから来たのかわかりづらくなるのであまり推奨されない
#from lesson_package.utils import say_twice

#r = lesson_package.utils.say_twice("hello")
#r = utils.say_twice("hello")

#非推奨
#r = say_twice("hello")

#print(r)

# print(animal.sing())
# print(animal.cry())

# print(human.sing())
# print(human.cry())

try:
    from lesson_package import utils
except ImportError:
    #新しいパッケージの場合はこちら、というような使い方
    from lesson_package import utils

r = utils.say_twice("word")
print(r)