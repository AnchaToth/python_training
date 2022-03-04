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