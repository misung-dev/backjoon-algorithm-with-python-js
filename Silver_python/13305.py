# 주유소

from sys import stdin

n = int(stdin.readline())
city = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))

total = 0
cheap = cost[0]

for i in range(n-1):
  if cost[i] < cheap:
    cheap = cost[i]
  total += cheap * city[i]

print(total)

# 포인트
# 구현은 어렵지 않았지만
# input()은 느릴 수 있기 때문에, 많은 입력을 처리할 땐 sys.stdin.readline() 사용하기