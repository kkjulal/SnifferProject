'''
Faculty of Engineering and Computing (FENC)
School of Computing and Information Technology (SCIT)
CIT4020: Computer Security
Occurrence:
Lecturer: Mr. Kevin Johnson
Project: Packet Sniffer
Date: November 13, 2023
@author: Kimarley Julal (0704125), Everee Reid (1004481), Micah Brown (1802146)
'''
import os
from time import sleep

import RocketSniffer

#Applicatio Menu
def menu():
    print("\n ROCKET SNIFFER TOOL")
    print("""
    1. Full Capture
    2. Capture IP data
    3. Capture IPV6 data
    4. Capture TCP Protocol data
    5. Capture UDP Protocol data
    6. Capture HTTP Protocol data
    7. Capture WiFi data
    8. Capture Ethernet data
    9. Capture Protocol and Port data
    0.Exit/Quit
    """)


def main():
    call = RocketSniffer.Sniffer()
    try:
        option = int(input("What would you like to do? "))
    except:
        print("An exception occured.")

    while option != 0:
        if option == 1:
            call.fullsniff()
        elif option == 2:
            call.ip()
        elif option == 3:
            call.ipv6()
        elif option == 4:
            call.tcp()
        elif option == 5:
            call.udp()
        elif option == 6:
            call.http()
        elif option == 7:
            call.wifi()
        elif option == 8:
            call.ethernet()
        elif option == 9:
            call.protoport()
        else:
            print("Invalid option. Try again")
            sleep(2)
        menu()
        try:
            option = int(input("What would you like to do? "))
        except:
            print("An exception occured.")

    print("\nThanks for using ROCKET SNIFFER.")

if __name__=="__main__":
    menu()
    main()