import random


def gen_mac_general():
    v_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    l = list()
    for v in range(0, 12, 1):
        l.append(str(random.choice(v_range)))
    return ''.join(l)


def gen_mac_linux(mac):
    # Generate MAC formated for Unix, Linux, and Juniper
    l = list()
    [l.append(mac[i:i+2]) for i in range(0, len(mac), 2)]
    return ':'.join(l).lower()


def gen_mac_cisco(mac):
    # Generate MAC formated for Cisco
    l = list()
    [l.append(mac[i:i+4]) for i in range(0, len(mac), 4)]
    return '.'.join(l).lower()


mac = gen_mac_general()

l_mac = gen_mac_linux(mac=mac)
print(l_mac)

c_mac = gen_mac_cisco(mac=mac)
print(c_mac)
