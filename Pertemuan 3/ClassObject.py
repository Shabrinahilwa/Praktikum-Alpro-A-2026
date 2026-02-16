#Class/Object
# 1. Creat a Class
class MyClass:
  x = 28

print(MyClass)

# 2. Creat a Object
class MyClass:
  x = 13

kelas = MyClass()
print(kelas.x)

#Remove Object
"""
class Person:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def myfunc(self):
    print("Haloo ini " + self.nama)

p1 = Person("Jeongwoo", 21)

del p1

print(p1)
"""

#Multiple Object
class MyClass:
  x = 15

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
