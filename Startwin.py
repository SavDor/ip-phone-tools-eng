from colorama import init, Fore
from colorama import Back
from colorama import Style
import os
import requests
import json
import ipinfo
import time
from urllib.request import urlopen
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
import speedtest

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
    clear()
    print(Fore.GREEN + "Load.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load..")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "City - " + details.city)
    print(Fore.GREEN + "Region - " + details.region)
    print(Fore.GREEN + "Country - " + details.country)
    print(Fore.GREEN + "Location - " + details.loc)
    print(Fore.GREEN + "Org - " + details.org)
    print(Fore.GREEN + "Timezone - " + details.timezone)
    print(Fore.CYAN + "else) Back")
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
    clear()
    print(Fore.GREEN + "Load.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load..")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "Ip - " + IP)
    print(Fore.GREEN + "Org - " + org)
    print(Fore.GREEN + "City - " + city)
    print(Fore.GREEN + "Country - " + country)
    print(Fore.GREEN + "Region - " + region)
    print(Fore.CYAN + "else) Back") 
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
    else:
        clear()
        Help()

def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def SpeedTestWifi():
    clear()
    print(Fore.GREEN + "Load.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load..")
    down = speedtest.Speedtest(secure=True).download()
    uplo = speedtest.Speedtest(secure=True).upload()
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "Speed Download - ",humansize(down))
    print(Fore.GREEN + "Speed Upload - ",humansize(uplo))
    print(Fore.GREEN + "else) Back")
    num3 = input(Fore.MAGENTA +">> ")
    if num3 == "1":
        clear()
        Help()
    else:
        clear()
        Help()

def ChekNumberOne():
    clear()
    print("Enter Number example: +7 0000000000 and +70000000000")
    number = input(Fore.MAGENTA +">> ")
    clear()
    print(Fore.GREEN + "Load.")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load..")
    phoneNumber = phonenumbers.parse(number)
    timeZone = timezone.time_zones_for_number(phoneNumber)
    geolocation = geocoder.description_for_number(phoneNumber,"en")
    service = carrier.name_for_number(phoneNumber,"en")
    time.sleep(0.8)
    clear()
    print(Fore.GREEN + "Load...")
    time.sleep(0.5)
    clear()
    print(Fore.GREEN + "Time Zone - ",timeZone)
    print(Fore.GREEN + "Location - ",geolocation)
    print(Fore.GREEN + "Service provider - ",service)
    print(Fore.GREEN + "else) Back")
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
    print(Fore.CYAN +"2) GeoIP")
    print(Fore.CYAN +"3) Speed Test")
    print(Fore.CYAN +"4) Phone info Option One (loc,provider,timezone)")
    print(Fore.CYAN +"5) Help")
    print(Fore.CYAN +"6) Exit")
Help()

while(True):
    num1 = input(Fore.MAGENTA +">> ")
    if num1 == "6":
        clear()
        print(Fore.GREEN +"Goodbye")
        quit()
    elif num1 == "5":
        clear()
        Help()
    elif num1 == "4":
        clear()
        ChekNumberOne()
    elif num1 == "3":
        clear()
        SpeedTestWifi()
    elif num1 == "2":
        clear()
        GeoIp_one()
    elif num1 == "1":
        Ip_For_Pc()
    else:
        print(Fore.RED +"No Command")