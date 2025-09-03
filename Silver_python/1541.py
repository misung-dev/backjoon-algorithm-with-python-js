# 잃어버린 괄호 (그리디 알고리즘)
expr = input()

groups = expr.split('-')
sums = [sum(map(int, g.split('+'))) for g in groups]
answer = sums[0] - sum(sums[1:])
print(answer)

# ex) 55-50+40+70-100
# ['55', '50+40+70', '100']
# [55, 160, 100]
# -205