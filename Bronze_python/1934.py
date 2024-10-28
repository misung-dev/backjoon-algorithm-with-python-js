# 최소공배수

import math

def lcm(x, y):
  return x * y // math.gcd(x, y)

num = int(input())

for i in range(num):
  num1, num2 = map(int, input().split(' '))
  print(lcm(num1, num2))