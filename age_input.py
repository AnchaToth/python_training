# kerd be szuletesi evet, ha <1900 vagy nagyob mint 2022, ird ki, hogy helytelen
# ellenkező esetben ird ki az eletkort

year = int(input("Add meg a szuletesi eved: "))

if 1900 > year or year > 2022:
    print("Helytelen szuletesi ev")
else:
    print("az eletkorod:", 2022-year)
print("end")