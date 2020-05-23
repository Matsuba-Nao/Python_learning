d = {"x": 10, "y": 20, "z": 30}
print(d)
print(d["x"])

c = dict([("a", 1), ("b", 2), ("c", 3)])
print(c)

# メソッド
print(d.keys())
# d.keys()
print(d.values())

d2 = {"x": 1000, "y": 100}
d.update(d2)
print(d)
#print(d["t"])
#print(d.get("t"))
print(d.pop("x"))
#print(type(d.get("t")))
print(d)
print("d" in d)

#コピー関連
x = {"a":1}
#y = x
y = x.copy()
y["a"] = 100
print(x)
print(y)

l = [
    ["apple", 100]
    ["banana", 200]
    ["prange", 300]
]

fruits = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
}

#リスト型と違って位置を知っている必要がない
#dictionary型はハッシュを持っており検索がリストに比べて早い
print(fruits["apple"])
