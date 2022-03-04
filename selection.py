if 5-4<0:
    print("0-nal kissebb szam")
print("End")

name = input("Add meg a neved: ")
print(len(name))

if len(name) == 0:
    print("Nem jó, nem adtál meg nevet!")
print("end if1")

if name == "":
    print("Nem jó, adj meg egy nevet!")
print("End if2")

age = int(input("Add meg a korod: "))
if age <20:
    print("túl fiatal vagy")
print("end if-age")