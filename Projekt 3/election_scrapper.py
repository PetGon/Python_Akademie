"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Petra Gondek
email: petra@gondek.online
discord: Petra G#9835
"""

import requests
from bs4 import BeautifulSoup
import sys
import csv

def save_csv_file(final_list, csv_file):
    print(f"Converting to CSV and saving the file.")
    with open(csv_file, "w+", newline='', encoding='utf-8') as csv_file:
        write_csv = csv.writer(csv_file)
        write_csv.writerow(list(final_list[0].keys()))
        for list_line in final_list:
            write_csv.writerow(list_line.values())    

def process_cities(city_list):
    print(f"Processing cities...")
    max_parties = 0
    final_list = []
    for city in city_list:
        city_reply = get_reply(city["link"])
        city_soup = make_reply_soup(city_reply)
        city_tables = get_tables(city_soup)
        main_rows = get_all_raws(city_tables,[0])
        result_rows = get_all_raws(city_tables, [*range(1,len(city_tables),1)])
        main_data = get_main_data(main_rows)
        result_data = get_result_data(result_rows)
        if max_parties == 0:
            max_parties = len(result_data)
        if len(result_data) != max_parties: # if number of parties is not equal max. parties = page not completed.
            print(f"List of parties in {city['location']} is not complete.")
            exit()
        final_dict_row = city
        final_dict_row.pop("link")
        final_dict_row.update(main_data)
        final_dict_row.update(result_data)
        final_list.append(final_dict_row)
        print(f"{city['location']} done.")
    return final_list

def get_result_data(result_rows):
    result_data = {}
    for row in result_rows:
        column_cislo = row.find_all('td', class_="cislo")
        column_name = row.find_all('td', class_="overflow_name")
        if len(column_cislo) > 0:
            result_data[column_name[0].text] = int(column_cislo[1].text.replace("\xa0","")) # remove UTF8 " ", converting to INT
    return result_data

def get_main_data(main_rows):
    main_data = {}
    for row in main_rows:
        column_cislo = row.find_all('td', class_="cislo")
        if len(column_cislo) > 0:
            # column 3 = registered, column 6 = envelopes returned, column 7 = returned envelopes valid
            main_data["registered"] = int(column_cislo[3].text.replace("\xa0","")) # remove UTF8 " ", converting to INT
            main_data["envelopes"] = int(column_cislo[6].text.replace("\xa0","")) # remove UTF8 " ", converting to INT
            main_data["valid"] = int(column_cislo[7].text.replace("\xa0","")) # remove UTF8 " ", converting to INT
    return main_data   

def get_city_list(rows, base_url):
    city_list = []
    for row in rows:
        column_cislo = row.find_all('td', class_="cislo")
        column_name = row.find_all('td', class_="overflow_name")
        if len(column_cislo) > 0:
            link = column_cislo[0].find_all('a')
            if len(link) == 0:
                print (f"Web page does not contain city list!")
                exit()
            full_link = base_url + link[0].attrs['href']
            city_code = column_cislo[0].text # column 0 = city code
            city_location = column_name[0].text # column 1 = city location
            city_list.append({"link": full_link,"code": city_code, "location": city_location})
    return city_list

def get_all_raws(tables, id_table_list):
    all_rows = []
    for table_id in id_table_list:
        rows = tables[table_id].find_all('tr')
        all_rows.extend(rows)
    return all_rows    

def get_tables(soup):
    tables = soup.find_all('table')
    return tables

def make_reply_soup(request):
    soup = BeautifulSoup(request.text, 'html.parser')
    return soup

def get_reply(url):
    get_all_reply= requests.get(url)
    return get_all_reply

def get_final_list(url):
    print(f"Scrapped page: {url}")
    base_url = url[:(url.rfind('/'))+1]
    reply = get_reply(url)
    status_code = reply.status_code
    if status_code != 200:
        print (f"Web page cannnot be reached. Error code: {status_code}!")
        exit()
    soup = make_reply_soup(reply)
    tables = get_tables(soup)
    rows = get_all_raws(tables, [*range(0,len(tables),1)])
    city_list = get_city_list(rows, base_url)
    final_list = process_cities(city_list)
    return final_list

def scrape_web(args):
    if len(sys.argv) != 3:
        print("Missing 2 arguments!")
        print("1st argument - url for scrapping.")
        print("2nd srgument - filename for CSV export.")
        exit()
    final_list = get_final_list(args[1])
    save_csv_file(final_list, args[2])

scrape_web(sys.argv)