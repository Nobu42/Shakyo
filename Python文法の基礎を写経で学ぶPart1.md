# -*- coding: utf-8 -*-
"""
Python文法の基礎を写経で学ぶPart1

- 変数と型
- 条件分岐（if文）
- ループ（for / while）
- 関数定義と呼び出し
- リストと辞書の操作
"""

# 1. 変数と基本の型
message = "こんにちは、Python！"
number = 42
pi = 3.14
is_active = True

print(message)
print(f"数字: {number}, 円周率: {pi}, 有効か？: {is_active}")

# 2. 条件分岐
age = 20
if age >= 18:
    print("大人です")
elif age >= 13:
    print("ティーンです")
else:
    print("子供です")

# 3. リストの使い方
fruits = ["りんご", "みかん", "バナナ"]

# 要素の追加・削除
fruits.append("いちご")
fruits.remove("みかん")

print("果物リスト:", fruits)

# 4. forループ
for fruit in fruits:
    print("好きな果物:", fruit)

# 5. whileループ
count = 0
while count < 3:
    print(f"カウント: {count}")
    count += 1

# 6. 関数定義と呼び出し
def greet(name):
    print(f"{name}さん、こんにちは！")

greet("のぶ")

# 7. 戻り値のある関数
def square(x):
    return x * x

result = square(5)
print("5の二乗は", result)

# 8. 辞書の使い方
user = {
    "名前": "のぶ",
    "年齢": 45,
    "職業": "エンジニア"
}

# 値の取得
print("ユーザー名:", user["名前"])

# 値の更新と追加
user["年齢"] = 46
user["出身"] = "大阪"

# 辞書のループ
for key, value in user.items():
    print(f"{key}: {value}")

# 9. 例外処理の基本
try:
    value = int("abc")  # 整数に変換できないので例外発生
except ValueError as e:
    print("例外が発生しました:", e)

# 10. リスト内包表記（ちょっと上級）
squares = [x * x for x in range(1, 6)]
print("1〜5の二乗:", squares)
