# a = list(map(int, input().split()))
# m = 0
# for i in range(len(a)-1):
#     if (a[i] + a[i+1]) % 2 == 0:
#         m = max(m, a[i] + a[i+1])
# print(m)


# import sys

# def pairwise_sum_fill(a, b, fill=0):
#     L = max(len(a), len(b))
#     for i in range(L):
#         c = a[i] if i < len(a) else fill
#         d = b[i] if i < len(b) else fill
#         yield c + d
# exec(sys.stdin.read())

# import sys

# def warn_after(iters=2, message='Too many calls'):
#     if not isinstance(iters, int) or iters < 0:
#         iters = 1
#     def decorator(func):
#         c = 0
#         def wrapper(*args, **kwargs):
#             nonlocal c
#             c += 1
#             res = func(*args, **kwargs)
#             if c > iters:
#                 print(message)
#             return res
#         return wrapper
#     return decorator                 
# exec(sys.stdin.read())

# import sys

# def apply_scholarships(students, rules):
#     gpa = [r for r in rules if r["type"] == "gpa"]
#     amount = [r for r in rules if r["type"] == "amount"]
#     for s in students:
#         for r in gpa:
#             if s["gpa"] >= r["min_gpa"]:
#                 s["stipend"] *= (1 + r["percent"]/100)
#         for r in amount:
#             if s["name"] == r["name"]:
#                 s["stipend"] += r["amount"]
#     total = sum(st["stipend"] for st in students)
#     return students, total
# exec(sys.stdin.read())


import sys, json

class Student:
    def __init__(self, name, stipend):
        self.name = name
        self.stipend = int(stipend)
    def richer_than(self, other):
        return self.stipend > other.stipend
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        name = data.get("name")  
        stipend = data.get("stipend") 
        return cls(name, stipend)
class StudentList:
    def __init__(self, student_list):
        self.student_list = student_list
        self.index = 0
    def append(self, student):
        self.student_list.append(student)
    def __iter__(self):
        self.index = 0
        return self
    def __str__(self):
        return "[" + ",".join(str(s) for s in self.student_list) + "]"
    def __next__(self):
        student = self.student_list[self.index]
        self.index += 1
        return student
exec(sys.stdin.read())

# from math import gcd
# import sys
# class Fraction:
#     def __init__(self, num, den):
#         g = gcd(num, den)
#         self.num = num // g
#         self.den = den // g
#     def __str__(self):
#         return f"({self.num} / {self.den})"
#     def __add__(self, other):
#         num = self.num * other.den + other.num * self.den
#         den = self.den * other.den
#         return Fraction(num, den)
#     def __sub__(self, other):
#         num = self.num * other.den - other.num * self.den
#         den = self.den * other.den
#         return Fraction(num, den)
#     def __mul__(self, other):
#         num = self.num * other.num
#         den = self.den * other.den
#         return Fraction(num, den)
#     def __truediv__(self, other):
#         num = self.num * other.den
#         den = self.den * other.num
#         return Fraction(num, den)
#     def __eq__(self, other):
#         return self.num * other.den == self.den * other.num
#     def __ne__(self, other):
#         return not self == other
# exec(sys.stdin.read())