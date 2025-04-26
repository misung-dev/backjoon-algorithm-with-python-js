# 파도반 수열

import sys

input = sys.stdin.readline

T = int(input())
tlist = []
wave = [1, 1, 1]

for _ in range(T):
  n = int(input())
  tlist.append(n)

tmax = max(tlist)

for i in range(3, tmax):
  wave.append(wave[i-3] + wave[i-2])

for j in tlist:
  print(wave[j-1])

# 포인트
# sys.stdin.readline()의 결과값은 문자열이다.