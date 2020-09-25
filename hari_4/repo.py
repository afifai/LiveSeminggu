class Barang:
    diskon = 0.2
    def __init__(self, jenis, merek, tipe,harga, stok):
        self.jenis = jenis
        self.merek = merek
        self.tipe = tipe
        self.harga = harga
        self.stok = stok
    def diskon_barang(self):
        self.harga = self.harga - (self.harga * self.diskon)
    def beli(self, pcs):
        if self.stok < pcs:
            print("Barang kurang")
        else:
            self.stok -= pcs
            print(f'Harga : {self.harga * pcs}')
