# 행렬 곱셈

# 입력받기
n, m = map(int, input().split())
a = []

for _ in range(n):
  row = list(map(int, input().split()))
  a.append(row)

m2, k = map(int, input().split())
b = []

for _ in range(m2):
  row = list(map(int, input().split()))
  b.append(row)

# 곱셈 계산
result = []

for i in range(n):
  row_result = []
  
  for j in range(k):
    result_sum = 0
    
    for l in range(m):
      result_sum += a[i][l] * b[l][j]
    
    row_result.append(result_sum)
  
  result.append(row_result)

# 결과 출력
for row in result:
  print(' '.join(map(str, row)))