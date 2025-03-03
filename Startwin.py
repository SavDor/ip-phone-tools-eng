from colorama import init, Fore
from colorama import Back
from colorama import Style
import os
import requests
import json
import ipinfo
from urllib.request import urlopen

init(autoreset=True)

clear = lambda: os.system('cls')

clear()

access_token = 'a34f1aaf828eae'

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

def GeoIp_one():
    print(Fore.CYAN + "Write the Ip")
    Ip = input(Fore.MAGENTA +">> ")
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(Ip)
    print(Fore.GREEN + "City - " + details.city)
    print(Fore.GREEN + "Region - " + details.region)
    print(Fore.GREEN + "Country - " + details.country)
    print(Fore.GREEN + "Location - " + details.loc)
    print(Fore.GREEN + "Org - " + details.org)
    print(Fore.GREEN + "Timezone - " + details.timezone)
    print(Fore.CYAN + "1) Back")
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
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
    print(Fore.GREEN + "Ip - " + IP)
    print(Fore.GREEN + "Org - " + org)
    print(Fore.GREEN + "City - " + city)
    print(Fore.GREEN + "Country - " + country)
    print(Fore.GREEN + "Region - " + region)
    print(Fore.CYAN + "1) Back") 
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
    else:
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
    print(Fore.CYAN +"2) GeoIP Option One")
    print(Fore.CYAN +"3) Help")
    print(Fore.CYAN +"4) Exit")
Help()

while(True):
    num1 = input(Fore.MAGENTA +">> ")
    if num1 == "4":
        clear()
        print(Fore.GREEN +"Goodbye")
        quit()
    elif num1 == "3":
        clear()
        Help()
    elif num1 == "2":
        clear()
        GeoIp_one()
    elif num1 == "1":
        Ip_For_Pc()
    else:
        print(Fore.RED +"No Command")
