class Moore:
    def __init__(self, durumlar, girdi_alfabe, cikti_alfabe, gecis_tablosu, cikti_tablosu):
        self.durumlar = durumlar
        self.girdi_alfabe = girdi_alfabe
        self.cikti_alfabe = cikti_alfabe
        self.gecis_tablosu = gecis_tablosu
        self.cikti_tablosu = cikti_tablosu
        self.mevcut_durum = durumlar[0]

    def input_isle(self, input_dizisi):
        cikti_dizisi = ""
        for sembol in input_dizisi:
            if sembol not in self.girdi_alfabe:
                raise ValueError(f"Geçersiz girdi sembolü: {sembol}")

            mevcut_girdi_index = self.girdi_alfabe.index(sembol)
            sonraki_durum = self.gecis_tablosu[self.mevcut_durum][mevcut_girdi_index]
            cikti_sembol = self.cikti_tablosu[self.mevcut_durum]

            cikti_dizisi += cikti_sembol
            self.mevcut_durum = sonraki_durum

        return cikti_dizisi

def main():

    durumlar = input("Sonlu durumlar kümesini girin (virgülle ayrılmış): ").split(',')
    girdi_alfabe = input("Girdi sembollerini girin (virgülle ayrılmış): ").split(',')
    cikti_alfabe = input("Çıktı sembollerini girin (virgülle ayrılmış): ").split(',')


    gecis_tablosu = {}
    for durum in durumlar:
        gecisler = input(f"{durum} durumu için geçişleri girin : ").split(',')
        gecis_tablosu[durum] = gecisler


    cikti_tablosu = {}
    for durum in durumlar:
        cikti_sembol = input(f"{durum} durumu için çıktı sembolünü girin ({','.join(cikti_alfabe)}): ")
        cikti_tablosu[durum] = cikti_sembol


    moore_makinesi = Moore(durumlar, girdi_alfabe, cikti_alfabe, gecis_tablosu, cikti_tablosu)


    input_string = input("Giriş stringini girin: ")

    try:
        output_string = moore_makinesi.input_isle(input_string)
        print(f"Çıkış stringi: {output_string}")
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
