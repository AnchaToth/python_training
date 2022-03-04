# kerjunk be egy egész szamot es irjuk ki, hogy az paros vagy paratlan

number =int(input("Adj meg egy egesz szamot: "))

if number == 0:
    print("a szam 0")
elif number % 2 == 0:
    print("paros")
else:
    print("paratlan")
print("end")