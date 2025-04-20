# N과 M (2)

def dfs(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in range(start, n+1):
    if i not in s:
      s.append(i)
      dfs(i+1)
      s.pop()

n, m = map(int, input().split())
s = []
dfs(1)

# 포인트
# 다음에 다시 풀어봐야할 듯