# 바구니 뒤집기
n, m = map(int, input().split())
order = [i for i in range(1, n+1)]

for i in range (m):
  start, end = map(int, input().split())
  order[start-1 : end] = order[start-1 : end][::-1]

for i in range(n):
  print(order[i], end=' ')