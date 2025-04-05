# 인사성 밝은 곰곰이

n = int(input())
total_count = 0
user_set = set()

for _ in range(n):
  value = str(input())
  
  if value == 'ENTER':
    total_count += len(user_set)
    user_set.clear()
  else:
    user_set.add(value)

print(total_count + len(user_set))   

# 포인트
# set()의 특징: 중복 허용 X, 순서 X, 집합 연산 가능 (합, 교, 차집합 등)
# set()의 선언, 원소 추가, 초기화 방법

# 요소 갯수 구하는 방법
# len(): 리스트의 요소 개수 구하기 
# count(): 리스트의 특정 요소 개수 구하기 -> set은 중복을 허용하지 않기 때문에 사용X
# ex)
# i = [1,1,3,4,5,3,3,7,6,8,9,3,2,5,9]
# print(i.count(3)) #리스트i에 요소3의 개수 구할때 
# >>> 4  