s = "jadfjsalifgyhaoliujg;aiokjvxc"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    #print(d.keys())
    #print(d.values())
    #同じkeyのvalueに対してインクリメント
    d[c] += 1
print(d)

# d = {}
# for c in s:
#     d.setdefault(c, 0)
#     d[c] += 1
# print(d)

from collections import defaultdict

d = defaultdict(int)

print(d)
for c in s:
    d[c] += 1
print(d)

print(d["f"])