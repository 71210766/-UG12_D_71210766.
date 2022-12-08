print("~~~~Table Matematika Nich~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
pilihan = int(input("Masukkan model matematika yang diinginkan 1/2 : "))
angka = int(input("Menampilkan table matematika dari angka : "))
for i in range(1, 10):
    sama_dengan = angka * i
    print(angka, "x", i, "=", sama_dengan)
    for i in range(3, 10):
        sama_dengan2 = angka * i 
        print(angka, "x", i, "=", sama_dengan2) 
    

