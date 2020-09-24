tambah = 'y'
pesanan = []
while tambah != 'n':
    if tambah == 'y':
        pesan = input("Mau makan apa ? ")
        pesanan.append(pesan)
    else:
        print("Perintah tidak ditemukan")
    tambah = input("Ada lagi ? (y/n) ")
    tambah = tambah.lower()
jum = len(pesanan)
print(f'Anda memesan {jum} item')
for item in pesanan:
    print(f'Anda Memesan {item}')
