# -*- coding: utf-8 -*-
"""
Python文法の総まとめ：実行結果で動作確認できる入門サンプル
Author: のぶ（デューク補佐）
"""

# -------------------------
# 1. 変数と基本データ型
# -------------------------
print("■ 1. 基本的な型")

integer = 42
floating = 3.14
text = "Hello, Python!"
boolean = True

print(f"整数: {integer}, 浮動小数点: {floating}, 文字列: {text}, 論理値: {boolean}")

# 型確認
print(type(integer), type(floating), type(text), type(boolean))

# -------------------------
# 2. リスト
# -------------------------
print("\n■ 2. リスト")

fruits = ['apple', 'banana', 'cherry']
print("リストの内容:", fruits)
print("最初の要素:", fruits[0])

fruits.append('orange')
print("追加後:", fruits)

for fruit in fruits:
    print(f"- {fruit}")

# -------------------------
# 3. 辞書（dict）
# -------------------------
print("\n■ 3. 辞書（dict）")

person = {
    'name': 'Alice',
    'age': 30,
    'city': 'Tokyo'
}

print("名前:", person['name'])
print("全情報:", person)

for key, value in person.items():
    print(f"{key}: {value}")

# -------------------------
# 4. セットとタプル
# -------------------------
print("\n■ 4. setとtuple")

colors = {'red', 'green', 'blue'}
fixed = (10, 20, 30)

print("セット:", colors)
print("タプル:", fixed)

# -------------------------
# 5. if文
# -------------------------
print("\n■ 5. 条件分岐")

score = 85
if score >= 90:
    print("評価: A")
elif score >= 80:
    print("評価: B")
else:
    print("評価: C")

# -------------------------
# 6. for/whileループ
# -------------------------
print("\n■ 6. ループ")

print("forで繰り返し:")
for i in range(5):
    print(i, end=' ')
print()

print("whileで繰り返し:")
x = 0
while x < 3:
    print(x)
    x += 1

# -------------------------
# 7. 関数定義と引数
# -------------------------
print("\n■ 7. 関数")

def greet(name="world"):
    return f"Hello, {name}!"

print(greet())
print(greet("のぶ"))

def calc_area(width, height):
    return width * height

print("面積:", calc_area(5, 3))

# -------------------------
# 8. リスト内包表記
# -------------------------
print("\n■ 8. リスト内包表記")

squares = [x ** 2 for x in range(5)]
print("2乗リスト:", squares)

# -------------------------
# 9. 例外処理
# -------------------------
print("\n■ 9. 例外処理")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("エラー発生:", e)

# -------------------------
# 10. ファイル操作
# -------------------------
print("\n■ 10. ファイル操作")

filename = "sample.txt"
with open(filename, 'w') as f:
    f.write("これはサンプルです。\nPythonは楽しい！")

with open(filename, 'r') as f:
    content = f.read()

print("ファイル内容:\n", content)

# -------------------------
# 11. クラスとオブジェクト
# -------------------------
print("\n■ 11. クラスとオブジェクト")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} が鳴きます。"

class Dog(Animal):
    def speak(self):
        return f"{self.name}：ワン！"

dog = Dog("ポチ")
print(dog.speak())

# -------------------------
# 12. モジュールとライブラリ
# -------------------------
print("\n■ 12. モジュールと標準ライブラリ")

import random
import datetime

print("ランダムな数:", random.randint(1, 100))
print("今日の日付:", datetime.date.today())

# -------------------------
# 13. 応用：複数のクラスでやりとり
# -------------------------
print("\n■ 13. クラス応用")

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}：{amount}円入金しました。残高：{self.balance}円")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.name}：残高不足です。")
        else:
            self.balance -= amount
            print(f"{self.name}：{amount}円引き出しました。残高：{self.balance}円")

# 口座を作って試す
acc = Account("のぶ", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)

# -------------------------
# 14. 実践的な組み合わせ：辞書+ループ+条件
# -------------------------
print("\n■ 14. 実践パターン")

users = [
    {"name": "Alice", "age": 24},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 30}
]

print("20歳以上のユーザー：")
for user in users:
    if user['age'] >= 20:
        print(f"- {user['name']}（{user['age']}歳）")

# -------------------------
# 15. 終了
# -------------------------
print("\nすべて完了しました！Pythonの基本をざっくり網羅しました 🚀")
