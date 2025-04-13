# 괄호

n = int(input())

for _ in range(n):
  a = str(input())
  stack = []
  
  for i in a:
    if i =='(':
      stack.append(i)
    elif i == ')':
      if stack:
        stack.pop()
      else:
        print('NO')
        break
  
  else:
    if not stack:
      print('YES')
    else:
      print('NO')
        
# 포인트
# for문이 정상적으로 종료되었을때 else문을 사용할 수 있다