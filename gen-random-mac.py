import random


def gen_mac_general():
    v_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    l = list()
    for v in range(0, 12, 1):
        l.append(str(random.choice(v_range)))
    return ''.join(l)


m = gen_mac_general()

print(f'MAC: {m}')

# Unix/Linux/Juniper Format
n = list()
o = [n.append(m[i:i+2]) for i in range(0, len(m), 2)]
print(f'MAC (Unix/Linux/Juniper): {":".join(n).lower()}')

# Cisco Format
p = list()
q = [p.append(m[i:i+4]) for i in range(0, len(m), 4)]
print(f'MAC (Cisco): {".".join(p).lower()}')
