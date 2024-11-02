# 퇴사 (삼성 SW 역량 테스트 기출 문제)

rest = int(input())
schedules = []

# 일정 입력 받기
for _ in range(rest):
  t, p = map(int, input().split())
  schedules.append([t,p])

# 각 날짜별 최대 수익을 기록할 dp 배열 생성
dp = [0] * (rest+1)

# 역순으로 최대 수익 계산
for i in range(rest - 1, -1, -1):
    t, p = schedules[i]
    if i + t <= rest:  # 해당 일정이 기간 내에 완료될 수 있는 경우
        dp[i] = max(p + dp[i + t], dp[i + 1])  # 일정 참여 vs 불참 중 최대값 선택
    else:
        dp[i] = dp[i + 1]  # 일정이 불가능한 경우, 다음 날의 수익 가져옴

# 첫날의 최대 수익이 전체 최대 수익
total_pay = dp[0]
print(total_pay)