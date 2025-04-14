# 세 막대

sticks = list(map(int, input().split()))
sticks.sort()

if sticks[0] + sticks[1] > sticks[2]:
  print(sum(sticks))
else:
  print(sticks[0] + sticks[1] + (sticks[0] + sticks[1]) - 1)

# 포인트
# 삼각형을 만드는 기본 조건에 충실하자