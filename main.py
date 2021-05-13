from bs4 import BeautifulSoup
import time
import requests
import os

link = 0
min_price = 1
max_price = 2
link_test = "https://www.youtube.com"
test = False
urls = []


def find_price_opensea(link, min, max):
    try:
        html_text = requests.get(link, headers={'User-Agent': 'Custom'}).text
        soup = BeautifulSoup(html_text, 'lxml')
        price_eth = soup.find('div', class_='Price--amount').text
        price_dls = soup.find('div', class_='Price--fiat--amount').text.replace("(", "").replace(")", "")
        name = soup.find('header', class_='item--title').text
    except:
        print(f"Url: '{link}' is not valid.")
        print("Check your internet connection and try again, if the issue persists, try deleting the item and adding it again.")
        return

    print(f'Name: {name}')
    print(f'Price (ETH): Ξ{price_eth}')
    print(f'Price (USD): {price_dls}')

    if float(price_dls[1:].replace(",", "")) < min:
        print("The price is under the lower limit!")
        #os.system("say 'EL precio actual es menor al límite inferior.'")
    if float(price_dls[1:].replace(",", "")) > max:
        print("El precio es mayor al límite superior!")
        print("The price is over the upper limit!")
        #os.system("say 'EL precio actual es mayor al límite superior.'")
    print()


def scan_urls():
    global urls
    for url in urls:
        print()
        find_price_opensea(url[link], url[min_price], url[max_price])

def delete():
    type = False
    index = 0
    while type == False:
        try:
            index = int(input("Art piece number you want to delete: "))
            type = True
        except ValueError:
            print("You must type an integer. Try again.")
            type = False

    while index > len(urls) or index <= 0:
        print("Art piece does not exist, try again.")
        index = int(input("Art piece number you want to delete: "))
    print(f"Art piece {index} deleted from the list.")
    os.system("afplay del.mpeg&")
    #os.system("say 'Ítem eliminado'")
    urls.pop(index-1)
    print("This is the updated list.")
    print()
    scan_urls()
    print()

def add():
    new = input("Copy and paste the art piece url here: ")
    if "opensea.io" in new:
        min_type = False
        max_type = False
        min_value = 0
        max_value = 0

        while not min_type:
            min_value = input("What is the lower limit you want for this piece? (USD): $")
            try:
                min_value = int(min_value)
                min_type = True
            except:
                print("You must type an integer. Try again.")
                min_type = False

        while not max_type:
            max_value = input("What is the upper limit you want for this piece? (USD): $")
            try:
                max_value = int(max_value)
                max_type = True
            except:
                print("You must type an integer. Try again.")
                max_type = False

        urls.append([new, min_value, max_value])
        print("url added")
        os.system("afplay add.mpeg&")
        #os.system("say 'URL agregada'")
        print("This is the updated list.")
        print()
        scan_urls()
        print()
    else:
        print("Url not valid, it must be from opensea.io")


#INICIO DEL PROCESO
while test == False: #primero
    print("Testing your connection, please wait a few seconds...")
    try:
        html_text = requests.get(link_test, headers={'User-Agent': 'Custom'})
        print("Connection successful")
        test = True
    except:
        print("No internet connection, retrying in 10 seconds.")
        time.sleep(10)
        test = False


inicial = input("Copy and paste the art piece url here: ")
while inicial not in ["", "\n"]: #segundo
    if "opensea.io" in inicial:

        min_type = False
        max_type = False
        min_value = 0
        max_value = 0

        while not min_type:
            min_value = input("What is the lower limit you want for this piece? (USD): $")
            try:
                min_value = int(min_value)
                min_type = True
            except:
                print("You must type an integer. Try again.")
                min_type = False

        while not max_type:
            max_value = input("What is the upper limit you want for this piece? (USD): $")
            try:
                max_value = int(max_value)
                max_type = True
            except:
                print("You must type an integer. Try again.")
                max_type = False

        urls.append([inicial, min_value, max_value])
        print("Url added")
        os.system("afplay add.mpeg&")
        #os.system("say 'URL agregada'")
    else:
        print("url not valid, it must be from opeansea.io")
    inicial = input("Copy and paste the url for the piece you want to follow (Enter to end list): ")
print("============================================")
print()
scan_urls()
print()

#Ciclo Principal
while True: #tercero
    print("What do you want to do: ")
    print("1: Add art piece.")
    print("2: Delete art piece.")
    print("3: Show list.")
    print("Type anything else to leave the program running in the background.")
    opcion = input("> ")
    if opcion == "1":
        add()
    elif opcion == "2":
        if len(urls) > 0:
            delete()
        else:
            print("List is empty, can't delete anything.")
    elif opcion == "3":
        scan_urls()
    elif opcion not in "123" or opcion == "123":

        test_horas = False
        horas = 0

        while not test_horas:
            horas = input("How many hours do you want to leave the program running for: ")
            try:
                horas = int(horas)
                test_horas = True
            except:
                print("You must type an integer, try again.")
                test_horas = False

        print("PERFECT!")
        starttime = time.time()
        clock = 0
        while clock < horas:
            time.sleep(10 - ((time.time() - starttime) % 10))
            clock += 1
            scan_urls()
