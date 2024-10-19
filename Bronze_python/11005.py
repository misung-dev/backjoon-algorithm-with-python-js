# 진법 변환 2

num, formation = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while num:
    s += str(arr[num%formation])
    num //= formation

print(s[::-1])
