# 창문 닫기

import sys
input = sys.stdin.readline

n = int(input())

print(int(n**0.5))

# windows = [1] * n

# # 차례로 문열고 닫기
# for i in range(2, n+1):
#   for j in range(i-1, n, i):
#     if windows[j] == 0:
#       windows[j] = 1 
#     else:
#       windows[j] = 0

# # 결과 출력 (열려 있는 창문 갯수)
# target = 1
# result = windows.count(target)
# print(result)