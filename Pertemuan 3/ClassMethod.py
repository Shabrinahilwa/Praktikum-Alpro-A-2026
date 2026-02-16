#Class Method
class Orang:
  def __init__(self, nama):
    self.nama = nama

  def greet(self):
    print("Haloo ini " + self.nama)

p1 = Orang("Woojin")
p1.greet()

 #Class Method dengan Parameter
class KalKulator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

kalku = KalKulator()
print(kalku.add(5, 9))
print(kalku.multiply(10, 6))

#Metode Mengakses Properti
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def get_info(self):
    return f"Namanya {self.nama}, umurnya {self.umur} tahun."

p1 = Orang("Jihoon", 26)
print(p1.get_info())

class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def ucapan(self):
    self.umur += 1
    print(f"Happy birthday! umur mu sekarang {self.umur}")

p1 = Orang("Sarah", 18)
p1.ucapan()
p1.ucapan()

#Method __str__()
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def __str__(self):
    return f"{self.nama} ({self.umur})"

p1 = Orang("Junghwan", 22)
print(p1)

#Berbagai Metode dalam Satu Kelas
class Playlist:
  def __init__(self, nama):
    self.nama = nama
    self.lagu = []

  def add_song(self, lagu):
    self.lagu.append(lagu)
    print(f"Tambah lagu: {lagu}")

  def remove_song(self, lagu):
    if lagu in self.lagu:
      self.lagu.remove(lagu)
      print(f"Removed: {lagu}")

  def show_songs(self):
    print(f"Playlist '{self.nama}':")
    for lagu in self.lagu:
      print(f"- {lagu}")

my_playlist = Playlist("Lagu Favorit")
my_playlist.add_song("Boyfriend - Justin Bieber")
my_playlist.add_song("Adrenaline - Ateez")
my_playlist.add_song("Nothin' On You - B.o.B")
my_playlist.show_songs()