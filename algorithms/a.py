# def f(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


# print(f(14, 18))


# n = int(input())
# for i in range(2, int(n ** 0.5)+1):
#     if n % i == 0:
#         print(i)
#         break
#     else:
#         print(n)
#         break

# a = int(input())
# b = int(input())


# def f(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


# print(f(a, b))


# a = int(input())
# b = int(input())


# def f(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


# print(f(a, b))

# import math

# a = int(input())
# b = int(input())
# print(a * b // math.gcd(a, b)

# a = int(input())
# def prost(s):
#     for i in range(2, int(s ** 0.5)+1):
#         if s % i == 0:
#             return False
#     return True
    
    
# for i in range(2, a+1):
#     if a % i == 0 and prost(i):
#         print(i)

# n = int(input())
# i = 2
# while i * i <= n:
#     while n % i == 0:
#         print(i, end=' ')
#         n //= i
#     i += 1
# if n > 1:
#     print(n)


# def prost(s):
#     for i in range(2, int(s ** 0.5)+1):
#         if s % i == 0:
#             return False
#     return True


# def f(s):
#     a = set()
#     for i in range(2, int(s ** 0.5)+1):
#         if s % i == 0:
#             if prost(i):
#                 a.add(i)
#             elif prost(s // i):
#                 a.add(s // i)
#     return a


# n = int(input())
# for i in range(2, n+1):
#     if len(f(i)) >= 3:
#         print(i)



# n = int(input())
# cnt = [0] * (n + 1)
# for i in range(2, n + 1):
#     if cnt[i] == 0:
#         for j in range(i, n + 1, i):
#             cnt[j] += 1
# for i in range(2, n + 1):
#     if cnt[i] >= 3:
#         print(i)

# n = int(input())
# a = list(map(int, input().split()))
# prost_sp = []
# def prost(s):
#     for i in range(2, int(s ** 0.5)+1):
#         if s % i == 0:
#             return False
#     return True


# for i in range(1, 10**6 + 1):
#     if prost(i):
#         prost_sp.append(i)

# o = []
# for j in a:
#     o.append(prost_sp[j])
# print(*o)

# m = 1600000
# s = [1] * (m + 1)
# s[0] = s[1] = 0

# for i in range(2, int(m**0.5) + 1):
#     if s[i]:
#         for j in range(i*i, m+1, i):
#             s[j] = 0

# a = [i for i, j in enumerate(s) if j]

# n = int(input())
# o = list(map(int, input().split()))
# res = [a[k-1] for k in o]
# print(*res)

# n = int(input())
# m = [0] * (n + 1)
# for i in range(2, n + 1):
#     if m[i] == 0:
#         m[i] = i
#         for j in range(i * 2, n + 1, i):
#             if m[j] == 0:
#                 m[j] = i
# print(sum(m[2:]))


# from math import *
# x1, y1, x2, y2 = map(int, input().split())
# ans = gcd(abs(x2 - x1), abs(y2 - y1)) + 1
# print(ans)


# from math import *
# n, k = map(int, input().split())
# result = (n * k) // gcd(n, k)
# print(result)


# m = 10**6 + 3          
# n = int(input())         
# a, b = 1, 1              
# for i in range(2, n + 1):
#     a, b = b, (a + b) % m  
# print(b if n > 0 else a) 



# m = 10**6 + 7
# a, b = map(int, input().split())
# res = ((a * a - b * b) % m)
# print(res)


# m = 10**6 + 3
# n = int(input())
# if n >= m:
#     print(0)
# else:
#     f = 1
#     for i in range(1, n+1):
#         f = (f * i) % m
#     print(f)

# def task4(n, k, cur=''):
#   if len(cur) == n:
#     print(cur)
#     return
#   else:
#     for i in range (0, k):
#       task4(n, k, cur + str(i))

# n,k = map(int, input().split())
# task4(n, k)

# def counting_sort(arr) :
#     count = [0] * (max(arr) + 1)
#     for num in arr:
#         count[num] += 1
        
#     result = []
#     for num in range(len(count)):
#         result.extend([num] * count[num])
        
#     return 

# from collections import deque
# n, k = map(int, input().split())
# q = deque([n])
# res = 0
# while q:
#     s = q.popleft()
#     if s <= k:
#         res += 1
#     else:
#         q.append(s // 2)
#         q.append((s + 1) // 2)
# print(res)

# def part(n, max_v, c):
#     if n == 0:
#         print(*c)
#         return
#     for i in range(1, min(n, max_v) + 1):
#         part(n - i, i, c + [i])
# a = int(input())
# part(a, a, [])

# from itertools import permutations
# n, k = map(int, input().split())
# c = 0
# for p in permutations(range(1, n + 1)):
#     a = sum(p[i] * p[i + 1] for i in range(n - 1))
#     if a % k == 0:
#         c += 1
# print(c)

# from itertools import permutations
# n, k = map(int, input().split())
# c = 0
# for p in permutations(range(1, n + 1)):
#     a = sum(p[i] * p[i + 1] for i in range(n - 1))
#     if a % k == 0:
#         c += 1
# print(c)

# n = int(input())
# k = int(input())
# f = [1, 2]
# while f[-1] < n:
#     f.append(f[-1] + f[-2])
# def fi(t, a, c):
#     if t == 0:
#         print('+'.join(map(str, c)))
#         return
#     for i in range(a, len(f)):
#         if f[i] > t:
#             break
#         if c.count(f[i]) < k:
#             fi(t - f[i], i, c + [f[i]])
# fi(n, 0, [])

# def f(n):
#     if n <= 2:
#         return 1
#     return f(n - 1) + f(n - 2)
# n = int(input())
# print(f(n))

# a, b = map(int, input().split())
# l = int(b**0.5)
# p = [True] * (l + 1)
# p[0] = p[1] = False
# for i in range(2, int(l**0.5) + 1):
#     if p[i]:
#         for j in range(i * i, l + 1, i):
#             p[j] = False
# seg = [True] * (b - a + 1)
# if a == 1:
#     seg[0] = False
# for i in range(2, l + 1):
#     if p[i]:
#         s = max(i * i, (a + i - 1) // i * i)
#         for j in range(s, b + 1, i):
#             if j >= a:
#                 seg[j - a] = False
# res = []
# for i in range(len(seg)):
#     if seg[i]:
#         res.append(a + i)
# print(*res)

# def CountingSort(A):
#     c = [0] * 20001
#     for x in A:
#         c[x + 10000] += 1
#     r = []
#     for i in range(20001):
#         r.extend([i - 10000] * c[i])
#     return r
# n = int(input())
# A = list(map(int, input().split()))
# print(*CountingSort(A))

# def f(A, B):
#     res = []
#     i = 0
#     j = 0
#     while i < len(A) and j < len(B):
#         if A[i] < B[j]:
#             res.append(A[i])
#             i += 1
#         else:
#             res.append(B[j])
#             j += 1
#     res.extend(A[i:])
#     res.extend(B[j:])
#     return res

# def q(A):
#     if len(A) <= 1:
#         return A
#     mid = len(A) // 2
#     L = q(A[:mid])
#     R = q(A[mid:])
#     return f(L, R)

# n = int(input())
# if n == 0:
#     print()
# else:
#     A = list(map(int, input().split()))
#     print(*q(A))







p = int(input())
q = int(input())
if p > q:
    for i in range(1, p):
        if p % i == 0 and q % i == 0:
            print(p*q-i if i != 1 else p*q-i)
            break
else:
    for i in range(1, q):
        if p % i == 0 and q % i == 0:
            print(p*q-i if i != 1 else p*q-i)
            break