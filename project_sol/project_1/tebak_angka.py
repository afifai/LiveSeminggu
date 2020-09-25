from random import randint
print('*'*50)
print("PERMAINAN TEBAK ANGKA")
print('*'*50)
print()
# inisiasi
angka = randint(1,20)
score = 100
ulang = True

print("Saya memikirkan sebuah angka dari 1 - 20")
print("Silahkan tebak Angka yang Saya pikirkan")
print("Input HARUS BERUPA ANGKA")
print()
while ulang:
    print(f'Score Anda saat ini {score}')
    if score > 0:
        tebak = input("Masukkan tebakkan Anda : ")
        if tebak.isnumeric():
            tebak = eval(tebak)
            if tebak > angka:
                score -= 10
                print("Tebakkan Anda terlalu besar, score Anda dikurangi 10")
            elif tebak < angka:
                score -= 10
                print("Tebakkan Anda terlalu kecil, score Anda dikurangi 10")
            else:
                print("Selamat !, Tebakkan Anda benar")
                print(f'Score Anda {score}')
                ulang = False
            print()
        else:
            score -= 20
            print("[WARNING] Tebakkan harus berupa angka")
            print("Penalty!, Score Anda dikurangi 20")
        print()
    else:
        print("GAME OVER")
        print(f'Score Anda {score}')
        ulang = False
