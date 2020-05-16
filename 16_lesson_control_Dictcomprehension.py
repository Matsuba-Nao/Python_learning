w = ["mon", "tue", "wed"]
f = ["coffee", "milk", "water"]

d = {}
# for x, y in zip(w, f):
#     d[x] = y

d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
#set型の内包表記
s = set()

# for i in range(10):
#     s.add(i)

s = {i for i in range(10) if i % 2 == 0}
print(s)

#ジェネレータ内包表記
def g():
    for i in range(10):
        yield i

g = g()
#g = (i for i in range(10) if i % 2 == 0)
g = tuple(i for i in range(10) if i % 2 == 0)
for x in g:
    print(x)
# g = g()
print(type(g))
#print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
