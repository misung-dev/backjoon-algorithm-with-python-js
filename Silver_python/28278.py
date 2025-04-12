# 스택 2

import sys

input = sys.stdin.readline

n = int(input())
n_list = []

for _ in range(n):
  a = list(map(int, input().split()))
  
  if a[0] == 1:
    n_list.append(a[1])
  
  if a[0] == 2:
    if len(n_list) >= 1:
      print(n_list[-1])
      n_list.pop()
    else:
      print(-1)
  
  if a[0] == 3:
    print(len(n_list))
    
  if a[0] == 4:
    if len(n_list) == 0:
      print(1)
    else:
      print(0)
  
  if a[0] == 5:
    if len(n_list) >= 1:
      print(n_list[-1])
    else:
      print(-1)

# 포인트
# 입력이 1개일때, 2개일때 있음 >> 이런경우 입력을 받아봐야 아는데
# 리스트로 처리하기