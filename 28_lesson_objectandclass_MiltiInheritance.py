class Person(object):
    def talk(self):
        print("talk")
    def run(self):
        print("person run")

class Car(object):
    def run(self):
        print("run")

#多重継承
#左側にあるもので先に見つけた関数が優先される
#なるべくなければないほうがよい
class PersonCarRobot(Person, Car):
    def fly(self):
        print("fly")

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()