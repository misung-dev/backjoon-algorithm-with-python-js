# 단어 정렬

n = int(input())
words = set()

for _ in range(n):
  words.add(input().strip()) # 줄 바꿈 제거
  
sorted_words = sorted(words, key=lambda x: (len(x), x)) # 길이순 → 사전순 정렬


for word in sorted_words:
  print(word)