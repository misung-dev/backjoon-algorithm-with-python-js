# 카드2

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
  cards.popleft()
  cards.append(cards.popleft()) 

# for i in range(1, n+1):
#   cards.append(i)

# while len(cards) > 1:
#   tmp = cards[1]
#   cards.pop(0)
#   cards.pop(0)
#   cards.append(tmp)

print(cards[0])

# 포인트
# deque를 사용하지 않고 반복문을 통해 문제 해결을 하려고 하면,
# 런타임 에러, 시간 초과가 반복적으로 생김
# 따라서 deque 사용하기