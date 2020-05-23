class Word(object):
    def __init__(self, text):
        self.text = text

    # オブジェクトが呼ばれたときの型に応じてメソッドを返す
    # これが一番使われるかも
    def __str__(self):
        return "Word!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word("text")
w2 = Word("###################")

print(w)
print(len(w))
print(len(w2))
print(w + w2)
# 特殊メソッドにより文字列の比較が可能に
print(w == w2)
