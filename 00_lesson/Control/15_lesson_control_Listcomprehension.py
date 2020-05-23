t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)


r = []
# for i in t:
#     r.append(i)

# リスト内包表記
# 処理が速いらしい
r = [i for i in t]
print(r)

r = []
# for i in t:
#     for j in t2:
#         r.append(i * j)

#長くなっても使えるが読みづらい
r = [i*j for i in t for j in t2]
print(r)

