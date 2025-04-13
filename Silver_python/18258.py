# 큐 2

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue_list = deque()

for _ in range(n):
  n_list = input().split()
  
  if (n_list[0] == 'push'):
    queue_list.append(n_list[1])
    
  elif(n_list[0] == 'pop'):
    if queue_list:
      print(queue_list.popleft())
    else:
      print(-1)
    
  elif(n_list[0] == 'size'):
    print(len(queue_list))
    
  elif(n_list[0] == 'empty'):
    if not queue_list:
      print(1)
    else:
      print(0)
    
  elif(n_list[0] == 'front'):
    if queue_list:
      print(queue_list[0])
    else:
      print(-1)
        
  elif(n_list[0] == 'back'):
    if queue_list:
      print(queue_list[-1])
    else:
      print(-1)
    
# 포인트 
# from collections import deque 사용해보기
# deque에서는 queue_list.pop(0) 대신해서 popleft() 사용하기. 