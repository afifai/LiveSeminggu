class Siswa:
    jum_siswa = 0
    def __init__(self, nama_depan, nama_belakang, usia, kelas):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.email = nama_depan.lower() + '@ngodingpython.com'
        self.usia = usia
        self.kelas = kelas
        Siswa.jum_siswa += 1
    def nama_lengkap(self):
        return f'{self.nama_depan} {self.nama_belakang}'
    def ulang_tahun(self):
        print(f'Horeee, si {self.nama_depan} ulang tahun')
        self.usia += self.tambah_usia

if __name__ == '__main__':
    print("Ini dijalankan sebagai main program")

