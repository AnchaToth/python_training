# irjatok egy get_max nevu fv-t, aminek parameterul at lehet adni 2 lebegopontos szamot
# es adja vissza a 2 kozul a nagyobbat

def get_max(a_float: float, b_float: float) -> float:  # type hint használata a parametereknel + a return ertekre
    if a_float > b_float:
        return a_float
    else:
        return b_float


print(get_max(3.5,4.2))


# irjatk egy beszedes (konzolra kiiro) print_square fv-t
# ami parameterul kap 2 egesz szamot.
# rajzoljon ki egy ekkora teglalapot csillagokbol
def print_square(side_a, side_b):
    a = 0
    b = 0
    h = 0
    w = 0
    while a <= side_a:
        a += 1
        while b <= side_b:
            b += 1
            if a == 1 or a == side_b:
                for w in side_a:
                    print("*", end="")
            else:
                if b== 1 or b == side_a:
                    print("*",end="")
                else: print(" ", end="")


def print_square2(side_a, side_b):
    full_row = side_a*"*"
    if side_a == 1:
        frame_row = "*"
    else:
        frame_row = "*" + (side_a - 2) * " " + "*"

    # for w in range(0,side_a):
    #     full_row += "*"
    #
    # frame_row += "*"
    # for w2 in range(1,side_a-1):
    #     frame_row += " "
    # frame_row += "*"

    b=1
    while b <= side_b:
        if b == 1 or b == side_b:
            print(full_row)
        else:
            print(frame_row)
        b += 1

print_square2(1,3)

def print_squareT(width: int, height: int) -> None:
    if width <= 0 or height <= 0:
        return

    # print full row
    # if height == 1 : return


# irjatok egy fv-t ami parameterul megkapja a szava listajat
# es visszaadja ezeket osszefuzve,
# de mindegyiket gondolatjel kozott

def concat_words(words_list):
    result_string = ""
    for word in words_list:
        result_string += "-"+word+"-"
    return result_string

my_list = ["kono", "sono", "ano"]
print(concat_words(my_list))