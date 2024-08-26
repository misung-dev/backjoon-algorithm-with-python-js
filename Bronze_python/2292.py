# 벌집

num = int(input())
count = 1
total = 1

while total < num:
  total += 6 * count
  count += 1

print(count)