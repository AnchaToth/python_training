name = "John Doe"

print(name.upper())
print(name.lower())

print(name[0])

for ch in name:
    print(ch)

print(len(name))

print(name[2:5])
print(name[:6])
print(name[:6:2])  # 2 karakterenként
print(name[::-1])  # visszafele

print(name[:-1])
print(name[:len(name)-1])

filename = "doom.exe"
print(filename[-3:])

print("a" in "alma")
print("b" in "alma")

## irj egy olyan fv-t amley megszamolja, hogy hany db á betű van egy szóban

def count_a(word: str):
    counter = 0
    for w in word:
        if w == "a":
            counter += 1
    return counter


## irj egy olyan fuggvenyt amley parameterul kape egy szot es megszamolja a maganhangzokat

def count_vowels(word: str):
    vowels = "aeuoi"
    counter = 0

    for w in word:
        if w in vowels:
            counter +=1

    return counter

# irj egy fv-t amely kap egy szot és visszaadja a benne szereplő karaktereket *-gal elválasztva
# az utolso karakter után ne legyen *
def sever_word(word: str):
    severed_word = ""
    for w in word:
        severed_word += w +"*"
    return severed_word[:-1]

# isszaadja, hogy a parameternek kapott szo visszafele ugyan az-e
def is_palindrom(word: str):
    return word == word[::-1]

# irj egy fv-t. ami a par
# # irj egy fv-t amely vameterkent kapott szobol kiveszi a space-ket és azt adja vissza
def delete_space(word: str):
    return_string = ""
    for w in word:
        if w != " ":
            return_string += w
    return return_string

print(delete_space(" csak hogy irjak valamit "))
print(is_palindrom("anna"))
print(is_palindrom("barmi"))
print(count_a("barmi"))
print(count_a("elemer"))
print(count_vowels("ebben"))
print(sever_word("eztszeddszet"))