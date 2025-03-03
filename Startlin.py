from colorama import init, Fore
from colorama import Back
from colorama import Style
import os
import requests
import json
from urllib.request import urlopen

init(autoreset=True)

import os

clear = lambda: os.system('clear')

clear()

def Ip_For_Pc():
    clear()
    public_ip = requests.get('https://api.ipify.org').text
    print(f"Public IP Address: {public_ip}")
    print(Fore.CYAN + "y) More info")
    print(Fore.CYAN + "else) Back")
    num2 = input(Fore.MAGENTA +">> ")
    if num2 == "y":
        Ip_more_info()
    else:
        clear()
        Help()

def Ip_more_info():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    print(Fore.CYAN + "Ip - " + IP)
    print(Fore.CYAN + "Org - " + org)
    print(Fore.CYAN + "City - " + city)
    print(Fore.CYAN + "Country - " + country)
    print(Fore.CYAN + "Region - " + region)
    print(Fore.CYAN + "1) Back") 
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()

def Help():
    print(Fore.CYAN +'███████████████████████████████████████')
    print(Fore.CYAN +'████████ ██████████  ██████████████████')
    print(Fore.CYAN +'███████████████████ █ █████████████████')
    print(Fore.CYAN +'████████ ██████████ █ █████████████████')
    print(Fore.CYAN +'████████ ██████████  ██████████████████')
    print(Fore.CYAN +'████████ ██████████ ███████████████████')
    print(Fore.CYAN +'████████ ██████████ ███████████████████')
    print(Fore.CYAN +'███████████████████████████████████████')
    print("")
    print(Fore.CYAN +"1) Your Ip Address")
    print(Fore.CYAN +"2) Help")
    print(Fore.CYAN +"3) Exit")
Help()

while(True):
    num1 = input(Fore.MAGENTA + ">> ")
    if num1 == "3":
        clear()
        print(Fore.GREEN +"Goodbye")
        quit()
    elif num1 == "2":
        clear()
        Help()
    elif num1 == "1":
        Ip_For_Pc()
    else:
        print(Fore.RED +"No Command")
