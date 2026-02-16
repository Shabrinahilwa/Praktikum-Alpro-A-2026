#The __init__() Function
class Orang:
  def __init__(self, nama, tinggi):
    self.nama = nama
    self.tinggi = tinggi

p1 = Orang("Louis", 180)

print(p1.nama)
print(p1.tinggi)

#Without __init__() function
class Orang:
  pass

p1 = Orang()
p1.nama = "Yoshi"
p1.tinggi = 176

print(p1.nama)
print(p1.tinggi)

#
class Person:
  def __init__(self, nama, umur, tinggi, negara):
    self.nama = nama
    self.umur = umur
    self.tinggi = tinggi
    self.negara = negara

p1 = Person("Junghwan", 20, 182, "Korea Selatan")

print(p1.nama)
print(p1.umur)
print(p1.tinggi)
print(p1.negara)