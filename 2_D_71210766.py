print("~~~~Table Matematika Nich~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
pilihan = int(input("Masukkan model matematika yang diinginkan 1/2 : "))
angka = int(input("Menampilkan table matematika dari angka : "))
if pilihan == 1 :
    for i in range(1, 10):
        sama_dengan = angka * i
        print(angka, "x", i, "=", sama_dengan)
    for i in range(3, 10):
        sama_dengan2 = angka * i 
        print(angka, "x", i, "=", sama_dengan2) 
elif pilihan == 2:
    for i in range(50, 66):
        sama_dengan = i / angka
        print(i, ":", angka, "=", sama_dengan)
else :
    print("Pilihan tidak tersedia, jangan ngasal!")



