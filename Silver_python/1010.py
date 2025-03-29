# 다리 놓기

import math

t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))

  print(bridge)
  
# 포인트
# 조합 공식 활용
# 조건: N ≤ M