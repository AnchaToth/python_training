print("Gondolj egy szamra 1 es 10 kozott!")
answer = ""
lowest_possible = 1
highest_possible = 10

while answer != "e":
    guess = (highest_possible + lowest_possible) // 2
    answer = input("Ennel a szamnal kissebb (k) nagyobb (n) vagy egyenlo (e)? "+str(guess)+" ")
    if answer == "k":
        highest_possible = guess-1
    elif answer == "n":
        lowest_possible = guess+1

print("A gondolt szam:", guess)
