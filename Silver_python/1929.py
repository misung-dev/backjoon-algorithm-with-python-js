# 소수 구하기

m, n = map(int, input().split())

def isPrime(x):
  if x < 2:
    return False
  
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False

  return True

for j in range(m, n+1):
  if isPrime(j):
    print(j)

