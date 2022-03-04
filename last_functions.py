# irjuk ki a szorzotablat
# h aaz eredmény <10 akkor tegyünk elé egy spacet

def print_multiplication_table():
    multiplication = 0
    for i in range(1,11):
        for j in range(1,11):
            print(i*j," ", end="")
        print("")


#print_multiplication_table()


# egy szamot irjuk át a számjegyekke 1968 --> 1, 9, 6, 8
def digits(number):
    tent = number // 10000
    number = number % 10000
    tousand = number // 1000
    number = number % 1000
    hundred = number // 100
    number = number % 100
    ten = number // 10
    number = number % 10

    print(tent, tousand, hundred, ten, number)

digits(1968)

def digits2(number):
    while number > 10:
        temp_digit = number % 10
        print(temp_digit)
        number = number // 10
    print(number)

digits2(2465)

def digits3(number):
    temp_power = 9
    result_string = ""
    while number > 10:
        if number // (10 ** temp_power) > 0:
            result_string = result_string + str(number % (10 ** temp_power)) + ", "
            number = number // (10 ** temp_power)
        temp_power -= 1

    print(result_string)

digits3(345)