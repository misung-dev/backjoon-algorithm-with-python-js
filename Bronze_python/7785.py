# 회사에 있는 사람

import sys
input = sys.stdin.readline

num = int(input())
company = {}

for i in range(num):
    man, state = map(str, input().split())
    if state == 'enter':
      company[man] = True
    else:
      del company[man]

print('\n'.join(sorted(company.keys(), reverse = True)))

# 딕셔너리 구조는 해시맵을 통해 key-value값으로 저장되며, 추가 삭제 연산이 빠름