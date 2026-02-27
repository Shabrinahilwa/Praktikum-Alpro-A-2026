class ValidasiNama(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"Nama terlalu pendek! Minimal 3 karakter.")

class ValidasiUmur(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f"Umur tidak memenuhi syarat (17-60 tahun).")

class ValidasiEmail(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f"Email tidak valid! Harus mengandung '@'.")

class ValidasiNoHP(Exception):
    def __init__(self, nohp):
        self.nohp = nohp
        super().__init__(f"No HP tidak valid! Harus 10-13 digit angka.")


def periksa_nama(nama):
    if len(nama) < 3:
        raise ValidasiNama(nama)
    return True

def periksa_umur(umur):
    if umur < 17 or umur > 60:
        raise ValidasiUmur(umur)
    return True

def periksa_email(email):
    if '@' in email:
        pass
    else:
        raise ValidasiEmail(email)
    return True

def periksa_no_hp(nohp):
    if 10 <= len(nohp) <= 13:
        pass
    else:
        raise ValidasiNoHP(nohp)
    return True

print("\n==== REGRISTASI PESERTA SEMINAR ====")

while True:
    try:
        nama = input ("Nama Lengkap: ")
        periksaNama = periksa_nama(nama)
    except ValidasiNama as e:
        print(f"[ERROR] {e}")
    else:
        break
    
while True:
    try:
        umur = int(input("Umur: "))
        periksaumur = periksa_umur(umur)
    except ValueError:
        print("Masukkan bilangan bulat!")
    except ValidasiUmur as e:
        print(f"[ERROR] {e}")
    else:
        break

while True:
    try:
        email = input ("Email: ")
        periksaEmail = periksa_email(email)
    except ValidasiEmail as e:
        print(f"[ERROR] {e}")
    else:
        break

while True:
    try:
        nomorHp= input ("No HP: ")
        periksaNoHp = periksa_no_hp(nomorHp)
    except ValidasiNoHP as e:
        print(f"[ERROR] {e}")
    else:
        break

print("\n=== DATA PESERTA ===")
print("Nama     : ", nama)
print("Umur     : ", umur)
print("Email    : ", email)
print("Nomor HP : ", nomorHp)
print("Status   :  TERDAFTAR")
