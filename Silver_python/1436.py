# 영화감독 숌

n = int(input())
count = 0
result  = 666

while True:
  if '666' in str(result):
    count += 1
  
  if count == n:
    break
  
  result += 1

print(result)

# 포인트
# n번째로 큰 수를 찾는 것이므로, 숫자를 1씩 증가시키며 '666'이 연속으로 포함된 수를 찾는다.