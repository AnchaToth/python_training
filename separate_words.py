# fv: egy paraméterül akpott szavak listáját,
# összefűzi vesszővel elválasztva és ezzel tér vissza
# de az utolsó elem után, ne legyen vessző
# be lehet vezetni egy is_first boolean-t, hogy az első után, a szavak elé tegyünk vesszőt

def concat_words(words_list):
    result_text = ""
    counter = 1
    for word in words_list:
        if counter < len(words_list):
            result_text += word + ", "
        else:
            result_text += word
        counter +=1
    return result_text

words = ["valami", "akarmi", "barmi", "kono", "sono", "ano"]
print(concat_words(words))