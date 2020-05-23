n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(n))
print(n[::2])
print(n[2:])
print(n[:-1])
print(n[::-1])

l = ["a", "b", "c"]

# リストの結合
x = [n, l]
print(x)
print(x[0][1])

s = ["a", "b", "c", "d", "e", "f", "g"]
s[2:5] = []
print(s)

#リストの操作色々
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.pop()
print(n)
n.pop(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [1, 2, 3]

#a += b
a.extend(b)
print(a)

print(a.index(3))
print(a.index(3, 3))

if 5 in a:
    print("exsist")

a.sort()
print(a)
a.reverse()
print(a)

s = "My name is Mike."
to_split = s.split(" ")
print(to_split)
x = "####".join(to_split)
print(x)

# pythonは参照渡しに自動的になる
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print("j =", j)
print("i =", i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print("y =", y)
print("x =", x)

