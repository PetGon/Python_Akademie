"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petra Gondek ♀
email: petra@gondek.online
discord: Petra G.#9835
"""
from datetime import datetime
import random

def check_result(try_number):
    if try_number <= 2:
        result_txt = "amazing"
    elif try_number > 2 and try_number <= 4:
        result_txt = "gr8"
    elif try_number > 4 and try_number <= 8:
        result_txt = "good"
    elif try_number > 8 and try_number <= 16:
        result_txt = "average"    
    else:
        result_txt = "not so good"
    return result_txt

def count_cows_bulls(random_num, input_num):
    bulls = 0
    cows = 0
    for iter in range(len(random_num)):
        if input_num[iter-1] in random_num:  # pokud je splněno, je to kráva nebo býk
            if input_num[iter-1] == random_num[iter-1]:  # je to býk
                bulls += 1
            else:
                cows += 1
    return bulls, cows

def input_check_num():
    while True:
        print("-----------------------------------------------")
        input_num = input(">>> ")
        if input_num.isdigit():
            if int(input_num) >= 1000 and int(input_num) <= 9999: 
                if check_unique(input_num):
                    return list(input_num)
                else:
                    print("All numbers must be unique!")
            else:
                print("Please, enter the number between 1000 and 9999.")
        else:
            print("Please, enter only digits!")

def check_unique(num_list):
    if len(num_list) == len(set(num_list)):
        return True
    else:
        return False
    
def gen_num():
    while True:
        random_num = random.randint(1000, 9999)
        random_num = list(str(random_num))
        if check_unique(random_num):
            return random_num

def input_user():
    username = input("username:")
    return username

def run_game():
    bulls = 0
    try_number = 0
    username = input_user()
    print(f"Hi there {username}!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    random_num = gen_num()
    #print(random_num) #pro debug
    print("Enter a number:") 
    start_time = datetime.now() 
    while bulls < len(random_num):
        try_number += 1
        input_num = input_check_num()
        bulls, cows = count_cows_bulls(random_num, input_num)
        if bulls == 1:
            bull_text = "bull"
        else:
            bull_text = "bulls"
        if cows == 1:
            cow_text = "cow"
        else:
            cow_text = "cows"
        if try_number == 1:
            count_txt = "guess"
        else:
            count_txt = "guesses"
        if bulls < len (random_num):
            print(f"{bulls} {bull_text}, {cows} {cow_text}")
    end_time = datetime.now()
    print("Correct, you've guessed the right number")
    print(f"in {try_number} {count_txt}!")
    print(f"The game took {end_time - start_time}.")
    print("-----------------------------------------------")
    result_txt = check_result(try_number)
    print(f"That's {result_txt}.")
    pass

run_game()


    