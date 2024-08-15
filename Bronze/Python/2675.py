count = int(input())
for i in range(count):
  num, alpha = input().split()
  num = int(num)
  word = ''

  for j in alpha:
    word += j*num
  
  print(word)