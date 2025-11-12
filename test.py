# c = 1
# mi = 10 ** 10
# for i in range(len(a)):
#     if i > 0 and i < mi and c % 2 == 1:
#         mi = i
#     c += 1
# print(mi)


# a = list(map(int, input().split()))
# print(min(f for f in a if f % 2 == 1))

# n = int(input())
# a = {}
# for i in range(n):
#     name, price, count = input().split()
#     cost = int(price) * int(count)
#     c = a.get(name)
#     if c is None or cost < c:
#         a[name] = cost
# print(a)

# import sys

# def all_of(items, predicate):
#     for i in items:
#         if not predicate(i):
#             return False
#     return True
        
# exec(sys.stdin.read())

# import sys

# def alternate(items1, items2):
#     for i, (a, b) in enumerate(zip(items1, items2), start=1):
#         yield (i, a, b)
# exec(sys.stdin.read())


# import sys
# class Book:
#     def __init__(self, title, year):
#         self.title = title
#         self.year = year
#     def newer(self, other):
#         return self.year > other.year
# exec(sys.stdin.read())

# import json
# import sys
# class Book:
#     def __init__(self, title, year):
#         self.title = title
#         self.year = year
#     def newer(self, other):
#         return self.year > other.year
#     @classmethod
#     def from_json(cls, json_str):
#         data = json.loads(json_str)
#         return cls(data["title"], data["year"])
# exec(sys.stdin.read())

# import json
# import sys
# class Book:
#     def __init__(self, title, year):
#         self.title = title
#         self.year = int(year)
#     def __str__(self):
#         return f"({self.title}, {self.year})"
#     @classmethod
#     def from_json(cls, json_str):
#         data = json.loads(json_str)
#         return cls(data["title"], data["year"])
    
# class Library:
#     def __init__(self, book_list):
#         self.book_list = book_list
#     def __iter__(self):
#         return iter(self.book_list)
# exec(sys.stdin.read())

# import sys 
# import sqlite3
# class ProductRepo:
#     @classmethod
#     def count_in_stock(cls, db_path: str, min_units: int):
#         with sqlite3.connect(db_path) as conn:
#             cur = conn.cursor()
#             cur.execute(
#                 "SELECT COUNT(*) FROM Products WHERE UnitsInStock >= ?",
#                 (min_units,)
#             )
#             row = cur.fetchone()
#             return int(row[0] if row is not None else 0)
# exec(sys.stdin.read())

