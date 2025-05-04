# 문자열 폭발

full_str = str(input())
explosion_word = str(input())

stack = []

for s in full_str:
  stack.append(s)

  # stack의 마지막 문자열이 explosion_word와 동일하면 폭발시킴
  if ''.join(stack[-len(explosion_word):]) == explosion_word:
    del stack[-len(explosion_word):]

if stack: 
  print(''.join(stack)) # stack의 모든 원소를 join함
else:
  print('FRULA')

# 포인트
# 처음에 단순히 생각해서 replace 혹은 find를 사용하려했으나, 역시 시간 초과가 발생했음
# 이는 문자열을 계속해서 탐색하기 때문에 매우 비효율적임