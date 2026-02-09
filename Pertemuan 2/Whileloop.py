#While Loop
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement
  j = 0
while j < 6:
  j += 1
  if j == 3:
    continue
  print(j)