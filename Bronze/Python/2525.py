hours, minutes = map(int, input().split())
time = int(input())

# 기존 시간과 분에 더하기
hours += time // 60
minutes += time % 60 

# 60분을 초과하면 시간을 증가시키고 분을 조정
if minutes >= 60:
    hours += minutes // 60
    minutes = minutes % 60

# 24시간을 초과하면 24시간 단위로 환산
if hours >= 24:
    hours = hours % 24

print(hours, minutes)
