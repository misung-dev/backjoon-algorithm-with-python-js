# 피보나치 수 5

n = int(input())

# 재귀함수
# 특정 조건을 충족하면 다시 자기 자신을 호출
def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))
