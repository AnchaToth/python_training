print("alma" == "korte")

print("alma" == "alma")

while False: #sose fut le
    print("Hello ciklus")

#while True: #végtelen ciklus
#    print("Hello vegtelen")

count = 0
while count < 10:
    print("Hello",count)
    count=count+1

print("End!")

#Feladat: addig kerjen be szamot amig 0-t nem kap. Irja ki a kapott szam ketszereset
num =int(input("Adj meg egy szamot: "))

while num!=0:
    print(num*2)
    num=int(input("Adj meg egy szamot: "))
print("End")
