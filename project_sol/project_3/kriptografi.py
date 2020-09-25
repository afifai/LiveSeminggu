print("Pilih Mode : 1) Enkripsi 2) Dekripsi")
mode = input(">>> ")
inp = input("Masukkan pesan rahasia : ")
kode = input("Masukkan kode rahasia : ")

if kode.isdecimal():
    if mode.isdecimal() and mode in ['1', '2']:
        kode = int(kode)
        kode = (kode * -1) if mode == '2' else kode
        out = ''
        for c in inp:
            if c.isupper():
                out += chr((ord(c) + kode - 65) % 26 + 65)
            elif c.islower():
                out += chr((ord(c) + kode - 97) % 26 + 97)
            else:
                out += c
        print(f"HASIL : {out}")
    else:
        print("Mode tidak ada")
else:
    print("Kode bukan Angka")
