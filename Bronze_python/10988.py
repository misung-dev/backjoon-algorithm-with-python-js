# 팰린드롬인지 확인하기

word = str(input())
reversed = word[::-1]

if word == reversed :
  print(1)
elif word != reversed:
  print(0)