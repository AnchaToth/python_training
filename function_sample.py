# hozz letre egy is_even() nevu fuggvenyt, amely True-t ad vissza ha a parameterkent megadott ertek paros
# egyeb esetben false

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_even2(number):
    return number % 2 == 0  # boolean-t ad vissza rögtön

# sum_negativ, amely parameterul kap egy listat, es osszegzi a benne szereplo negativ szamokat, azzal ter vissza
def sum_negativ(number_list):
    sum_numbers = 0
    for number in number_list:
        if number < 0:
            sum_numbers += number
    return sum_numbers


# to_minutes fv-t, amely parameterul megkapja az orak szamat es visszadaja a perceket
def to_minutes(hours):
    minutes = hours*60
    return minutes


# input_number fv-t egy parameterrel. A fuggveny beker a felhasznalotol egy szoveget
# a parameterrel megadott szoveget szamma konvertalja és azt adja vissza
def input_number():
    input_text = input("Adj meg egy szamot! ")
    return int(input_text)


def input_number2(message):
    return int(input(message))


input_number2("Adj meg egy szamot v2!")

# irjatok egy annotate_every_even_number fv-t, amely kap egy szam listat
# a lista elemeit kiirja egymas ala, ugy, hogy minden masodik elemet egy karakterrel bentebb ir
# lehet egy boolean kapcsolóval is
def annotate_every_even_number(numbers_list):
    counter = 1
    for number in numbers_list:
        if counter % 2 == 0:
            print(" "+str(number))
        else:
            print(number)
        counter += 1


# irj egy concatenate_shorts fv-t, amely parameterul kap egy listat szavakkal
# es osszefuzi a 3 karakternel rovidebb szavakat egy stringbe, es ezt adja vissza
def concatenate_shorts(text_list):
    return_text = ""
    for text in text_list:
        if len(text) <= 2:
            return_text = return_text + text + ","
            # return_text += text
    return return_text


print(is_even(7))

numbers = [2,4,5,-2,-4,3,-1]

print(sum_negativ(numbers))
print(to_minutes(4))
print(input_number())

annotate_every_even_number(numbers)

words = ["alma", "korte", "be", "ki", "le", "fel", "hova"]

print(concatenate_shorts(words))