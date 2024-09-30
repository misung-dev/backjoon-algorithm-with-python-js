# 인간-컴퓨터 상호작용

# 50점짜리 풀이 (부분 성공)
word = str(input())
q = int(input())

for i in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)

    arr = ''
    arr = word[l:r+1]
    
    print(arr.count(a))


# find() 함수는 파이썬에서 특정 문자열의 위치, 인덱스 번호를 찾고자 할 때 사용.

# word.slice[l:r+1]는 잘못된 사용법! 
# 문자열 슬라이싱은 대괄호([])를 사용해서 word[l:r+1]처럼 해야 한다.
# slice는 메서드가 아니고, 슬라이싱을 위한 기본 문법이다.