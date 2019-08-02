#!/usr/bin/python
#
# This is a small, simple script to test your server's abilities to spoof IPv4 packets or not. 
# You should use this instead of things like caida project's tool, because they're rumored to 
# collect data or hand it off to others who harass the server/network owners until they re-configure 
# their networks and discontinue allowing spoofed packets.
#
# By default, this script sends spoofed packets to fuzzme.packet.tel - but it can be configured to 
# send them anywhere. You can download a constantly running pcap by typing:
# wget http://fuzzme.packet.tel/fuzzme.packet.tel.last10minutes.pcap
#
# Requires scapy and a spoofy box
#
# Enjoy!
# @notdan (https://twitter.com/notdan
#
# (Originally written by @notdan; Rights transferred to PACKET.TEL LLC.)
# Maintained by the PACKET.TEL LLC - Internet Research Group
#

from scapy.all import *

howmany = 30                          # Change this if u want 
destination = "fuzzme.packet.tel"     # u can also change this too!
message = "yes hello! this is an IPv4 packet header spoofing test from packet.tel's spoofboitest.py test tool!"

print("\r\n---------------------------------------------------------------")
print("------- PACKET.TEL LLC - Internet Research Group - 2019 -------")
print("---------------------- www.packet.tel -------------------------\r\n")
print("Originally by @notdan (https://twitter.com/notdan)\r\n\r\n")
print("[*] We're gonna be spoofing now!")
print("[*] How many packjets r we sending: ")
print(howmany)
print("[*] Where we sending deez spoofy bois to: ")
print(destination)
print("[*] Verifying fuzzme.packet.tel still lives on the internet with ICMP ping...")
send(IP(dst="fuzzme.packet.tel")/ICMP())
print("[*] Sending some spoofy packjets to da box!")
packjet = IP(src=RandIP(),dst=destination)/ICMP()/"spooy boi packet tester by notdan of packet.tel llc"

send(packjet,count=howmany)
print("[*] If you used the default fuzzme.packet.tel destination, you can")
print("[*] grab the most recent pcap from the server at:")
print("[*] http://fuzzme.packet.tel/fuzzme.packet.tel.last10minutes.pcap")
