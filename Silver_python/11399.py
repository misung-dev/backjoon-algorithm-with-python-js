# ATM

n = int(input())
order = list(map(int, input().split()))
order.sort()

current = 0
total = 0

for i in range(n):
  current += order[i] 
  total += current
  
print(total)

# 포인트
# 그리디 알고리즘(매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출) 사용