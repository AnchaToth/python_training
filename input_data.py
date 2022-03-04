#Kerjuk be a felhasznalo nevet. ha ures, akkor irjuk ki, hogy nem lehet ures és kerjuk ujra.
#Ha nem ures, irjuk ki, hogy koszonom

name = ""
while len(name) == 0:
    name = input("Add meg a neved: ")
    if name == "":
        print("A nevet nem lehet uresen hagyni!")

print("Koszonom!")
