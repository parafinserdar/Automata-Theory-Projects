def Mealey(durum_sayisi, giris_alfabe, cikis_alfabe, gecisler, giris_dizisi):
    # Başlangıç durumu
    suanki_durum = 0


    gecis_dict = {}
    for gecis in gecisler:
        suanki, giris_sembol, sonraki_durum, cikis_sembol = gecis.split('/')
        gecis_dict[(int(suanki), giris_sembol)] = (int(sonraki_durum), cikis_sembol)


    for sembol in giris_dizisi:
        if sembol not in giris_alfabe:
            print(f"Hatalı giriş sembolü: {sembol}")
            return


        suanki_durum, cikis_sembol = gecis_dict.get((suanki_durum, sembol), (None, None))


        print(f"Durum: q{suanki_durum}, Giriş: {sembol}, Çıkış: {cikis_sembol}")

    print(f"\nNihai Durum: q{suanki_durum}")

if __name__ == "__main__":

    durum_sayisi = int(input("Durum Sayısı: "))
    giris_alfabe = input("Giriş Sembol Kümesi (virgülle ayırın): ").split(',')
    cikis_alfabe = input("Çıkış Sembol Kümesi (virgülle ayırın): ").split(',')


    gecisler = []
    while True:
        gecis = input("Geçiş (çıkmak için q): ")
        if gecis.lower() == 'q':
            break
        gecisler.append(gecis)


    giris_dizisi = input("Giriş Dizisi: ")


    Mealey(durum_sayisi, giris_alfabe, cikis_alfabe, gecisler, giris_dizisi)
