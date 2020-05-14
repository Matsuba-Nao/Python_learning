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
print(s.title())
print(s.upper())
print(s.replace("Mike", "Nancy"))

print("a is {0} {1} {2}".format(1, 2, 3))
print("a is {2} {1} {2}".format(1, 2, 3))
print("Myname is {0} {1}. Watashi ha {1} {0}".format("Jun", "Sakai"))
print("Myname is {name} {family}. Watashi ha {family} {name}".format(
    name="Jun", family="Sakai"))

x, y, z = 1, 2, 3
print(f"a is {x} {y} {z}")
