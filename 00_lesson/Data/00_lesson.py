num: int = 1
name = "Mike"
is_ok = True

#num = name
#print(num, type(num))
# print(name, type(name))
# print(is_ok, type(is_ok))
print("Hi", "Mike", sep=",")
print("Hi", "Mike", sep=",", end=".\n")

print("#######################")
print("""\
line1
line2
line3\
        """)
print("#######################")
# 長い文字列リテラルを引っ付けるときに開業すると便利
s = ("aa"
     "bbbbbbbbbb")

t = ("cccc")

print(s)

s = "My name is Mike. Hi Mike."
is_start = s.startswith("My")
print(is_start)
print(s.find("Mike"))
print(s.rfind("Mike"))
print(s.count("Mike"))
print(s.capitalize())
print(s.title)
print(s.upper())
print(s.replace("Mike", "Nancy"))

# {}にformatでindexが代入されて表示される
# 数値で順番を指定できる
print("a is {0} {1} {2}".format(1, 2, 3))
print("a is {2} {1} {2}".format(1, 2, 3))
print("Myname is {0} {1}. Watashi ha {1} {0}".format("Jun", "Sakai"))
# 変数の名前として渡すこともできる
print("Myname is {name} {family}. Watashi ha {family} {name}".format(
    name="Jun", family="Sakai"))

# Python3.6からf-stringsが使えるようになった。こちらの方が処理が速い
x, y, z = 1, 2, 3
print(f"a is {x} {y} {z}")
