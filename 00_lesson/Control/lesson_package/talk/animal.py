from lesson_package import utils

def sing():
    return "dfhasofiu"

def cry():
    return utils.say_twice("fhsauiofdsajwe")

#importされたときに実行されないようにする
if __name__ == "__main__":
    print(sing())
    print("animal", __name__)