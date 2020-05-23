#import builtins

ranking = {
    "A": 100,
    "B": 85,
    "C": 95
}

#ranking.get("A")
#イテレータブルな変数を並び変える標準関数
print(sorted(ranking, key=ranking.get, reverse=True))