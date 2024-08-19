# 나머지
nums = []

for i in range (10):
  num = int(input())
  bal = num % 42
  nums.append(bal)

# 중복된 값을 제거하기 위해 set 사용
unique = set(nums)

# 고유한 값들의 개수를 출력
print(len(unique))