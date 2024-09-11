# 대지

num = int(input())
x_list =[]
y_list = []
row = 0
column = 0

for i in range(num):
  x, y = map(int, input().split())

  x_list.append(x)
  y_list.append(y)

row = max(x_list) - min(x_list)
column = max(y_list) - min(y_list)

print(row * column)