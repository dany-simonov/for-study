# p = int(input())
# q = int(input())
# if p == q:
#     print(1)
# else:
#     print(2)

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# u = list(map(int, input().split()))
# a1 = u[0]
# b1 = u[1]
# v = list(map(int, input().split()))
# a2 = v[0]
# b2 = v[1]
# if a1 % b2 == 0 or a2 % b1 == 0:
#     print(a1 * a2// gcd(a1, b2), b1 * b2// gcd(a2, b1))
# else:
#     print(a1 * a2, b1 * b2)


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# u = list(map(int, input().split()))
# a1 = u[0]
# b1 = u[1]
# v = list(map(int, input().split()))
# a2 = v[0]
# b2 = v[1]
# n = b1 * b2 // gcd(b1, b2)
# n2 = a1 * a2 // gcd(a1, a2)
# print(a1*a2//n, b1*b2//n2)


# u = list(map(int, input().split()))
# a = u[0]
# b = u[1]
# prost = [1] * (b + 1)
# prost[0] = prost[1] = 0
# for i in range(2, int(b ** 0.5)):
#     if prost[i]:
#         for j in range(i*i, b+1, i):
#             prost[j] = 0
# r = []
# for q in range(len(prost)):
#     if prost[q]:
#         r.append(q)
# p = set()
# for x in range(len(p)):
#     for z in range(x, len(p)):
#         if a <= p[x]*p[z] <= b:
#             p.add(p[x]*p[z])
# for l in p:
#     print(l)

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# u = list(map(int, input().split()))
# a1 = u[0]
# b1 = u[1]
# v = list(map(int, input().split()))
# a2 = v[0]
# b2 = v[1]
# print(a1*a2//gcd(a1*a2, b1*b2), b1*b2//gcd(a1*a2, b1*b2))

# def f(a):
#     if len(a) <= 1:
#         return a, 0
#     m = len(a) // 2
#     l, c1 = f(a[:m])
#     r, c2 = f(a[m:])
#     s = []
#     i = j = 0
#     c = c1 + c2
#     while i < len(l) and j < len(r):
#         if l[i] <= r[j]:
#             s.append(l[i])
#             i += 1
#         else:
#             s.append(r[j])
#             c += len(l) - i
#             j += 1
#     s.extend(l[i:])
#     s.extend(r[j:])
#     return s, c

# n, L = map(int, input().split())
# w = list(map(int, input().split()))
# t = [i + L * w[i] for i in range(n)]
# s, q = f(t)
# print(q)


# s = list(map(str, input().split()))
# k = int(input())
# t = ""
# for j in s:
#     c = 1
#     for i in j:
#         t += i * c
#         c += 1
#     t += " "
# print(t[k])

# s = list(map(str, input().split()))
# k = int(input())
# t = ""
# for j in s:
#     c = 1
#     for i in j:
#         t += i * c
#         c += 1
#     t += " "
#     if k <= len(t):
#         break
# print(t[k])


# s = input().split()
# k = int(input())
# for w, j in enumerate(s):
#     c = 1
#     for i in j:
#         if k < c:
#             print(i)
#             exit()
#         else:
#             k -= c
#             c += 1
#     if w < len(s) - 1:
#         if k == 0:
#             print(" ")
#             exit()
#         else:
#             k -= 1
#     else:
#         print(i)
#         exit()


# n = int(input())
# r = []
# m = 0
# c = 0
# for i in range(n-1):
#     a = input().split()
#     u, w = a[0], a[1]
#     r.append([u, w])
# colors = list(map(int, input().split()))
# for j, q in r:
#     if colors[j] == colors[q]:
#         c += 1
#         m = max(m, c)
# print(m)


# import sys
# sys.setrecursionlimit(100000)

# n = int(input())
# r = [[] for x in range(n)]
# for i in range(n - 1):
#     u, v = map(int, input().split())
#     r[u].append(v)
#     r[v].append(u)
# colors = list(map(int, input().split()))
# m = 1
# def dfs(u, p):
#     global m
#     c = 1
#     color1 = True
#     for v in r[u]:
#         if v != p:
#             s, q = dfs(v, u)
#             if colors[v] != colors[u] or not q:
#                 color1 = False
#             else:
#                 c += s
#     if color1:
#         m = max(m, c)
#         return c, True
#     else:
#         return 0, False
# dfs(0, -4)
# print(m)

for i in range(27):
    print(f"{i})")
    
    
    # p = int(input())
# q = int(input())
# r = int(input())
# if p != q and p != r and r != q:
#     print(8)
# elif p == q and p == r:
#     print(4)
# else:
#     print(6)

# a1, b1 = map(int, input().split())
# a2, b2 = map(int, input().split())
# if a1 / b1 > a2 / b2:
#     print(">")
# elif a1 / b1 < a2 / b2:
#     print("<")
# else:
#     print("=")

# N = int(input())
# p = []
# def f(r, l, c):
#     if r == 0:
#         p.append(c.copy())
#         return
#     lim = min(r, l)
#     x = 1
#     while x <= lim:
#         c.append(x)
#         f(r-x, x, c)
#         c.pop()
#         x += 1
# f(N, N, [])

# ans = set()
# print(p)
# for q in p:
#     for d in q:
#         print(100, p, 100, q, 100, d)
#         if q.count(d) == 1:
#             print(q)
#         else:
#             continue
#             # ans.add(q)
# for t in ans:
#     print(t)

# for q in range(len(p)):
#     if len(q) > 1:
#         if :
#             print(*q)
#     else:
#         print(*q)


A, B = map(int, input().split())
prost = [1] * (B+1)
prost[0] = prost[1] = 0
for i in range(int(B ** 0.5) + 1):
    if prost[i]:
        for j in range(i*i, B, i):
            prost[j] = 0
prime = [q for q in range(A, B) if prost[q]]

ans = []
for z in range(len(prime)):
    for x in range(z, len(prime)):
        if prime[z] * prime[x] > B:
            break
        elif prime[z] * prime[x] >= A:
            if prime[z] != prime[x]:
                ans.append(prime[z] * prime[x])
for t in sorted(ans):
    print(t)


# ans = []
# for z in range(len(prime)):
#     for x in range(z, len(prime)):
#         if prime[z] * prime[x] > B:
#             break
#         elif prime[z] * prime[x] >= A:
#             if prime[z] != prime[x]:
#                 ans.append(prime[z] * prime[x])
# for t in sorted(ans):
#     print(t)


# n = int(input())
# a = list(map(int, input().split()))
