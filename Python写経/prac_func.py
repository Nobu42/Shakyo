# -*- coding: utf-8 -*-
import functools  # lru_cache で使用

print("========== 1. 関数と例外処理の組み合わせ ==========")

def divide(a, b):
    """0除算の可能性に備えた安全な割り算関数"""
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"エラー: 0では割れません - {e}")
        return None
    else:
        return result
    finally:
        print("割り算終了（成功／失敗問わず実行）")

print("10 ÷ 2 =", divide(10, 2))
print("5 ÷ 0 =", divide(5, 0))  # 例外発生

print("\n========== 2. functools.lru_cache の使用 ==========")

@functools.lru_cache(maxsize=100)
def fib(n):
    """再帰的フィボナッチ（キャッシュ付き）"""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("フィボナッチ数列:")
for i in range(10):
    print(f"fib({i}) = {fib(i)}")

print("キャッシュヒット数:", fib.cache_info())

print("\n========== 3. ジェネレーター（yield） ==========")

def countdown(n):
    """カウントダウンを yield で一つずつ返す"""
    while n > 0:
        yield n
        n -= 1

print("カウントダウン:")
for num in countdown(5):
    print(num)

def even_numbers(limit):
    """偶数を返すジェネレーター"""
    for i in range(limit):
        if i % 2 == 0:
            yield i

print("偶数だけ出力:")
for e in even_numbers(10):
    print(e)

print("\n========== 4. ジェネレーター式（内包表記のような形式） ==========")

squares = (x * x for x in range(5))
print("平方ジェネレーター:")
for s in squares:
    print(s)

print("\n========== 5. イテレータを自作するクラス ==========")

class Countdown:
    """自作イテレータクラス"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val

print("自作イテレータ:")
for num in Countdown(3):
    print(num)
