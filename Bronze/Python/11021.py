count = int(input())

for i in range(1, count+1):
  num1, num2 = map(int, input().split())
  sum = num1 + num2
  print('Case #' + str(i) + ': ' +str(sum))