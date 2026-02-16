#Self Parameter
class Orang:
  def __init__(self, nama, tinggi):
    self.nama = nama
    self.tinggi = tinggi

  def greet(self):
    print("Hello, nama saya " + self.nama)

p1 = Orang("Haruto", 184)
p1.greet()

#Kenapa Menggunakan Self?
class Buah:
  def __init__(self, nama):
    self.nama = nama

  def printname(self):
    print(self.nama)

p1 = Buah("Mangga")
p2 = Buah("Durian")

p1.printname()
p2.printname()

#The self Parameter is not a Keyword
class Mobil:
  def __init__(myobject, merk, tahun):
    myobject.merk = merk
    myobject.tahun = tahun

  def greet(abc):
    print("Mobil " + abc.merk)

p1 = Mobil("Toyota", 2020)
p1.greet()

#Mengkses Properti dengan self
class Motor:
  def __init__(self, merek, model, tahun):
    self.merek = merek
    self.model = model
    self.tahun = tahun

  def display_info(self):
    print(f"{self.tahun} {self.merek} {self.model}")

motor1 = Motor("Honda", "Vario", 2025)
motor1.display_info()

#Memanggil Metode dengan self
class Orang:
  def __init__(self, nama):
    self.nama = nama

  def greet(self):
    return "Hello, " + self.nama

  def welcome(self):
    message = self.greet()
    print(message + "! Selamat datang di situs kami.")

p1 = Orang("Sean")
p1.welcome()