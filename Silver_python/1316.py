# 그룹 단어 체커

num = int(input())
count = num

for i in range(num):
  word = str(input())
  
  for i in range(len(word)-1):
    if word[i] == word[i+1]: 
      pass
    elif word[i] in word[i+1:]:
      count -= 1
      break

print(count)