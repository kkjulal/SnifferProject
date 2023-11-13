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
    2. Get IP data
    3. Get IPV6 data
    4. Get TCP Protocol data
    5. Get UDP Protocol data
    6. Get WiFi data
    7. Get Ethernet data
    8. Get Protocol and/ Port data
    0.Exit/Quit
    """)
menu()

try:
    option = int(input("What would you like to do? "))
except:
    print("An exception occured.")

while option != 0:
    if option == 1:
        Scapy.fullsniff()
    elif option == 2:
        Scapy.ip()
    elif option == 3:
        Scapy.ipv6()
    elif option == 4:
        Scapy.tcp()
    elif option == 5:
        Scapy.udp()
    elif option == 6:
        Scapy.wifi()
    elif option == 7:
        Scapy.ethernet()
    elif option == 8:
        Scapy.protoport()
    else:
        print("Invalid option. Try again")
        sleep(2)
    menu()
    try:
        option = int(input("What would you like to do? "))
    except:
        print("An exception occured.")

print("\nThanks for using ROCKET SNIFFER.")