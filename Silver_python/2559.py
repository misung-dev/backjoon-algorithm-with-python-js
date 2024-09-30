# 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

part_sum =sum(arr[:k])
result = part_sum

for i in range(n-k):
  part_sum += arr[i+k] - arr[i]
  if result < part_sum:
    result = part_sum

print(result)

# 슬라이딩 윈도우 알고리즘?

# 고정된 크기의 범위에서 합 또는 다른 연산을 효율적으로 계산하기 위해 사용
# 각 범위에 대한 합을 새로 계산하지 않고, 이전 범위에서 계산한 값을 바탕으로 빠르게 다음 범위의 값을 구할 수 있음

# 범위 합을 구할때 시간상의 효율을 구하기 위해 
# i번째 범위합은 i-1번째 범위합에서 왼쪽 끝을 빼고 오른쪽 끝을 더해주는 것
