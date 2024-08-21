# 단어 공부

# 단어 입력받기
word = str(input().upper())

# 각 문자의 빈도를 저장할 dictionary 초기화
word_dict = {}

# 입력된 단어의 각 문자에 대해 빈도수 세기
for char in word:
  if char in word_dict:
    word_dict[char] += 1
  else:
    word_dict[char] = 1

# 빈도 수 중에서 최대값 찾기
max_value = max(word_dict.values())

# 최대값을 가진 문자 찾기
max_char = []
for k, v in word_dict.items():
  if v == max_value:
    max_char.append(k)

# 결과 출력
if len(max_char) > 1:
  print('?')
else :
  print(max_char[0])