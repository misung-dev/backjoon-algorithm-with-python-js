# 듣보잡

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nset = set()
result = []

for _ in range(n):
  nset.add(input().strip()) # 줄바꿈 제거

for _ in range(m):
  name = input().strip()
  
  if name in nset:
    result.append(name)

print(len(result))

for name in sorted(result):
  print(name)
  
# 포인트
# 처음 작성한 'if j in nlist:' 이 부분에서 리스트를 선형 탐색하므로, 최악의 경우 O(N*M) 시간이 걸림
# set은 평균적으로 in 연산자가 O(1)이기 때문에, 탐색 속도가 훨씬 빠름