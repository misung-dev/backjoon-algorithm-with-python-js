# 영단어 암기는 괴로워

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for _ in range(n):
  word = input().strip()
  
  if (len(word) >= m):
    if not dict.get(word):
      dict[word] = 1
    
    else:
      dict[word] += 1

# 우선순위에 따른 정렬 (튜플형태로)
sorted_dict = sorted(dict.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

# 단어장 출력
for word, _ in sorted_dict:
  print(word)

# 포인트
# 왜 -를 붙이는가? 파이썬 기본 정렬은 오름차순이라서.
# 축약 버전
  # 이전
  #   if (len(word) >= m):
  #     if not dict.get(word):
  #       dict[word] = 1
  #     else:
  #       dict[word] += 1
  
  # 이후
  #     if len(word) >= m:
  #         word_dict[word] = word_dict.get(word, 0) + 1
  # dict.get(word, 0)은 word가 없으면 기본값으로 0을 줌
  
# 왜 .strip()이 필요할까?
  # sys.stdin.readline()은 줄 끝에 **\n (줄바꿈 문자)**를 포함해서 읽어오기 때문 
  # `.strip()`을 사용하면 'apple\n' → 'apple'로 깔끔하게 바뀜