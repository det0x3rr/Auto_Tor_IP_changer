# -*- coding: utf-8 -*-

import time
import os
import sys
import requests

sys.stdout.write("\033[0;32m")


def initialize():
    print('''
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.2
from det0x3rr
''')
    print("Original RepoLink - https://github.com/FDX100/Auto_Tor_IP_changer")
    print("Twitter Link - https://x.com/det0x3rr\n")

    os.system("service tor start")
    print("change your  SOCKS to 127.0.0.1:9050 \n")


def validate_user_input(user_input,defaultValue,):
    if(len(user_input)==0):
        return defaultValue
    elif user_input.isdigit():
        if int(user_input)<2:
            if(defaultValue==0):
                return user_input
            else:
                return defaultValue
        return user_input
    else:
        print("Please enter only numbers...")
        quit()


def get_input():
    try:
        SECONDS_TO_CHANGE_IP = input("[+] Time to change Ip in seconds [default 2 second], Press enter for default >> ")
        NO_OF_TIME_IP_WILL_CHANGE = input("[+] How many time do you want to change your ip [default 0 which is for infinite], Press enter for default >> ")

        SECONDS_TO_CHANGE_IP = validate_user_input(SECONDS_TO_CHANGE_IP,2)
        NO_OF_TIME_IP_WILL_CHANGE = validate_user_input(NO_OF_TIME_IP_WILL_CHANGE,0)

        return SECONDS_TO_CHANGE_IP,NO_OF_TIME_IP_WILL_CHANGE

    except KeyboardInterrupt:
        quit()



def get_my_ip():
    url = "https://api.ipify.org/?format=text"
    try:
        get_ip= requests.get(url,proxies=dict(http='socks5h://127.0.0.1:9050',https='socks5h://127.0.0.1:9050'),timeout=10)
        return get_ip.text

    except requests.exceptions.ConnectionError:  
        print("Connection Timeout, please check your internet connection...")
        quit()


ip_address_global=""
def change_ip():
    UP = "\033[1A" # it will take the cursor to previous line
    CLEAR = "\x1b[2K" # it will clear the output of that line where the cursor presents
    os.system("service tor reload")
    ip_address = get_my_ip()
    global ip_address_global
    ip_address_global = ip_address
    print(f"[+] Your IP has been Changed to : {ip_address}")
    print(UP,end=CLEAR)




def main():
    initialize()
    SECONDS_TO_CHANGE_IP,NO_OF_TIME_IP_WILL_CHANGE = get_input()

    print(f"\n[+] SECONDS_TO_CHANGE_IP = {SECONDS_TO_CHANGE_IP}")
    if(NO_OF_TIME_IP_WILL_CHANGE==0):
        print(f"[+] NO._OF_TIME_IP_WILL_CHANGE = inifinte\n")
    else:
        print(f"[+] NO_OF_TIME_IP_WILL_CHANGE = {NO_OF_TIME_IP_WILL_CHANGE} times\n")


    def run():
        try:
            time.sleep(int(SECONDS_TO_CHANGE_IP))
            change_ip()
        except KeyboardInterrupt:
            print(f"[+] Your IP has been Changed to : {ip_address_global}")
            print('\nshutdowning.....')
            print('Done')
            os.system("service tor stop")
            quit()

    if int(NO_OF_TIME_IP_WILL_CHANGE) ==int(0):
        while True:
            run()
    else:
        for i in range(int(NO_OF_TIME_IP_WILL_CHANGE)):
           run()
        print(f"[+] Your IP has been Changed to : {ip_address_global}")          
          

    
if __name__ == "__main__":
    main()