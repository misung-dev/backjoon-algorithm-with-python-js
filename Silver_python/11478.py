# 서로 다른 부분 문자열의 개수

import sys

input = sys.stdin.readline

s = input().strip()
n = len(s)

substrings = set()

for i in range(n):
  for j in range(i + 1, n + 1):
    substrings.add(s[i:j])

print(len(substrings))