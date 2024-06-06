a, b, c = map(int, input().split())
num_list = []
num_list.extend([a, b, c])

if a == b == c:
  result = 10000 + num_list[0]*1000
elif (a == b != c) or (a == c != b):
  result = 1000 + a * 100
elif b == c != a:
  result = 1000 + b * 100
else:
  result = max(num_list) * 100

print(result)