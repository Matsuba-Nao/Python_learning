count = 0
while count < 5:
    print(count)
    count += 1
else: # breakで抜けた場合は実行されない
    print("done")

# while True:
#     if count >= 5:
#         break
#     if count == 2:
#         count += 1
#         continue
#     print(count)
#    count +=1

while True:
    word = input("Enter")
    #入力が数値かどうか判断する
    if not word.isnumeric():
        print("数字を入力してください")
        continue

    num = int(word)
    if num == 100:
        break
    print("next")
    

