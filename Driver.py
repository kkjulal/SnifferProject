'''
Created on 7 Nov 2023

@author: Kimarley Julal (0704125)
'''
import os
from time import sleep

import Scapy


def menu():
    print("\n ROCKET SNIFFER TOOL")
    print("""
    1. Full Capture
    2. Get Source IP data
    3. Get Destination IP data
    4. Get TCP Protocol data
    5. Get UDP Protocol data
    6. Get WiFi data
    7. Get Ethernet data
    8. Get Port 53 & 80 data
    9. Get Port HTTPS data
    0.Exit/Quit
    """)
menu()

try:
    option = int(input("What would you like to do? "))
except:
    print("An exception occured.")

while option != 0:
    if option == 1:
        print("\n LIVE PACKET CAPTURE STARTED\n")
        Scapy.fullsniff()
    elif option == 2:
        print("\n CAPTURING DESTINATION IP DATA\n")
        Scapy.sourceip()
    elif option == 3:
        Scapy.destinip()
    elif option == 4:
        Scapy.tcp()
    elif option == 5:
        Scapy.udp()
    elif option == 6:
        Scapy.wifi()
    elif option == 7:
        Scapy.ethernet()
    elif option == 8:
        Scapy.ports()
    elif option == 9:
        Scapy.http()
    else:
        print("Invalid option. Try again")
        sleep(2)
    menu()
    try:
        option = int(input("What would you like to do? "))
    except:
        print("An exception occured.")

print("\nThanks for using ROCKET SNIFFER.")