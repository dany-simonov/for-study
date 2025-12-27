# # from math import *
# # N, K = map(int, input().split())
# # if K == ceil(log2(N)):
# #     print("Yes")
# # else:
# #     print("No")

# # N, M = map(int, input().split())
# # a = list(map(int, input().split()))
# # t = 0

# # n = int(input())
# # dp0 = [0] * (n + 1)
# # dp1 = [0] * (n + 1)
# # dp2 = [0] * (n + 1)
# # dp0[1] = dp1[1] = dp2[1] = 1
# # for i in range(2, n+1):
# #     dp0 = dp1 + dp2
# #     dp1 = dp0 + dp2
# #     dp2 = dp1 + dp0


# # n = int(input())
# # dp = [1, 1, 1]
# # for i in range(n - 1):
# #     a, b, c = dp
# #     dp = [b + c, a + c, a + b]
# # print(sum(dp))

# # N, M = map(int, input().split())
# # def f(a, b):
# #     return t[a][b]
# # t = []
# # for N in range(N):
# #     a = list(map(int, input().split()))
# #     t.append(a)
# # print(t)
# # m = t[0][0]
# # for j in range(0, len(t)-1):
# #     for i in range(j, len(t)-1):
# #         print(i, j)
# #         m += min(f(i+1, j), f(i, j+1))
# # print(m)


# N, M = map(int, input().split())
# t = []
# for i in range(N):
#     a = list(map(int, input().split()))
#     t.append(a)
# m = t[0][0]
# def f(a, b):
#     return t[a][b]
# for j in range(0, len(t)):
#     for i in range(0, j):
#         m += max(f(i+1, j), f(i, j+1))
# print(m)

# N, M = map(int, input().split())
# t = []
# for i in range(N):
#     a = list(map(int, input().split()))
#     t.append(a)
# m = t[0][0]
# def f(a, b):
#     return t[a][b]
# for j in range(0, len(t)):
#     for i in range(0, j):
#         m += max(f(i+1, j), f(i, j+1))
# print(m)

# N, M = map(int, input().split())
# t = []
# for i in range(N):
#     a = list(map(int, input().split()))
#     t.append(a)
# for j in range(1, M):
#     t[0][j] += t[0][j-1]
# for i in range(1, N):
#     t[i][0] += t[i-1][0]
# for q in range(1, N):
#     for j in range(1, M):
#         t[q][j] += max(t[q-1][j], t[q][j-1])
# print(t[N-1][M-1])
