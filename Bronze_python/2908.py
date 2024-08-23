# 상수

a, b = map(str, input().split())

newA = int(a[::-1])
newB = int(b[::-1])

if newA > newB:
  print(newA)
else:
  print(newB)