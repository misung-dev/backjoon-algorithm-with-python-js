# N번째 큰 수

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
  numbers = list(map(int, input().split()))
  for num in numbers:
    heapq.heappush(heap, num)
    if len(heap) > n:
      heapq.heappop(heap)
  
print(heap[0])

# 포인트
# heap 잘 활용하기