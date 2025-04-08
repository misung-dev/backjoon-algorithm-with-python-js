# 약수

n = int(input())
num_list = list(map(int, input().split()))

if n == 1:
  print(num_list[0] ** 2)
else:
  min_value = min(num_list)
  max_value = max(num_list)
  print(min_value * max_value)
  
# 포인트
# 규칙을 잘 파악만 하면 easy!