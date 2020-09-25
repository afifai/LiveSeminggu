from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-n", "--nama", required=True, help="Nama Anda")
ap.add_argument("-u", '--umur', default=17)
ap.add_argument("-p", '--pilihan', default=1, type=int)
args = vars(ap.parse_args())

def tes_1():
    print("f1")
def tes_2():
    print("f2")

nama = args['nama']
umur = args['umur']
print(f'nama anda {nama}')
print(f'umur anda {umur}')
if args['pilihan'] == 1:
    tes_1()
elif args['pilihan'] == 2:
    tes_2()
