# 최대 힙

import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
  x = int(input())
  
  if x == 0:
    if not heap:
      print(0)
    else:
      print(-heapq.heappop(heap))
      
  else:
    heapq.heappush(heap, -x)
    

# 포인트
# 리스트 비었는지 확인은 == [] 말고 if not num_arr이 더 깔끔
# heapq.heappush(heap, -x)	최대 힙처럼 만들기 위해 음수로 넣음
# -heapq.heappop(heap)	꺼낼 때 다시 양수로 바꿔서 원래 값 출력

# 시간 초과 코드
# max_value = max(heap)
# idx = heap.index(max_value)
# del heap[idx]
# print(max_value)