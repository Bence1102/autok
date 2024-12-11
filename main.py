import feladat1
import feladat2
import feladat3

autonev, gyartasiev = feladat1.autoadatok_bekerese()
feladat1.kor_kategoria(autonev, gyartasiev)






szamok = feladat2.lottoszamok()
egyjegyuek = feladat2.egyjegyuek_szama(szamok)
feladat2.konzol_kiir(szamok, egyjegyuek)
feladat2.file_kiir(egyjegyuek)


autok = feladat3.beolvas("auto.txt")
print("III/Flotta:")
print(f"Autók száma: {feladat3.flotta(autok)}.")

legfiatalabb_auto = feladat3.legfiatalabb(autok)
print("III/Legfiatalabb:")
print(f"A legfiatalabb autó: {legfiatalabb_auto.nev} ({legfiatalabb_auto.gyartasi_ev}).")

atlag_kor = feladat3.atlagos_kor(autok)
print("III/Átlag kor:")
print(f"Az autók átlagos kora: {atlag_kor:.2f} év.")