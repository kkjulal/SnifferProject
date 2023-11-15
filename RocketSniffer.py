'''
Faculty of Engineering and Computing (FENC)
School of Computing and Information Technology (SCIT)
CIT4020: Computer Security
Occurrence:
Lecturer: Mr. Kevin Johnson
Project: Packet Sniffer Group Project
Date: November 13, 2023
@author: Kimarley Julal (0704125), Everee Reid (1004481), Micah Brown (1802146)
'''
import csv
import os

import scapy.all as scapy
from scapy.error import Scapy_Exception
from scapy.utils import wrpcap

class Sniffer:
    def __init__(self):
        self.capture = None
        self.filename = None

    def fullsniff(self): #performs a full capture of packets
        amt = self.captureamt()
        print("\n FULL CAPTURE STARTED\n")
        try:
            self.capture = scapy.sniff(count=amt)
        except Scapy_Exception:
            print("Scapy error.")
        print(self.capture.show())
        self.filename = 'Result_fullsniff'
        self.savesniff()

    def ip(self): #captures ipv4 packets
        amt = self.captureamt()
        print("\n IPV4 CAPTURE STARTED\n")
        capture = scapy.sniff(filter='ip', count=amt)
        print(capture.show())
        self.filename = 'Result_ipsniff'
        self.savesniff()

    def ipv6(self): #captures ipv6 packets
        amt = self.captureamt()
        print("\n IPV6 CAPTURE STARTED\n")
        capture = scapy.sniff(filter='ip6', count=amt)
        print(capture.show())
        self.filename = 'Result_ipv6'
        self.savesniff()

    def tcp(self): #captures tcp packets
        amt = self.captureamt()
        print("\n TCP CAPTURE STARTED\n")
        capture = scapy.sniff(filter="tcp", count=amt)
        print(capture.show())
        self.filename = 'Result_tcp'
        self.savesniff()

    def udp(self): #captures ucp packets
        amt = self.captureamt()
        print("\n UDP CAPTURE STARTED\n")
        capture = scapy.sniff(filter="udp", count=amt)
        print(capture.show())
        self.filename = 'Result_udp'
        self.savesniff()

    def http(self): #captures http packets
        global capture
        amt = self.captureamt()
        print("\n HTTP CAPTURE STARTED\n")
        try:
            capture = scapy.sniff(filter="http", count=amt)
        except Scapy_Exception:
            print("Scapy error.")
        print(capture.show())
        self.filename = 'Result_http'
        self.savesniff()

    def wifi(self): #captures wifi packets
        amt = self.captureamt()
        print("\n WIFI CAPTURE STARTED\n")
        try:
            capture = scapy.sniff(iface="Wi-Fi", filter="tcp", count=amt)
        except Scapy_Exception:
            print("Scapy error.")
            return  -2
        print(capture.show())
        self.filename = 'Result_wifi'
        self.savesniff()

    def ethernet(self): #captures ethernet packets
        amt = self.captureamt()
        print("\n ETHERNET CAPTURE STARTED\n")
        capture = scapy.sniff(iface='Ethernet', count=amt)
        print(capture.show())
        self.filename = 'Result_ethernet'
        self.savesniff()

    def protoport(self): #captures with protocol and port filters packets
        amt = self.captureamt()
        print("\n PROTOCOL/PORT 'FILTER' CAPTURE STARTED\n")
        protocol = input("Enter protocol(http, udp, tcp, etc.): ")
        portnum = input("Enter port (80, 53, etc.): ")
        capture = scapy.sniff(filter=protocol+" port "+portnum, count=amt)
        print(capture.show())
        self.filename = 'Result_protoport'
        self.savesniff()

    def captureamt(self): #//sets the amount of packets to be captured
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

    def savesniff(self): #this function gives the use the option to save the sniff result to a csv file
        option = 0
        while True:
            try:
                option = int(input("Would you like to save a copy of this result? 1-yes 2-no: "))
            except ValueError:
                print("Invalid entry. Try again.")
                continue
            if option == 1:
                #filename = 'Result'
                wrpcap(f"{self.filename}.pcap", self.capture) #save results to a pcap file

                #convert results to csv using pshark
                w=f"cd C:\\Program Files\\Wireshark\\ " #open tshark directory

                #use tshark to parse relevant data
                x=f'tshark -r {self.filename}.pcap -T fields -e frame.number -e frame.time -e frame.protocols -e ip -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, -E quote=d -E occurrence=f > {self.filename}.csv'
                #execute commands
                os.system(w)
                os.system(x)
                print(f"\nCSV file Saved to App path as {self.filename}.csv \n")
                break
            elif option == 2:
                print("\nOk. Returning to main")
                break
            else:
                print("\nInvalid entry. Try again.\n")



