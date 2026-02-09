#Python Conditions and If statements
a = 33
b = 200
if b > a:
  print("b lebih besar dari a")

angka = 8

if angka > 0:
  print("Angka positif")

#Multiple Statements in If Block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Elif Statement
a = 33
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a sama dengan b")

#Multiple Elif Statements
score = 75

if score >= 90:
  print("Nilai: A")
elif score >= 80:
  print("Nilai: B")
elif score >= 70:
  print("Nilai: C")
elif score >= 60:
  print("Nilai: D")

#How Elif Works
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#When to Use Elif
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#Else Statement
a = 200
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b sama")
else:
  print("a lebih besar dari b")

#Else Without Elif
a = 200
b = 33
if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

#How Else Works
bilangan = 7

if bilangan % 2 == 0:
  print("Bilangan adalah genap")
else:
  print("Bilangan adalah ganjil")

#Complete If-Elif-Else Chain
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#Else as Fallback
username = "Ohyul"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#Short Hand If
a = 5
b = 2
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#Assign a Value With If ... Else
a = 30
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Nested If Statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("Kamu bisa mengemudi")
  else:
    print("Kamu butuh SIM untuk mengemudi")
else:
  print("Kamu terlalu muda untuk mengemudi")

#Nested If vs Logical Operators
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!") 

score = 92
extra_credit = 5

#More Examples of Nested If Statements
if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")