count = int(input())
numList = []
sum = 0

for i in range(count):
  num = int(input())
  if (num == 0) and len(numList) > 0:
    numList.pop(-1)
  else:
    numList.append(num)

for i in numList:
  sum += i

print(sum)