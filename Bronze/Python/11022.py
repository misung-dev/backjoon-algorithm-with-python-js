# solution1
count = int(input())

for i in range (count):
  num1, num2 = map(int, input().split())
  sum = num1 + num2
  print('Case #' + str(i+1) + ': ' + str(num1) + ' + ' + str(num2) + ' = ' + str(sum))

# solution2
count = int(input())

for i in range (count):
  num1, num2 = map(int, input().split())
  sum = num1 + num2
  print(f'Case #{i+1}: {num1} + {num2} = {sum}')
