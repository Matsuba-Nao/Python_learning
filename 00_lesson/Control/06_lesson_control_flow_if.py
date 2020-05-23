# if文
x = 0
if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")

a = 5
b = 10
if a > 0:
    print("positive")
    if b > 0:
        print("b is positive")
if a > 0 and b > 0 or b < 100:
    print("ok")

"""
y = [1, 2, 3]
x = 1
if x in y:
    print("in")
if x not in y:
    print("not in")

a = 1
b = 2
# あまり勧められないケース
if not a == b:
    print("Not equal")
# こっちを使う
if a != b:
    pri("Not equal")

#notの使い方
is_ok = True
if not is_ok:
    print("hello")
"""

#値が入っていない判定を行うテクニック
# False, 0, 0.0, "", [], (), {}, set()
is_ok = 10

if is_ok:
    print("OK")
else:
    print("No")

#None(Null)の判定
is_empty = None
print(is_empty)
if is_empty is None:
    print("None!!!")
#この場合はTrueとなる
print(1 == True)
#isは同じものでないとtrueにならない
print(1 is True)
