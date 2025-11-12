# a = list(input().split())
# name = list(input().split())
# n = len(a) % len(name)
# print(name[n-1])

# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b >= c or c >= b >= a:
#     print(b)
# elif a >= c >= b or b >= c >= a:
#     print(c)
# else:
#     print(a)

# k = int(input())
# print(*range(24 * k, 24 * k + 24))

# n = int(input())
# sd = []
# sm = []
# for i in range(n):
#     m, l = list(map(int, input().split()))
#     if m == 0:
#         sd.append(l)
#     else:
#         sm.append(l)
# m = 0
# for j in sorted(sd):
#     m = max(m, sd[j] - sd[j-1])
# for k in sorted(sm):
#     m = max(m, sd[k] - sd[k-1])
# print(m)

# n = int(input())
# s = 0
# for i in range(1, n+1):
#     s += ((2*i-1)/(2*i+1))
# print(round(s, 2))

# a = list(map(int, input().split()))
# print(min(i for i in a if i > 0))
# def pal(s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1
#         r += 1
#     return l + 1, r - 1


# s = input()
# n = len(s)
# m = []
# for i in range(len(s)-2):
#     if s[i] == s[i+2]:
#         m.append(s[i:i+2+1])
#         for j in range(1, 122):
#             if s[i-j] == s[i+2+j]:
#                 m.append(s[i-j:i+2+j+1])
#             else:
#                 break
# print(max(m, key=len))


# import sys
# def fibonacci(n:int) -> str:
#     if n == 1:
#         return "a"
#     elif n == 2:
#         return "b"
#     else:
#         return fibonacci(n-2)+fibonacci(n-1)
# exec(sys.stdin.read())

# a = list(map(int, input().split()))
# b = set()
# s = []
# for i in a:
#     if i in b:
#         s.append("YES")
#     else:
#         s.append("NO")
#         b.add(i)
# for j in s:
#     print(j)

# N = int(input())
# K = int(input())
# if N % 2 == 0:
#     if K % 2 == 0:
#         print((N // 2 + 1) * (K // 2 + 1))
#     else:
#         print((N // 2 + 1) * (K+1) // 2)
# else:
#     if K % 2 == 0:
#         print((N+1) // 2 * (K // 2 + 1))
#     else:
#         print((N+1) // 2 * (K+1) // 2)

# k = int(input())
# a = list(map(int, input().split()))
# s = int(input())
# mi = 10 ** 10
# for i in range(k):
#     mi = min(abs(a[i] - s), mi)
# for j in range(k):
#     if abs(a[j] - s) == mi:
#         print(a[j])
#         break