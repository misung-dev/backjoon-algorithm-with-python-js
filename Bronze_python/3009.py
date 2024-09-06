# 네 번째 점

x_list = []
y_list = []

for i in range(3):
  a, b = map(int, input().split())
  x_list.append(a)
  y_list.append(b)

for i in range(3):
  if x_list.count(x_list[i]) == 1:
    x4 = x_list[i]
  if y_list.count(y_list[i]) == 1:
    y4 = y_list[i]

print(x4, y4)