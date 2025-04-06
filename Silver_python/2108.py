# 통계학

from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
  nums.append(int(input()))
  
nums.sort()

def get_avg(nums):
  return round(sum(nums) / len(nums))

def get_median(nums):
  return nums[len(nums) // 2]

def get_mode(nums):
    counter = Counter(nums)
    max_count = max(counter.values())

    modes = [
        num for num, cnt in counter.items()
        if cnt == max_count
    ]
    modes.sort()

    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]

def get_range(nums):
  return nums[-1] - nums[0]    

print(get_avg(nums))  
print(get_median(nums))
print(get_mode(nums))
print(get_range(nums))

# 포인트
# Counter는 리스트 안에 있는 각 숫자의 등장 횟수를 세는 dict 형태의 객체
# nums = [1, 1, 2, 2, 3]
# Counter(nums) → {1: 2, 2: 2, 3: 1}