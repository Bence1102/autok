def autoadatok_bekerese():
    autonev:str =str(input("Autó neve: "))
    gyartasiev:int = int(input("Gyártási dátum: "))
    return autonev, gyartasiev

def kor_kategoria(autonev, gyartasiev):
    if gyartasiev == 2024:
        print(f"Ez az {autonev} friss gyártás.")
    elif gyartasiev < 2000:
        print(f"Ez az {autonev} öreg autó.")
    else:
        print(f"Ez az {autonev} átlagos korú.")