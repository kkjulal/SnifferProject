'''
Created on 7 Nov 2023

@author: Kimarley Julal (0704125)
'''
import scapy.all as scapy
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, ICMP, TCP


def fullsniff(): #performs a full capture of packets
    amt = captureamt()
    print("\n FULL CAPTURE STARTED\n")
    capture = scapy.sniff(count=amt)
    print(capture.show())
    dummysavepdf(capture)

def ip():
    amt = captureamt()
    capture = scapy.sniff(filter='ip', count=amt)
    print(capture.show())
    dummysavepdf(capture)


def ipv6(): #captures all destination ip
    amt = captureamt()
    capture = scapy.sniff(filter='ipv6', count=amt)
    print(capture.show())
    dummysavepdf(capture)

def tcp():
    amt = captureamt()
    capture = scapy.sniff(filter="tcp", count=amt)
    print(capture.show())
    dummysavepdf(capture)

def udp():
    amt = captureamt()
    capture = scapy.sniff(filter="udp", count=amt)
    print(capture.show())
    dummysavepdf(capture)

def wifi():
    amt = captureamt()
    capture = scapy.sniff(iface="wifi0", count=amt)
    print(capture.show())
    dummysavepdf(capture)

def ethernet():
    amt = captureamt()
    capture = scapy.sniff(iface="eth0", count=amt)
    print(capture.show())
    dummysavepdf(capture)

def protoport():
    amt = captureamt()
    protocol = input("Enter protocol: ")
    portnum = input("Enter port: ")
    capture = scapy.sniff(filter=""+protocol+" port "+portnum+"", count=amt)
    print(capture.show())
    dummysavepdf(capture)


def dummysavepdf(data):

    option = 0

    while True:
        try:
            option = int(input("Would you like to save a copy of this result? 1-yes 2-no: "))
        except ValueError:
            print("Invalid entry. Try again.")
            continue
        if option == 1:
            print("\nPDF Saved.\n")
            break
        elif option == 2:
            print("\nOk. Returning to main")
            break
        else:
            print("\nInvalid entry. Try again.\n")


def captureamt(): #//sets the amount of packets to be captured

    global option
    while True:
        try:
            option = int(input("How many packets do you want to capture? "))
        except ValueError:
            print("Invalid entry. Try again.")
            continue
        if option > 0:
            break
    return option



