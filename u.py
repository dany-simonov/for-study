# k = int(input())
# p = int(input())
# s = int(input())
# print(int(s // (k * (1 + p / 100))))

# A = int(input())
# B = int(input())
# if A < B:
#     print(*[i for i in range(A, B+1)])
# else:
#     print(*[i for i in range(A, B-1, -1)])


# n = int(input())
# a = list(map(int, input().split()))
# print(*sorted(a))

#4
# n = int(input())
# a = list(map(int, input().split()))
# c = 0
# for i in range(1, len(a)-1):
#     if a[i-1] < a[i] > a[i+1] :
#         c +=1
# print(c)

# n = int(input())
# a = set()
# for i in range(n):
#     s = input()
#     a.add(s)
# print(len(a))

# n, m = list(map(int, input().split()))
# s = {}
# for i in range(n):
#     a = list(input().split())
#     name = a[0]
#     t = a[1]
#     s[name] = a[1]
# for j in range(m):
#     a = list(input().split())
#     d = a[0]
# print(s.get())



# import sys

# def dict_from_lists(keys, values):
#     return dict(zip(keys, values))
# exec(sys.stdin.read())

# import sys

# def group_revenue(sales: list, key_fn):

# exec(sys.stdin.read())

# import sys

# def count_to(n: int):
#     for i in range(n+1):
#         yield i

# exec(sys.stdin.read())

# o = int(input())
# for i in range(o):
#     print(i)

# import sys

# def squares(iterable):
#     for i in iterable:
#         yield i ** 2
# exec(sys.stdin.read())

# import sys

# def sum_iterator(it):
#     s = 0
#     while True:
#         try:
#             element = next(it)
#             s += element
#         except StopIteration:
#             break
#     return s
# exec(sys.stdin.read())


# def weekday_cycle(n: int, start: int = 0):
#     s = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     sp = s * (10 ** 3)
#     return sp[start:n]

# import sys

# def weekday_cycle(n: int, start: int = 0):
#     weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     start_index = start % 7
#     for i in range(n):
#         yield weekdays[(start_index + i) % 7]

# exec(sys.stdin.read())

# import sys
# def derive(i):
#     def prost(s):
#         for j in range(int(s**0.5)+1):
#             if s % j == 0:
#                 return False
#             else:
#                 return True
#     for k in range(i):
#         if prost(k):
#             yield k
# exec(sys.stdin.read())

# import sys

# def derive(n):
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             yield d
#             while n % d == 0:
#                 n //= d
#         d += 1
#     if n > 1:
#         yield n

# exec(sys.stdin.read())

# for i in range((r + 9) // 10 + 1):
#     x = r - i * 10
#     if x < 0:
#         x = 0
#     cost = i * 125 + x * 15
#     if cost < best:
#         best = cost
#         p10 = i
#         p1 = x

# print(p1, p10, p60)

# import sys

# def with_tax(revenues, tax_fn):
#     for i in revenues:
#         yield i - tax_fn(i)
# exec(sys.stdin.read())

# import sys
# 
# def simple_groupby(items, key_fn):
#     if len(items) != 0:
#         current_key = key_fn(items[0])
#         group_list = [items[0]]
#         for i in items[1:]:
#             if key_fn(i) == current_key:
#                 group_list.append(i)
#             else:
#                 yield (current_key, group_list)
#                 current_key = key_fn(i)
#                 group_list = [i]         
#         yield (current_key, group_list) 
# exec(sys.stdin.read())

# import sys

# def simple_groupby(items, key_fn):
#     it = iter(items)
#     try:
#         first_item = next(it)
#     except StopIteration:
#         return

#     current_key = key_fn(first_item)
#     group_list = [first_item]

#     for item in it:
#         key = key_fn(item)
#         if key == current_key:
#             group_list.append(item)
#         else:
#             yield (current_key, group_list)
#             current_key = key
#             group_list = [item]
    
#     yield (current_key, group_list)

# exec(sys.stdin.read())


# import sys

# def gmap(iterable, func):
#     for i in iterable:
#         yield func(i)

# def gfilter(iterable, predicate):
#     for i in iterable:
#         if predicate(i):
#             yield i

# def gbatch(iterable, size):
#     b = []
#     for i in iterable:
#         b.append(i)
#         if len(b) == size:
#             yield b
#             b = []
#     if b:
#         yield b

# def pipeline(source, map_fn, pred_fn, batch_size):
#     return gbatch(gfilter(gmap(source, map_fn), pred_fn), batch_size)

# class DictIter:
#     def __init__(self, d):
#         self.items = list(d.items())
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.items):
#             key, value = self.items[self.index]
#             self.index += 1
#             return [key, value]
#         else:
#             raise StopIteration


# import sys
# class MovingAverage:
#     def __init__(self, data, size=3):
#         self.data = data
#         self.size = size
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index + self.size > len(self.data):
#             raise StopIteration
#         window = self.data[self.index : self.index + self.size]
#         avg = sum(window) / self.size
#         self.index += 1
#         return avg
# exec(sys.stdin.read())


# n = int(input())
# p60 = n // 60
# r = n - p60 * 60
# p1, p10 = r, 0
# best = p1 * 15

# import json

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = int(age)

#     @classmethod
#     def sort_names(cls, json_str):
#         people = json.loads(json_str)
#         people.sort(key=lambda d: (d['age'], d['name']))
#         return ' '.join(d['name'] for d in people)
    
# json_str = "[{\"name\": \"Ann\", \"age\": 18}, {\"name\": \"Bob\", \"age\": 15}, {\"name\": \"Cara\", \"age\": 20}, {\"name\": \"Dan\", \"age\": 18}]"
# print(Person.sort_names(json_str) == "Bob Ann Dan Cara")
# print("Bob Ann Dan Cara")

import sys

def printer(*args, sep=' ', end='\n', **kwargs):
    printed = False
    if args:
        print(sep.join(map(str, args)), end='')
        print(end, end='')
        printed = True
    if kwargs:
        if not printed:
            print(end, end='')
        items = [f"({k!r}, {v!r})" for k, v in kwargs.items()]
        print(sep.join(items), end='')
        print(end, end='')
        printed = True
    if not printed:
        return
exec(sys.stdin.read())