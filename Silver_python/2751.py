# 수 정렬하기 2

import sys

input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
  nums.append(int(input()))

nums.sort()

for num in nums:
  print(num)

# 포인트
# set은 sort() 메서드를 지원하지 않음
# 중복제거가 아닌이상 list로 쓰자
# input() 함수와 print() 함수가 기본적으로 느리다