hours, minutes = map(int, input().split())

if minutes >= 45:
  minutes -= 45

else:
  if hours >= 1:
    hours -= 1
  else:
    hours += 23
  minutes += 15

print (hours, minutes)