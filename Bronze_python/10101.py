# 삼각형 외우기

num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 + num2 + num3 != 180):
    print('Error')
elif (num1 == num2 == num3):
    print('Equilateral')
elif (num1 == num2 or num2 == num3 or num3 == num1) :
    print('Isosceles')
else:
    print('Scalene')
