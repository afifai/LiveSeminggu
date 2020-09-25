angka=["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
hasil =" "
n = int(input("Masukkan angka (0-99) : "))

if n >= 0 and n <= 11:
    hasil = hasil + angka[n]
elif n < 20:
    hasil = angka[n%10] + " Belas "
elif n < 100:
    hasil = angka[n // 10] + " Puluh " + angka[n % 10]
else :
    print("Hanya dapat sampai 99")
print(hasil)
