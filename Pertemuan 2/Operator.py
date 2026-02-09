# Python Operators
print(20 + 28)

# Arithmetic Operators
x = 12
y = 5

sum1 = 250 + 60      #250 + 60 = 310
sum2 = sum1 + 76     #310 + 76 = 386
sum3 = sum2 + sum2   #386 + 386 = 772

print(sum1)
print(sum2)
print(sum3)

x = 15
y = 4

print(x + y) #Addition (+) : menjumlahkan dua nilai 
print(x - y) #Subtraction (-) : mengurangkan dua nilai 
print(x * y) #Multiplication (*) : mengalikan dua nilai 
print(x / y) #Division (/) : membagi dua nilai 
print(x % y) #Modulus (%) : menghitung sisa pembagian
print(x ** y) #Exponentiation (**) : pemangkatan 
print(x // y) #Floor Division (//) : membagi dan dibulatkan ke bawah


#Assignment Operators
# Operator =
x = 5
print(x)
# Operator +=
x = 5
x += 3
print(x)
# Operator -=
x = 5
x -= 3
print(x)
# Operator *=
x = 5
x *= 3
print(x)
# Operator /=
x = 5
x /= 3
print(x)
# Operator %=
x = 5
x %= 3
print(x)
# Operator //=
x = 5
x //= 3
print(x)
# Operator **=
x = 5
x **= 3
print(x)

#Operator :=
print(x // y)

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))

#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)


#Bitwise Operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

#Operator Precedence
print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)