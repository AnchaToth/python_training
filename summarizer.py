# kerd be a felhasznalotol, hogy hany szamot szeretne megadni.
# kerj be tole pontosan annyi szamot, amit megadott
# osszegezzuk a felhasznalo altal megadott, csak pozitiv szamokat

number = int(input("Add meg hany darab szammal szeretnel dolgozni: "))
value = 0
sum_values = 0
counter = 1

while counter <= number:
    value = int(input("Add meg a "+str(counter)+". egy szamot: "))
    if value % 2 == 0:
        sum_values += value
    counter += 1
print("paros szamok osszege: ", sum_values)
