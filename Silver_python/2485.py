# 가로수

import sys
import math
from functools import reduce # 리스트나 배열 같은 걸 하나씩 차례로 줄여가면서 최종 결과를 만드는 함수

input = sys.stdin.readline
n = int(input())
nlist = []

for _ in range(n):
  num = int(input())
  nlist.append(num)

diff = []

for i in range(n-1):
  diff.append(nlist[i+1] - nlist[i])

# 리스트(diff)에 대해 여러 수의 최대공약수를 구하고 싶으면 reduce를 써야함
nlist_gcd = reduce(math.gcd, diff)

tree_count = (nlist[-1] - nlist[0]) // nlist_gcd + 1

print(tree_count - n)

# 코드 개선 방안
# 처음에는 최대공약수만큼 거리를 이동하며 가로수가 없는 위치를 찾아 새로운 배열에 추가하고, 
# 최종적으로 그 배열의 개수를 세어 필요한 가로수 수를 구했다. 
# 그러나 이후에는 가로수의 처음과 끝 위치를 이용해 전체 필요한 가로수 수를 계산한 뒤, 
# 기존에 있는 가로수 수를 빼서 최종적으로 심어야 할 가로수 수를 구하는 방식으로 개선했다.