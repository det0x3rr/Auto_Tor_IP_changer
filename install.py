import os
import subprocess

choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system

if str(choice) =='Y' or str(choice)=='y':
    # Checking pip is installed or not
    try:
        check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
        if str('install ok installed') in str(check_pip3):
            pass
    except subprocess.CalledProcessError:
        print('[+] pip3 not installed')
        subprocess.check_output('sudo apt update',shell=True)
        subprocess.check_output('sudo apt install python3-pip -y', shell=True)
        print('[!] pip3 installed succesfully')


    # checking request is installed or not
    try:
        import requests
    except Exception:
        print('[+] python3 requests is not installed')
        os.system('pip3 install requests')
        os.system('pip3 install requests[socks]')
        print('[!] python3 requests is installed ')


    # checking tor is installed or not
    try:
        check_tor = subprocess.check_output('which tor', shell=True)
    except subprocess.CalledProcessError:
        print('[+] tor is not installed !')
        subprocess.check_output('sudo apt update',shell=True)
        subprocess.check_output('sudo apt install tor -y',shell=True)
        print('[!] tor is installed succesfully ')

    run('chmod 777 autoTOR.py')
    run('mkdir /usr/share/aut')
    run('cp autoTOR.py /usr/share/aut/autoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/autoTOR.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/autoTOR.py')
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42m sudo aut \x1b[0m in terminal ''')


elif str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] now Auto Tor Ip changer  has been removed successfully')
