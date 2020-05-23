"""
test test ########
"""
animal = "cat"

def f():
    #global animal
    #print(animal)
    #宣言する前に使用すると、グローバルではなく関数内で宣言する前に使うことになりエラー
    animal = "dog"
    #locals()を使うとdoc型で返してくれる
    print("local", locals())

f()
print("global:", globals())