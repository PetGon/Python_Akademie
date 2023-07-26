"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petra Gondek
email: petra@gondek.online
discord: Petra G.#9835
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
uzivatele = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
 
def analyza(text):
    pocet_slov = len(text)
    velke_pismeno = 0
    for slovo in text:
        if slovo[0].upper():    # pokud první písmeno slova je velké
            velke_pismeno += 1  # inkrementuji o jedna (int) 
        print(slovo)
    return pocet_slov

def preved_text(text):
    text = text.replace(".", "")
    text = text.replace(",", "") # modifikace druhého zápisu "text" původně zadaného
    prevedeny_text = text.split()
    return prevedeny_text

def vyber_text(texty):
    select_number = input("Enter a number btw. 1 and 3 to select:")
    print("----------------------------------------")
    if not select_number.isnumeric() or int(select_number) < 1 or int(select_number) > 3:
        print("incorrect choice, terminating the program..")
        quit()
    vybrany_text = texty[int(select_number) - 1]
    return vybrany_text

def over_uzivatele(zadane_jmeno, zadane_heslo, registrovani_uzivatele):
    if zadane_jmeno in registrovani_uzivatele.keys():
        if zadane_heslo != registrovani_uzivatele[zadane_jmeno]:
            print("unregistered user, terminating the program..")
            quit()    
    else:
        print("unregistered user, terminating the program..")
        quit()

def zadej_uziv_udaje():
    vloz_jmeno = input("username:")
    vloz_heslo = input("password:")
    return vloz_jmeno, vloz_heslo

def analyzuj_text(texty_k_analyze, registrovani_uzivatele):
    zadane_jmeno, zadane_heslo = zadej_uziv_udaje()
    over_uzivatele(zadane_jmeno, zadane_heslo, registrovani_uzivatele)
    print("----------------------------------------")
    print("Welcome to the app,", zadane_jmeno)
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
    vybrany_text = vyber_text(texty_k_analyze)
    prevedeny_text = preved_text(vybrany_text)
    pocet_slov = analyza(prevedeny_text)
    print(pocet_slov)
    pass

analyzuj_text(TEXTS, uzivatele)