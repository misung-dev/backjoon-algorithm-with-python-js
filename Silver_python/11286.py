# 절댓값 힙

import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
  num = int(input())
  
  if num == 0:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  
  else:
    heapq.heappush(heap, (abs(num), num))
    
# 포인트
# 힙과 튜플 동시에 이용하기
# 차이 비교
# heapq.heappop(heap)[1] → 힙에서 가장 우선순위 높은 튜플의 두 번째 값 꺼냄
#   heap = [(1, -1), (2, 2)]
#   heapq.heappop(heap) → (1, -1)
#   (1, -1)[1] → -1
# heapq.heappop(heap[1]) → 힙 안의 두 번째 요소를 꺼냄
#   heapq.heappop((2, 2)) # ❌ TypeError 발생
#   heapq.heappop()은 리스트를 수정하면서 pop하는 함수
#   (2, 2)는 리스트가 아니라 그냥 튜플(값)이라서 pop 불가능!

# 파이썬 heapq의 기본 정렬 기준
# 기본적으로 최소 힙(Min Heap) 구조를 사용해
# "가장 작은 값이 루트(맨 앞)에 오도록" 정렬된다.  