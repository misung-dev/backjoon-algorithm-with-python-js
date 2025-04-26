# 대칭 차집합

a, b = map(int, input().split())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

total = len(s1.difference(s2)) + len(s2.difference(s1))

print(total)