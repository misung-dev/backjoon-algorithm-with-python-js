alpha_list = list(input())
for i in range(len(alpha_list)):
    times = sum(list(map(int, list(str(ord(alpha_list[i]))))))
    print(alpha_list[i] * times)

# 테스트 케이스
# smupc

# sssssss
# mmmmmmmmmm
# uuuuuuuuu
# pppp
# cccccccccccccccccc