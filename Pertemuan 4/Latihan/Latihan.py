#Soal No.1
angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

#Output:
#Masukkan index (0-2): A
#Harus berupa angka bulat!
#Selesai.

#Soal No.2
try:
    num1 = float(input("Masukkan Angka ke-1: "))
    num2 = float(input("Masukkan Angka ke-2: "))

    print(f"Hasil: {num1/num2}")
except ValueError:
    print("Harus berupa angka")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")



