#importした時点で読込先が実行される
from lesson_package.talk import animal
import config

def main():
    print(animal.sing())
    print("lesson:",__name__)

#mainとしてプログラムを作っていても、インポートされたときのことを考えてこうするのがよい
if __name__ == "__main__":
    main()