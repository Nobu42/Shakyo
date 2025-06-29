# -*- coding: utf-8 -*-
# Python の関数を多様な形で定義・活用する例

print("========== 基本的な関数 ==========")

def greet():
    """引数も戻り値もない関数"""
    print("こんにちは、のぶさん！")

greet()

def add(x, y):
    """2つの数値を加算して返す"""
    return x + y

result = add(10, 20)
print("10 + 20 =", result)

print("\n========== デフォルト引数 ==========")

def introduce(name, lang="Python"):
    print(f"私は {name} です。好きな言語は {lang} です。")

introduce("のぶ")
introduce("デューク", "Go")

print("\n========== 可変長引数（*args, **kwargs） ==========")

def sum_all(*args):
    """可変長の位置引数を合計する"""
    return sum(args)

print("合計:", sum_all(1, 2, 3, 4))

def print_info(**kwargs):
    """キーワード引数を全て表示する"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="のぶ", age=44, lang="Python")

print("\n========== 関数のネストとクロージャ ==========")

def outer(message):
    def inner():
        print(f"メッセージは: {message}")
    return inner

func = outer("これは閉包です")
func()  # inner() が outer の message を覚えている

print("\n========== ラムダ関数と map/filter/sorted ==========")

# ラムダはその場で使える匿名関数
square = lambda x: x ** 2
print("3の2乗:", square(3))

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, nums))
print("2乗:", squared)

evens = list(filter(lambda x: x % 2 == 0, nums))
print("偶数:", evens)

# sorted の key にもよく使う
names = ["alice", "Bob", "carol"]
sorted_names = sorted(names, key=lambda x: x.lower())
print("名前（大文字小文字無視）:", sorted_names)

print("\n========== 高階関数（関数を渡す／返す） ==========")

def operate(x, y, func):
    """2つの値に関数funcを適用"""
    return func(x, y)

def multiply(a, b):
    return a * b

print("3 * 4 =", operate(3, 4, multiply))

def power_factory(n):
    """n乗を返す関数を生成"""
    def power(x):
        return x ** n
    return power

square = power_factory(2)
cube = power_factory(3)
print("5の2乗:", square(5))
print("2の3乗:", cube(2))

print("\n========== デコレータ（関数に機能を追加） ==========")

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"実行中: {func.__name__}")
        result = func(*args, **kwargs)
        print("終了")
        return result
    return wrapper

@logger
def say_hello(name):
    print(f"こんにちは、{name} さん！")

say_hello("のぶ")

print("\n========== アノテーションと __doc__ ==========")

def subtract(x: int, y: int) -> int:
    """x から y を引いた値を返す"""
    return x - y

print("subtract(10, 3):", subtract(10, 3))
print("関数の説明:", subtract.__doc__)
print("アノテーション:", subtract.__annotations__)
