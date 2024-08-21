count = int(input())
scores = list(map(int, input().split()))
m = max(scores)

for i in range(count):
  scores[i] = scores[i]/m * 100

print(sum(scores)/count)

