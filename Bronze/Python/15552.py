import sys

count = int(input())
for i in range (count):
  num1, num2 = map(int, sys.stdin.readline().split())
  print(num1 + num2)