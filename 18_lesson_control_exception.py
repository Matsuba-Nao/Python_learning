# l = [1, 2, 3]
# i = 5

# try:
#     l[0]
# except IndexError as ex:
#     print("Don't worry {}".format(ex))
# except NameError as ex:
#     print(ex)
# #全てのExceptionをキャッチするのは実際は推奨されていない
# except Exception as ex:
#     print("Other: {}".format(ex))
# #exceptionなかったときに実行
# else:
#     print("done")
# #何が起きても実行してくださいという処理
# finally:
#     print("clean up")

# #print("last")


class UppercaseError(Exception):
    pass


def check():
    words = ["APPLE", "orange", "banana"]
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


# try,raise,exceptの3つを使いこなす
try:
    check()
# 独自エラーで発生させればどういう内容が発生したかが他の人も理解できる
except UppercaseError as exc:
    print("This is my fault. Go next")

#raise IndexError("test error")
