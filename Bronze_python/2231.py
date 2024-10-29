# 분해합

n = int(input())
result = 0

for i in range(1, n+1):
  num = list(map(int, str(i)))  # sum(num)은 리스트 요소를 모두 더할 수 있음
  result = i + sum(num) # i와 i의 각 자리 수를 더함

  if result == n:
    print(i)
    break

  if i == n:
    print(0)