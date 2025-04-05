# 붙임성 좋은 총총이

n = int(input())
dancer = set()
dancer.add('ChongChong')

for _ in range(n):
  a, b = map(str, input().split())
  
  if (a in dancer) or (b in dancer):
    dancer.add(a)
    dancer.add(b)
    
print(len(dancer))

# 포인트
# set()의 이해