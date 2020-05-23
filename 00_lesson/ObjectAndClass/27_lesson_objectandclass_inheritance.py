#ダックタイピング
# class Person(object):
#     def __init__(self, age=1):
#         self.age = age

#     def drive(self):
#         if self.age >= 18:
#             print("ok")
#         else:
#             raise Exception("No drive")

#抽象(abstract)クラスとしての実装
#特に使う必要がなければ使わなくてもよい
import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age
        
    #継承先で実装しないとエラーの出る関数
    @abc.abstractclassmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception("No drive")

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print("ok")

baby = Baby()
adult =  Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print("run")
    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)

#Carの継承
class ToyotaCar(Car):
    def run(self):
        print("fast")

class TeslaCar(Car):
    def __init__(self, model="Model S",
                enable_auto_run=False,
                password = "123"):
        #親クラスのコンストラクタを呼び出す
        super().__init__(model=model)
        #__だとクラス内のprivateになる
        #_一個の時はアクセスしてほしくないと明示するだけ
        self.__enable_auto_run = enable_auto_run
        self.password = password

    #enable_auto_runを呼び出した時はこれが呼ばれる
    @property
    def enable_auto_run(self):
        return self.enable_auto_run

    #setterをつけると外部での変更の際にこれが呼ばれる
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == "456":
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print(self.__enable_auto_run)
        print("super fast")
    def auto_run(self):
        print("auto run")

# toyota_car = ToyotaCar("Lexus")
# print(toyota_car.model)
# toyota_car.run()

# print("#####################")

tesla_car = TeslaCar("Model S", password="456")
tesla_car.enable_auto_run = True
tesla_car.run()
#tesla_car.auto_run()

#構造体として使うこともできるが、クラス定義外で定義するとバグにつながりやすい
class T(object):
    pass

t = T()
t.name = "Mike"
t.age = 28