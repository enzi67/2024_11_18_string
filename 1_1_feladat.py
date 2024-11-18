"""1.1 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti
milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
"""

vvv = input("Írj egy mondatot! ")

if vvv [-1] == ".":
    print("Ez a mondat kijelentő.")
elif vvv [-1] == "?":
    print("Ez a mondat kérdő.")
elif vvv [-1] == "!":
    print("Ez a mondat felkiáltó / felszólító / óhatjtó.")
else:
    print("Nem adtál meg mondatvégi írásjelet!")