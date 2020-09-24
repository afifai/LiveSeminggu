angka = input("Masukkan sebuah angka : ")
angka = eval(angka)
if angka > 0:
    print('Angka {} adalah bilangan positif'.format(angka))
    if angka > 50:
        print("Angka ini besar")
    else:
        print("Angka ini kecil")
elif angka == 0:
    print('Angka {} adalah bilangan nol'.format(angka))
else:
    print('Angka {} adalah bilangan negatif'.format(angka))
print("program selesai")
