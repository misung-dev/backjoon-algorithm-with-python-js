# 다음 소수

# 단순 소수 판별
def isPrimeNumber(x):
  if x < 2:
    return False

  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True # 모든 수로 나누어 떨어지지 않으면 소수

# n보다 크거나 같은 수 중 소수 찾기
def findPrimesGreaterThanOrEqual(n):
  while True:
    if isPrimeNumber(n):
      return n
    n += 1 # n를 증가시키며 소수 찾기

t = int(input())

for _ in range(t):
  n = int(input())
  print(findPrimesGreaterThanOrEqual(n))

# 포인트
# 소수를 판별할 때 최적화된 방법으로 x의 제곱근까지만 검사하는 방식 적용