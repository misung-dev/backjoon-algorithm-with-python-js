# 색종이

import sys

num = int(input())
papers = [[0] * 100 for _ in range(100)]

for i in range(num):
  row, col = map(int, input().split())
  for r in range(row, row+10):
    for c in range(col, col+10):
      papers[r][c] = 1

count = 0
for i in papers:
  count += i.count(1)

print(count)
