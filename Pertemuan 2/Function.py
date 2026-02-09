#Creating a Function
def my_function():
  print("Hello from a function")

#Calling a Function
def my_function():
  print("Hello from a function")

my_function()

#Calling a Function Multiple Times
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#Why Use Functions?
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#Return Values
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#Returned Value Directly
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

#Default Parameter Values
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

#Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

#Passing Different Data Types
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Return Values
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Returning Different Data Types
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("Jeongwoo")

#Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Sean")

#Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)