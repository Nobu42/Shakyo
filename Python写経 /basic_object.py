# -*- coding: utf-8 -*-
# Python のオブジェクト指向の基本と応用を学ぶサンプル

print("========== 1. 基本のクラス定義とインスタンス ==========")

class Dog:
    # クラス変数（すべてのインスタンスで共有）
    species = "Canis familiaris"

    def __init__(self, name, age):
        # インスタンス変数（各インスタンス固有）
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}（{self.age}歳）がワン！と鳴いた")

    def human_years(self):
        return self.age * 7

    def __str__(self):
        return f"{self.name} は {self.age} 歳の犬です"

dog1 = Dog("ポチ", 3)
dog2 = Dog("タロー", 5)

dog1.bark()
print(dog2)
print(f"{dog1.name} の人間年齢換算: {dog1.human_years()}")

print("\n========== 2. クラスメソッドとスタティックメソッド ==========")

class Counter:
    count = 0  # クラス変数

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def info():
        print("これはインスタンスに依存しない静的メソッドです")

c1 = Counter()
c2 = Counter()
print("生成されたインスタンス数:", Counter.get_count())
Counter.info()

print("\n========== 3. 継承とオーバーライド ==========")

class Animal:
    def speak(self):
        print("何かが鳴いた")

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} がニャーと鳴いた")

cat = Cat("ミケ")
cat.speak()  # オーバーライドされたメソッド

print("\n========== 4. 特殊メソッドの活用 ==========")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print("v1 + v2 =", v3)
print("v3 == Vector(4, 6)?", v3 == Vector(4, 6))

print("\n========== 5. isinstance と issubclass ==========")

print("v1 は Vector のインスタンス？", isinstance(v1, Vector))
print("Cat は Animal のサブクラス？", issubclass(Cat, Animal))
