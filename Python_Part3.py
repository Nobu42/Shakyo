# -*- coding: utf-8 -*-
"""
Python文法の基礎を写経で学ぶPart3

- CSVとJSONの読み書き
- 関数の引数と戻り値の応用
- ラムダ式とsorted()
- リスト・辞書内包表記
"""

import csv
import json

# 1. CSVファイルへの書き込み
csv_file = "sample.csv"
rows = [
    ["名前", "年齢", "職業"],
    ["のぶ", 45, "エンジニア"],
    ["さとし", 38, "デザイナー"]
]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("CSVファイルを書き込みました。")

# 2. CSVファイルの読み取り
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("CSVの中身:")
    for row in reader:
        print(row)

# 3. JSONファイルへの書き出し
user_data = {
    "name": "のぶ",
    "age": 45,
    "skills": ["Python", "Go", "Shell"]
}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f, ensure_ascii=False, indent=2)
print("JSONファイルを書き出しました。")

# 4. JSONファイルの読み込み
with open("user.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print("読み込んだJSON:")
    print(loaded)

# 5. デフォルト引数・キーワード引数
def greet(name, message="こんにちは"):
    print(f"{message}、{name}さん！")

greet("のぶ")
greet("さとし", message="やあ")

# 6. 可変長引数（*argsと**kwargs）
def show_info(*args, **kwargs):
    print("位置引数:", args)
    print("キーワード引数:", kwargs)

show_info("Python", "Go", level="中級", interest="自動化")

# 7. ラムダ式とsorted関数
languages = [
    {"name": "Python", "rank": 1},
    {"name": "C", "rank": 2},
    {"name": "Go", "rank": 4}
]

# ランクでソート
sorted_langs = sorted(languages, key=lambda x: x["rank"])
print("ランク順の言語:")
for lang in sorted_langs:
    print(f"{lang['name']} (Rank {lang['rank']})")

# 8. リスト内包表記
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print("平方:", squares)

# 9. 辞書内包表記
square_map = {n: n ** 2 for n in range(1, 6)}
print("辞書形式の平方:", square_map)

# 10. 条件付き内包表記
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("偶数の平方:", even_squares)
