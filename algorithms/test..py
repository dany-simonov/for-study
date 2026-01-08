# # from math import gcd
# # m, n = map(int, input().split())
# # def f(q):
# #     b = set()
# #     for i in range(1, int(q ** 0.5) + 1):
# #         if q % i == 0:
# #             b.add(i)
# #             b.add(q // i)
# #     return sorted(b)
# # a = f(n)
# # d = [x for x in a if x >= m]
# # k = len(d)
# # c = 0
# # for i in range(k):
# #     for j in range(i +1, k):
# #         x = d[i]
# #         y = d[j]
# #         if gcd(x, y) == 1 and (x + y) in a:
# #             c += 1
# # print(c)

# # n = int(input())
# # s = input()
# # k = [0] * 26
# # for i in s:
# #     k[ord(i) - ord("a")] += 1
# # c = 0
# # r = []
# # for x in k:
# #     c += x
# #     r.append(c)
# # print(*r)


# # N = int(input())
# # def f(i):
# #     if i == 1:
# #         return 0
# #     if i < 1:
# #         return 10 ** 10
# #     r = min(f(i-2) + 1, f(i-3) + 1)
# #     if i % 2 == 0:
# #         r = min(r, f(i//2) + 5)
# #     return r

# # a = f(N)
# # print(a if a < 10 ** 10 else -1)


# # N = int(input())
# # i = 10 ** 10
# # d = [i] * (N+1)
# # d[1] = 0
# # for i in range(2, N + 1):
# #     r = d[i - 2] + 1
# #     if i >= 3:
# #         r = min(r, d[i - 3] + 1)
# #         d[i] = r
# #     if i % 2 == 0:
# #         r = min(r, d[i // 2] + 5)
# #         d[i] = r
# # a = d[N]
# # print(a if a < 10 ** 10 else -1)


# # N, M = map(int, input().split())
# # r = []
# # for i in range(N):
# #     a = list(map(int, input().split()))
# #     r.append(a)
# # if r[0][0] == -1 or r[N-1][M-1] == -1:
# #     print(-1)
# #     exit()
# # inf = 10 ** 20
# # d = [[inf] * M for w in range(N)]
# # d[0][0] = r[0][0]
# # for i in range(N):
# #     for j in range(M):
# #         if r[0][0] == -1 or (i == 0 and j == 0) or r[i][j] == -1:
# #             continue
# #         p = inf
# #         if j > 0:
# #             p = min(p, d[i][j-1])
# #         if i > 0:
# #             p = min(p, d[i-1][j])
# #         if i > 0 and j > 0:
# #             p = min(p, d[i-1][j-1])
# #         if p != inf:
# #             d[i][j] = p + r[i][j]
# # q = d[N-1][M-1]
# # print(q if q < inf else -1)

# # N, M, h, w, K = map(int, input().split())
# # mh = N // h
# # mw = M // w
# # r = min(mh, mw)
# # if r < 1:
# #     print(0)
# #     exit()
# # def f(a):
# #     q = N // (a * h)
# #     e = M // (a * w)
# #     return q * e >= K
# # if not f(1):
# #     print(0)
# # l = 1
# # a = 1
# # while l <= r:
# #     m = (l + r) // 2
# #     if f(m):
# #         a = m
# #         l = m + 1
# #     else:
# #         r = m - 1
# # print(a)

# N = int(input())
# s = input().split()
# Q = int(input())
# r = []
# for i in range(Q):
#     a = list(map(int, input().split()))
# r.append(a)
# a = 0
# b = 0
# for i in range(Q):
#     p = list(map(int, input().split()))
#     for j in range(s[p[0]], s[p[1]]):
#         z = a
#         y = b
#         if j == "a":
#             j += 1
#         if j == "b":
#             j += 1
#     if z > y:
#         print(z)
#     elif y > z:
#         print(y)
#     else:
#         print("0")