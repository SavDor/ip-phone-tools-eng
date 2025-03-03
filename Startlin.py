from colorama import init, Fore
from colorama import Back
from colorama import Style
import requests

init(autoreset=True)

def Ip_For_Pc():
    public_ip = requests.get('https://api.ipify.org').text
    print(f"Public IP Address: {public_ip}")


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
    num1 = input(">> ")
    if num1 == "3":
        print(Fore.GREEN +"Goodbye")
        quit()
    elif num1 == "2":
        Help()
    elif num1 == "1":
        Ip_For_Pc()
    else:
        print(Fore.RED +"No Command")
