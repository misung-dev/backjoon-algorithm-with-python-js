# 이항 계수 1

import math

n, k = map(int, input().split())
value = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

print(value)


# 이항계수(Binomial Coefficient)?
# 주어진 크기 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 가짓수
# 2를 상징하는 ‘이항’이라는 말이 붙은 이유는 하나의 아이템에 대해서는 ‘뽑거나, 안 뽑거나’ 두 가지의 선택만이 있기 때문

# 포인트
# 이항 계수는 항상 정수가 나와야 하기 때문에 /가 아닌 //로 정수 나눗셈을 해야함