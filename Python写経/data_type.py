# -*- coding: utf-8 -*-
# Pythonの基本データ型とその応用的な使い方を学ぶサンプル
import copy  # deepcopyで使用

print("========== List（リスト） ==========")
# リストは順序付き・変更可能なデータ構造
numbers = [1, 2, 3, 4, 5]

# インデックスアクセス・スライス
print("2番目の値:", numbers[1])
print("最後の2つ:", numbers[-2:])

# 要素追加・削除
numbers.append(6)
numbers.insert(2, 99)
numbers.remove(3)
popped = numbers.pop()
print("popされた値:", popped)

# ソート（非破壊的な sorted も可）
numbers.sort()
print("ソート済:", numbers)

# 内包表記
squared = [x ** 2 for x in numbers if x % 2 == 0]
print("偶数の2乗:", squared)

# zipとの併用
names = ["Alice", "Bob", "Carol"]
ages = [25, 30, 27]
for name, age in zip(names, ages):
    print(f"{name} は {age} 歳")

print("\n========== Tuple（タプル） ==========")
# タプルはイミュータブルな順序付きデータ構造
point = (10, 20)
x, y = point  # アンパック
print(f"x={x}, y={y}")

# ネストされたタプル
nested = ((1, 2), (3, 4))
print("ネスト:", nested[1][0])

# 単一要素タプル
t = (42,)
print("型:", type(t))

print("\n========== Set（集合） ==========")
# Setは順序なし・重複なし
langs = {"Python", "Go", "Rust"}
langs.add("Python")  # 重複要素は無視される
langs.discard("JavaScript")  # 存在しない要素を削除してもOK

# 集合演算
a = {1, 2, 3}
b = {3, 4, 5}
print("和集合:", a | b)
print("積集合:", a & b)
print("差集合:", a - b)
print("対象差:", a ^ b)

# 内包表記
squares_set = {x**2 for x in range(5)}
print("平方の集合:", squares_set)

print("\n========== Dict（辞書） ==========")
# 辞書はキーと値のペア
user = {"name": "Nobu", "age": 40, "skills": ["C", "Python"]}

# アクセス
print("名前:", user["name"])
user["age"] += 1
user["location"] = "Tokyo"

# 安全な取得
email = user.get("email", "未登録")
print("Email:", email)

# キーと値の列挙
for k, v in user.items():
    print(f"{k} => {v}")

# 辞書内包表記
square_dict = {x: x**2 for x in range(5)}
print("平方の辞書:", square_dict)

# ネスト辞書＋ループ
people = {
    "Alice": {"age": 25, "skills": {"Python", "Go"}},
    "Bob": {"age": 30, "skills": {"Rust", "C"}}
}
for name, info in people.items():
    print(f"{name}は{info['age']}歳で、スキル: {', '.join(info['skills'])}")

print("\n========== deepcopy の使い方 ==========")
original = {"numbers": [1, 2, 3]}
shallow = original.copy()
deep = copy.deepcopy(original)

# 値を書き換えてみる
original["numbers"][0] = 999
print("浅いコピー:", shallow["numbers"])  # 影響を受ける
print("深いコピー:", deep["numbers"])     # 影響を受けない

print("\n========== zip, enumerate, sorted など ==========")
names = ["Nobu", "Jun", "Ken"]
scores = [88, 92, 75]
for i, (n, s) in enumerate(zip(names, scores), 1):
    print(f"{i}. {n}: {s}点")

# sorted で辞書を値でソート
score_dict = dict(zip(names, scores))
sorted_by_score = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
print("点数順:", sorted_by_score)

print("\n========== 文字列（str）とメソッド ==========")
s = "  Hello, World!  "
print("元の文字列:", repr(s))
print("strip:", s.strip())
print("小文字:", s.lower())
print("大文字:", s.upper())
print("置換:", s.replace("Hello", "Hi"))
print("区切り:", s.split(","))
print("接続:", "-".join(["Go", "Python", "Rust"]))

# f文字列とformat
name = "Duke"
age = 42
print(f"{name}は{age}歳です")
print("{}は{}歳です".format(name, age))

print("\n========== その他の便利機能 ==========")
# all, any, sum, max, min
nums = [1, 2, 3, 0]
print("全て真？", all(nums))
print("どれか真？", any(nums))
print("合計:", sum(nums))
print("最大:", max(nums))

# enumerate とインデックス付きループ
for i, value in enumerate(["A", "B", "C"]):
    print(f"index={i}, value={value}")
