# 과제 안 내신 분..?
students = []
for i in range(28):
  s = int(input())
  students.append(s)
students.sort()

for i in range(1, 31):
  if i not in students:
    print(i)