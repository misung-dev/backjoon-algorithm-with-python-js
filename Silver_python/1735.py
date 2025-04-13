# 분수 합

import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

b3 = math.lcm(b1, b2)
a3 = ((b3//b1) * a1) + ((b3//b2) * a2)

# 기약분수 구하기
g = math.gcd(a3, b3)

print(a3//g, b3//g)

# 포인트
# gcd, lcm으로 최대공약수, 최소공배수 구하기