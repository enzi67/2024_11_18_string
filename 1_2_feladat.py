"""1.2 Feladat
Az előbbi programot módosítsd úgy, hogy újabb és újabb mondatot kérjen be a program (amig a felhasználó csak
egy ENTER-t nem üt), majd állapítsa meg, és írja ki mineden egyes alkalommal a mondat fajtáját!
"""

while True:
    vvv = input("Írj egy mondatot! ")
    if vvv == "":
        break

    if vvv [-1] == ".":
        print("Ez a mondat kijelentő.")
    elif vvv [-1] == "?":
        print("Ez a mondat kérdő.")
    elif vvv [-1] == "!":
        print("Ez a mondat felkiáltó / felszólító / óhatjtó.")
    else:
        print("Nem adtál meg mondatvégi írásjelet!")
