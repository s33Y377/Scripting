from scapy.layers.inet import IP

# import scapy.all.Ether
# import scapy.all.IP
# import scapy.all.TCP

a = IP(ttl=10)
print(a)
print(a.src)
a.dst = "192.168.16.152"
print("Packet", a)
print("sourcse", a.src)
del a.ttl
print("Packet", a)
print("Time to live", a.ttl)
print("Packet", IP())
print(IP(proto=55) / TCP())
print(IP() / TCP())
print(Ether() / IP() / TCP())
print(Ether() / IP() / TCP() / UDP())
print(IP(_))
