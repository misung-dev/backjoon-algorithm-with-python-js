# 숫자 카드 2

n = int(input())
card_list = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

# card_list의 숫자별 등장 횟수를 저장하는 딕셔너리 생성
card_count = {}

for card in card_list:
  if card in card_count:
    card_count[card] += 1
  else:
    card_count[card] = 1

# 등장 횟수를 출력 리스트에 저장
result = []
for num in check_list:
  result.append(card_count.get(num, 0)) # 존재하지 않으면 0을 반환

print(' '.join(map(str, result)))