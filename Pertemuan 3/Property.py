#Properti
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

p1 = Orang("James", 22)

print(p1.nama)
print(p1.umur)

#Akses Properti 
class Mobil:
  def __init__(self, brand, merek):
    self.brand = brand
    self.merek = merek

car1 = Mobil("Toyota", "Innova")

print(car1.brand)
print(car1.merek)

#Ubah Properti
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

p1 = Orang("Ohyul", 19)
print(p1.umur)

p1.umur = 21
print(p1.umur)