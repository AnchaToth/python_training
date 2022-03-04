# irj egy fv-t (is_ascending), amley parameterul kap 3 egesz szamot
# True-t ad vissza  ha a szamok, szigoruan novekvo sorrendben vannak
# ellenekzo esetben False

def is_ascending(num_a, num_b, num_c):
    if num_a == num_b or num_a == num_c or num_b == num_c:
        return False
    if num_a < num_b and num_b < num_c:
        return True
    return False

# print(is_ascending(1,3,6))
# print(is_ascending(1,10,20))
# print(is_ascending(1,1,1))
# print(is_ascending(20,10,1))
# print(is_ascending(20,10,20))

# irj egy word_concat fv-t amely ket szot kap parameterkent
# es visszaadja oket osszefuzve ugy, hogy a rovidebb legyen elol

def word_concat(word_a, word_b):
    if len(word_a) > len(word_b):
        return word_b+word_a
    else:
        return word_a+word_b

# print(word_concat("alma","korte"))
# print(word_concat("cseresznye","meggy"))