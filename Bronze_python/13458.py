# 시험 감독

# solution1
room = int(input())
num_list = list(map(int, input().split()))
director, assistant = map(int, input().split())

count = room

for student in num_list:
  if (student - director) > 0:
    remain = student - director

    if remain % assistant == 0:
      count += remain // assistant
    else:
      count += remain // assistant + 1

print(count)

# solution2
# import math

# room = int(input())
# num_list = list(map(int, input().split()))
# director, assistant = map(int, input().split())

# count = room

# for student in num_list:
#   if (student - director) > 0:
#     remain = student - director
#     count += math.ceil(remain / assistant)

# print(count)