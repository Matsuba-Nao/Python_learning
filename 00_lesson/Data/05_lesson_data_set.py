#集合型、共通のものや関係性を調べたいデータを入れる
a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
b = {2, 3, 3, 6, 7}

print(a - b)
#print(a + b)
print(a & b)
print(a | b)
print(a ^ b)

s = {1,2,3,4,5}
print(s)
s.add(6)
print(s)
s.clear()
print(s)

my_friends = {"A", "C", "D"}
A_friends = {"B", "D", "E", "F"}

print(my_friends & A_friends)

#リストをセットに型変換することもできる
#この時は重複しているものが消える
f = ["apple", "banana", "apple", "banana"]
kind = set(f)
print(f)
print(kind)

"""
aaaa
bbbb
nnnn
test
"""