# 나는야 포켓몬 마스터 이다솜

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mon = []
name_to_idx = {}

for i in range(n):
  name = input().strip()
  mon.append(name)
  name_to_idx[name] = i + 1

for _ in range(m):
  j = input().strip()
  
  if j.isdigit():
    print(mon[int(j)-1])
  else:
    print(name_to_idx[j])
    
# 포인트
# 숫자 타입 검사하는 형식은 num.isdigit()
# 줄바꿈으로 입력받으려면 input().strip()
# 리스트는 앞에서부터 하나씩 탐색하기 때문에 O(n)의 시간이 걸리고 >> 계속 시간 초과 뜨는 원인
# 딕셔너리 조회는 O(1) >> 완전 중요