class Rumah:
    def __init__(self, ukuran, warna, banyak_kamar):
        self.ukuran = ukuran
        self.warna = warna
        self.banyak_kamar = banyak_kamar
    
    def sale(self):
        print("Rumah ini dijual dengan deskripsi berikut:" + self.ukuran, self.warna, self.banyak_kamar)
    def sewa(self):
        print("Rumah ini disewakan dengan deskripsi berikut:" + self.ukuran, self.warna, self.banyak_kamar)

p1= Rumah("besar", "merah", 4)
p2= Rumah("kecil", "biru", 2)
p3= Rumah("sedang", "hijau", 3)

print(p1.ukuran)
print(p1.warna) 
print(p1.banyak_kamar)