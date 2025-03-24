#알고리즘 수업 - 점근적 표기 1
a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

# f(n)을 x로, g(n)을 y로 가정
x = (a1 * n) + a0
y = c * n

if (x <= y) and (a1 <= c):
  print(1);
else:
  print(0)

