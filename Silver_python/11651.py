# 좌표 정렬하기 2

import sys

input = sys.stdin.readline

n = int(input())
nlist = []

for _ in range(n):
  m = list(map(int, input().split()))
  nlist.append(m)

nlist.sort(key=lambda x: (x[1], x[0]))

for a, b in nlist:
  print(a, b)