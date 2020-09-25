from prettytable import PrettyTable

tbl = PrettyTable()
tbl.field_names = ['Makanan / Minuman', 'Harga']

f = open('menu.txt', 'r')

for s in f:
    list_konten = s.split('#')
    angka = int(list_konten[1])
    angka = 'Rp {:20,.2f}'.format(angka)
    lst_br = list_konten[0]
    tbl.add_row([lst_br, angka])
f.close()


print(tbl)
