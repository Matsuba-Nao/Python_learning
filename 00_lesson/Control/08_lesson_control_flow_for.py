some_list = [1, 2, 3, 4, 5]

# 反復処理をするイテレータ
# for i in some_list:
#     print(i)

# for s in "abcde":
#     print(s)

# for word in ["My", "name", "is", "Mike"]:
#     if word == "name":
#         continue
#     print(word)

# for fruits in ["apple", "banana", "orange"]:
#     # if fruits == "banana":
#     #     print("Stop eating")
#     #     break
#     print(fruits)
# else:
#     print("I ate all!")

# range関数
# num_list = [0,1,2,3,4,5,6]
# for i in num_list:
#     print(i)

for i in range(10):
    print(i, "Hello")

# _を使うとただ10回ループしただけと明示できる
for _ in range(10):
    print("Hello")

# enumerate関数
# インデックスの番号を出したいとか
for i, fruit in enumerate(["apple", "banana", "orange"]):
    print(i, fruit)

# zip関数
days = ["Mon", "Tue", "Wed"]
fruits = ["apple", "banana", "orange"]
drinks = ["coffee", "tea", "beer"]

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

for day,fruit,drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

#辞書をforで処理する
d = {"x": 100, "y":200}
#よく使われる辞書の関数。taple型で辞書を返す
print(d.items())

for k, v in d.items():
    print(k,":", v)