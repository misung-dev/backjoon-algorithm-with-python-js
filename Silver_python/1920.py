# 수 찾기

n = int(input())
nset = set(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

for num in mlist:
  print(1 if num in nset else 0)
  
# 포인트
# set은 내부적으로 해시를 사용해서 in 연산이 평균적으로 O(1)