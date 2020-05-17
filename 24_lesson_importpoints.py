#一番上は標準ライブラリ
#カンマで区切ってインポートできるが勧められない
#順番はアルファベット順
#import collections, sys, os
import collections
import sys
import os

#サードパーティ製は一行開ける
import termcolor

#パッケージがどこから読み込んでいるかを表示できる
#print(collections.__file__)
#print(termcolor.__file__)

#pythonが読み込むフォルダ一覧
print(sys.path)