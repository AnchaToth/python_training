# fuggveny definicioja
def print_employee_data(name, age):  # paraméter nevek
    """Ez a fuggveny kiirja az alkalmazott nevet es korat"""

    print("Az alkalmazott neve:", name)
    print("Az alkalmazott eletkora:", age)


def print_dof_name(name):
    print("A kutya neve:", name)


def print_sum(a, b):
    print(str(a)+" es " + str(b) + " osszege: " + str(a+b))


def sum_list(numbers_list):
    sum_numbers = 0
    for number in numbers_list:
        sum_numbers += number
    print("A listaban szereplo szamok osszege:", sum_numbers)


print_employee_data("John", 30)  # függvény hívás paraméter értékekkel
print_employee_data("Jack", 10)
print_employee_data("Jane", 20)
print_dof_name("Buksi")
print_sum(12,27)

numbers = [1,2,3,4,5,6,7,8,9]
sum_list(numbers)

number_a = int(input("Add meg az osszeadas elso szamat: "))
number_b = int(input("Add meg az osszeadas masodik szamat: "))

print_sum(number_a,number_b)

print("End")