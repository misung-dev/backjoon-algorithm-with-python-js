count, num = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(count):
  if num_list[i] < num:
    print(num_list[i], end=' ')