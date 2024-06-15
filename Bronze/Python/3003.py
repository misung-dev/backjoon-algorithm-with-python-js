num = list(map(int, input().split()))

original = [1,1,2,2,2,8]
piece = []

for i in range(6):
  gap = original[i] - num[i]
  piece.append(gap)

print(' '.join(map(str, piece)))