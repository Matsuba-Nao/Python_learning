# タプル型=静的なリスト型のようなもの
t = (1, 2, 3, 4, 5, 6)
print(t[1])

t2 = 1, 2, 3, 4, 5
print(type(t2))
# カンマをつけるとタプル型になる

#t2[0] += 1
# print(t2[0])

new_tuple = (1,) + (4, 5, 6)
print(new_tuple)

# タプルのアンパッキング
num_tuple = 10, 20
x, y = num_tuple
print(x, y)

# 入れ替えにアンパッキングを使う
i = 10
j = 20

i, j = j, i
print(i, j)
print(type(i))

# 使いどころ
chose_from_two = ("A", "B", "C")
#chose_from_two = ["A", "B", "C"]

# chose_from_two.append("A")
# chose_from_two.append("B")

answer = []
answer.append("A")
answer.append("B")

print(chose_from_two)
print(answer)
