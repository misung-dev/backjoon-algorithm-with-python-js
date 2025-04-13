# 베르트랑 공준

import math
import sys

input = sys.stdin.readline

# 소수를 미리 구해두기 위한 최대 범위 (2 * 123456)
MAX = 246913
is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체 적용 (소수 리스트 만들기)
for i in range(2, int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime[i]:
            count += 1

    print(count)
    
# 포인트
# 소수 구할 줄 알아함. 근데 그게 어려움