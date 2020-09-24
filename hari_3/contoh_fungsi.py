def sapa(nama,umur=17):
    print(f"Halo {nama}")
    print(f"umur anda {umur} tahun")
    print("Apa kabar ?")
    print("Dirumah aja ya")


nama_1 = input("Masukkan nama Anda : ")
umur_1 = input("Usia anda : ")
sapa(nama=nama_1, umur=umur_1)

nama_2 = input("Masukkan nama Anda : ")
umur_2 = input("Usia anda : ")
sapa(umur=umur_2, nama=nama_2)

nama_3 = input("Masukkan nama Anda : ")
umur_3 = input("Usia anda : ")
sapa(nama_3, umur_3)

nama_4 = input("Masukkan nama Anda : ")
sapa(nama_4)
