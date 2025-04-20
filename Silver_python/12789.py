# 도키도키 간식드리미

import sys

input = sys.stdin.readline
n = int(input())
wait = list(map(int, input().split()))
tmp = []
target = 1

for i in wait:
  # wait를 순회하며 우선 tmp라는 stack에 넣어서 보관
  tmp.append(i)
  
  # target을 만날 경우에만 while문 실행
  while tmp and tmp[-1] == target:
    tmp.pop()
    target += 1
  
  # tmp의 마지막 원소가 가장 작은 수가 아닐때
  if len(tmp) > 1 and tmp[-1] > tmp[-2]:
    print("Sad")
    sys.exit()
  
if tmp:
  print("Sad")
else:
  print("Nice")
  
# 포인트
# 문제를 이해하는건 어렵지 않지만 분기처리를 잘 해야함