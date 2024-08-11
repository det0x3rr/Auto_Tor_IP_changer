# $${\color{green} Auto\_Tor \_IP\_changer \space V 2.2 }$$
![](https://github.com/det0x3rr/Auto_Tor_IP_changer/blob/master/images/intro.gif)


## Requirements

 - Python, Tor, Python - requests, requests[socks]

## Installation For Linux
 - `git clone https://github.com/det0x3rr/Auto_Tor_IP_changer.git`
 - `cd Auto_Tor_IP_changer`
 - `sudo python3 install.py`
 - To run, enter `sudo aut`
 - After that add the socks proxy -> host -  127.0.0.1, port - 9050
	 - You can add it ---
	 -	System wide using network > manual proxy in settings
	 -	OR
	 -	In firefox - enable socks5 proxy and also proxy DNS when using SOCKS v5
	 -	![](https://github.com/det0x3rr/Auto_Tor_IP_changer/blob/master/images/proxy.png)
	 

##  Original Repo Link
[FDX100-Auto_Tor_IP_Changer](https://github.com/FDX100/Auto_Tor_IP_changer)

## Improvements in V 2.2

 - Added User input validation
 - Used Functional approached
 - Error Handling
 - Changed url to get current ip address
 - Removed text highlight which was caused because of using the color code in print function, with the help sys.stdout.write({color-code})
 - Stream the output of ip address on same line
 - Added default values for SECONDS_TO_CHANGE_IP & NO._OF_TIME_IP_WILL_CHANGE
 - Moved the requirements code to install.py file
 - Tor will be stopped on error or closed or completion of no. of times the ip changed


> Open for improvements...
