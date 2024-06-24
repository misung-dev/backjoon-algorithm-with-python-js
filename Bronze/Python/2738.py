arr1, arr2 = [], []
n, m = map(int, input().split())

for row in range(n):
    row = list(map(int, input().split()))
    arr1.append(row)

for row in range(n):
    row = list(map(int, input().split()))
    arr2.append(row)
    
for row in range(n):
    for col in range(m):
        print(arr1[row][col] + arr2[row][col], end=' ')
    print()