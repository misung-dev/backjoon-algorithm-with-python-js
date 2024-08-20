# 세로읽기
words = [input() for i in range(5)]

for j in range(15):  # 최대 15회 반복
  for i in range(5):
    if j < len(words[i]):  # 현재 단어의 길이를 초과하지 않는 경우에만
      print(words[i][j], end='')