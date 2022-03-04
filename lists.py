names = []

names.append("John Doe")
names.append("Jack Doe")
names.append("Jane Doe")

print(names)

print(names[0:2])
print(names[::-1])

names[1] = "Jack Smith"
print(names)

names.remove("Jack Smith")
print(names)

numbers = [1,2,3]

employee = ["John Doe", 20]

print(len(numbers))
print("John Doe" in names)  # boolean-nel tér vissza

## irj egy fv-t ami parameterul kap egy listat, amiben nevek vannak es visszaad egy masik listat
## a masik listaban csak azok a nevek legyenek benne amik John-nal kezdodnek
def pick_johns(names_list):
    johns_list = []
    for name in names_list:
        # if "John" in name:
        #      if name.index("John") == 0:
        #         johns_list.append(name)
        if "John" in name and name.index("John") == 0:
            johns_list.append(name)
    return johns_list

names_list = ["John Doe", "Jack Doe", "John Smith", "Jane John"]
print(pick_johns(names_list))