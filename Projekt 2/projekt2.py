"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petra Gondek ♀
email: petra@gondek.online
discord: Petra G.#9835
"""
import random

def spocitej_cows_bulls(nahodne_cislo, zadane_cislo):
    bulls = 0
    cows = 0
    for iterace in range(len(nahodne_cislo)):
        if zadane_cislo[iterace-1] in nahodne_cislo:  # pokud je splněno, je to kráva nebo býk
            if zadane_cislo[iterace-1] == nahodne_cislo[iterace-1]:  # je to býk
                bulls += 1
            else:
                cows += 1
    return bulls, cows

def zadej_over_cislo():
    while True:
        print("-----------------------------------------------")
        print("Enter a number:")
        print("-----------------------------------------------")
        vloz_cislo = input(">>>> ")
        if vloz_cislo.isdigit():
            if int(vloz_cislo) >= 1000 and int(vloz_cislo) <= 9999: 
                if over_unikatnost(vloz_cislo):
                    return list(vloz_cislo)
                else:
                    print("All numbers must be unique!")
            else:
                print("Please, enter the number between 1000 and 9999.")
        else:
            print("Please, enter only digits!")

def over_unikatnost(list_cisel):
    if len(list_cisel) == len(set(list_cisel)):
        return True
    else:
        return False
    
def vygeneruj_cislo():
    while True:
        nahodny_cislo = random.randint(1000, 9999)
        nahodny_cislo = list(str(nahodny_cislo))
        if over_unikatnost(nahodny_cislo):
            return nahodny_cislo

def zadej_uziv_udaje():
    vloz_jmeno = input("username:")
    return vloz_jmeno

def spust_hru():
    bulls = 0
    pocet_pokusu = 0
    username = zadej_uziv_udaje()
    print(f"Hi there {username}!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    nahodne_cislo = vygeneruj_cislo()
    print(nahodne_cislo) 
    while bulls < len(nahodne_cislo):
        pocet_pokusu += 1
        zadane_cislo = zadej_over_cislo()
        bulls, cows = spocitej_cows_bulls(nahodne_cislo, zadane_cislo)
        if bulls == 1:
            bull_text = "bull"
        else:
            bull_text = "bulls"
        if cows == 1:
            cow_text = "cow"
        else:
            cow_text = "cows"
        print(f"{bulls} {bull_text}, {cows} {cow_text}")
    print("Correct, you've guessed the right number")
    print(f"in {pocet_pokusu} guesses!")
    print("-----------------------------------------------")
    print("That's ...")
    pass

spust_hru()


    