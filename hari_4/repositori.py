class Barang:
    rate_diskon = 0.2
    def __init__(self, jenis, merek, tipe, harga, stok):
        self.jenis = jenis
        self.merek = merek
        self.tipe = tipe
        self.harga = harga
        self.stok = stok
    def diskon(self):
        print(f"Harga Awal : {self.harga}")
        self.harga -= (self.harga * self.rate_diskon)
        print(f"Harga Setelah Diskon : {self.harga}")
    def beli(self, pcs):
        if self.stok < pcs:
            print("Barang Kurang")
        else:
            self.stok -= pcs
            print(f'Harga : {self.harga * pcs}')
