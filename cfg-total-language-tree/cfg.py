def kelimeleri_uret(cfg, baslangic_sembolu, alfabe):
    kelimeler = []
    stack = [(baslangic_sembolu, '')]

    while stack:
        mevcut, mevcut_kelime = stack.pop()

        if mevcut == '':
            kelimeler.append(mevcut_kelime)
        else:
            if mevcut[0] in alfabe:
                stack.append((mevcut[1:], mevcut_kelime + mevcut[0]))
            elif mevcut[0] in cfg:
                genislemeler = cfg[mevcut[0]]
                for genisleme in genislemeler:
                    yeni_stack_elemani = (genisleme + mevcut[1:], mevcut_kelime)
                    stack.append(yeni_stack_elemani)

    return kelimeler


def tekrarlanan_kelimeleri_bul(kelimeler):
    tekrarlanan_kelimeler = set()
    benzersiz_kelimeler = set()

    for kelime in kelimeler:
        if kelime in benzersiz_kelimeler:
            tekrarlanan_kelimeler.add(kelime)
        else:
            benzersiz_kelimeler.add(kelime)

    return tekrarlanan_kelimeler


def main():
    alfabe = set(input("Alfabeyi giriniz Σ=(örneğin, a b): ").split())

    cfg = {}
    cfg_str = input("CFG'yi girin (örneğin, S->aa|bX|aXX, X->ab|b): ")
    uretimler = cfg_str.split(', ')
    for uretim in uretimler:
        non_terminal, genisleme = uretim.split('->')
        cfg[non_terminal] = genisleme.split('|')

    baslangic_sembolu = input("Başlangıç sembolünü girin: ")

    kelimeler = kelimeleri_uret(cfg, baslangic_sembolu, alfabe)
    tekrarlanan_kelimeler = tekrarlanan_kelimeleri_bul(kelimeler)

    print(f"Üretilen Kelimeler: {', '.join(kelimeler)}")
    print(f"Tekrarlanan Kelimeler: {', '.join(tekrarlanan_kelimeler)}")


if __name__ == "__main__":
    main()
