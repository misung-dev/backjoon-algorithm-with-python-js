# 잃어버린 괄호 (그리디 알고리즘)
expression = str(input())
arr = []
value = ''

# 숫자와 연산자 분리
for i in range(len(expression)):
  if (expression[i] == '-') :
    arr.append(int(value)) 
    arr.append('-')
    i += 1
    value = ''  

  elif (expression[i] == '+'):
    arr.append(int(value))    
    arr.append('+')
    i += 1
    value = ''  

  else:
    value += expression[i]

arr.append(int(value))

# 연산자에 따라 계산
sum = 0
j = 1

while j < len(arr) - 1:
  if (arr[j] == '+'):
    sum = arr[j-1] + arr[j+1]
    del arr[j-1:j+2]
    arr.insert(j-1, sum)
    j -= 1
  else:
    j += 1 

# 순회하면서 뺄셈
total = arr[0]

for k in range(2, len(arr), 2):
  total -= arr[k]

# 출력
print(total)
