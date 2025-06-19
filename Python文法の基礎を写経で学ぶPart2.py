# -*- coding: utf-8 -*-
"""
Python文法の基礎を写経で学ぶPart2.py

- クラス定義と使用
- ファイル読み書き
- 標準ライブラリ(datetime, os, random)
- モジュール化とインポート
"""

# 1. クラス定義とインスタンス
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"『{self.title}』の著者は {self.author} です。")

# クラスのインスタンス生成とメソッド呼び出し
book = Book("入門Python3", "ビル・ルバノビック")
book.describe()

# 2. ファイルへの書き込み
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("これはPythonで作成したファイルです。\n")
    f.write("ファイル操作は大事です。\n")

# 3. ファイルからの読み込み
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("ファイルの中身:")
    print(content)

# 4. datetimeモジュール
import datetime

now = datetime.datetime.now()
print("現在日時:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 5. osモジュールでファイル確認
import os

if os.path.exists("sample.txt"):
    print("sample.txt は存在します。")
else:
    print("sample.txt は存在しません。")

# 6. randomモジュール
import random

num = random.randint(1, 100)
print(f"1〜100のランダムな数字: {num}")

# 7. モジュールの定義と利用（本来は別ファイルに分ける）
# ↓ モジュール的に扱うための関数定義
def greet(name):
    return f"{name}さん、ようこそ！"

# ↓ 通常のモジュールからの呼び出しっぽく関数を使う
print(greet("のぶ"))

# 8. 文字列の処理メソッド
text = "  Pythonは楽しい！  "
print("元の文字列:", text)
print("strip:", text.strip())
print("大文字:", text.upper())
print("分割:", text.split("は"))

# 9. 例外処理（ファイル削除を試みる）
try:
    os.remove("sample.txt")
    print("sample.txt を削除しました。")
except FileNotFoundError:
    print("ファイルが見つかりませんでした。")

# 10. __name__ の確認
if __name__ == "__main__":
    print("__name__ は main です（このスクリプトが直接実行された）")
