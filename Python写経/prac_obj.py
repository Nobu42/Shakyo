# -*- coding: utf-8 -*-
# OOP中級：property, 抽象クラス, 継承, ポリモーフィズム

from abc import ABC, abstractmethod

print("========== 1. @property によるゲッター・セッター ==========")

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # 慣習的に「_」で内部属性を示す

    @property
    def price(self):
        """ゲッター：price を取得"""
        return self._price

    @price.setter
    def price(self, value):
        """セッター：price を設定"""
        if value < 0:
            raise ValueError("価格は0以上でなければなりません")
        self._price = value

    @property
    def tax_included_price(self):
        return int(self._price * 1.1)

item = Product("ノートPC", 100000)
print(f"{item.name} の税込価格: {item.tax_included_price} 円")
item.price = 120000
print(f"値上げ後の価格: {item.price} 円")

# item.price = -1000  # ← ValueError: 価格は0以上でなければなりません

print("\n========== 2. 抽象クラスとインターフェース（abc） ==========")

class Shape(ABC):
    """抽象基底クラス（インターフェース）"""

    @abstractmethod
    def area(self):
        """面積を返す抽象メソッド"""
        pass

    @abstractmethod
    def name(self):
        """名前を返す抽象メソッド"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def name(self):
        return "円"

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def name(self):
        return "正方形"

shapes = [Circle(5), Square(4)]
for s in shapes:
    print(f"{s.name()} の面積: {s.area()}")

print("\n========== 3. 継承とポリモーフィズム ==========")

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} は働いています"

class Engineer(Employee):
    def work(self):
        return f"{self.name} はコードを書いています"

class Manager(Employee):
    def work(self):
        return f"{self.name} は会議しています"

employees = [Engineer("のぶ"), Manager("デューク")]
for emp in employees:
    # ポリモーフィズム：work() が動的に振る舞いを切り替える
    print(emp.work())
