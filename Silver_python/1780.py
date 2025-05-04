# 종이의 개수

n = int(input())
arr = []

# 2차원 배열 생성
for _ in range(n):
  row = list(map(int, input().split()))
  arr.append(row)

# 결과 담기
result = [0, 0, 0]

# 탐색: 각 구간이 동일한 값으로 이루어졌는지 확인
def count_paper(x, y, size):
  num = arr[x][y]

  for i in range(x, x+size):
    for j in range(y, y+size):
      if arr[i][j] != num:
        return False
  
  return True

# 전체 # 분할 정복: 3x3으로 구간을 나누어 탐색
def process_paper(x, y, size):
  if size == 1:
    result[arr[x][y] + 1] += 1
    return
  
  if count_paper(x, y, size):
    result[arr[x][y] + 1] += 1
  else:
    new_size = size // 3
    for i in range(3):
      for j in range(3):
        process_paper(x + i * new_size, y + j * new_size, new_size)

# 탐색 시작
process_paper(0, 0, n)

# 결과 출력
for res in result:
  print(res)