"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petra Gondek
email: petra@gondek.online
discord: Petra G.#9835
"""
import random

def zadej_over_cislo():
    while True:
        vloz_cislo = input("Enter a number:")
        if vloz_cislo.isdigit():
            if int(vloz_cislo) >= 1000 and int(vloz_cislo) <= 9999: 
                return vloz_cislo
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
    username = zadej_uziv_udaje()
    print(f"Hi there {username}!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    nahodne_cislo = vygeneruj_cislo()
    print(nahodne_cislo)
    zadane_cislo = zadej_over_cislo()
    print(zadane_cislo)

    pass

spust_hru()


    