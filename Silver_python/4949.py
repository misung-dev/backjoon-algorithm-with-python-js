# 균형잡힌 세상

while True:
  sentence = str(input())
  if sentence == '.':
    break
  
  stack = []
  is_balanced = True
  
  for i in sentence:
    if i == '[' or i == '(':
      stack.append(i)
    elif i == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        is_balanced = False
        break
    elif i == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        is_balanced = False
        break
  
  if is_balanced and not stack:
    print('yes')
  else:
    print('no')
    
# 포인트
# stack이 비어있으면서 괄호 조건이 맞아야함
# 이를 위해 is_balanced로 괄호 조건이 맞는지 체크
 