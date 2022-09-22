from sypher004 import Sypher004, generate_random_key
from base_conversions import *

k0, k1, k2, k3, k4, k5 = generate_random_key()

# k0 = '0101101110010010'
# k1 = '0000011001001011'
# k2 = '0001111000000011'
# k3 = '1010010101011111'
# k4 = '1110110010111101'
# k5 = '0111110010100101'

print('Key: ', end='')
print(bin2hex(k0), bin2hex(k1), bin2hex(k2), bin2hex(k3), bin2hex(k4), bin2hex(k5))
sypher004_1 = Sypher004(k0, k1, k2, k3, k4, k5)
sypher004_2 = Sypher004(k0, k1, k2, k3, k4, k5)

diff = (8,0,0,0)

m_pairs = []

# Selecting all the message pairs with difference of (8,0,0,0)
for i in range(16):
    for j in range(16):
        for k in range(16):
            for l in range(16):
                m1 = (dec2bin(str(i)), dec2bin(str(j)), dec2bin(str(k)), dec2bin(str(l)))
                m2 = (dec2bin(str(i^8)), dec2bin(str(j)), dec2bin(str(k)), dec2bin(str(l)))
                m_pairs.append((m1, m2))

print(f'Number of message pairs generated for difference {diff}:', len(m_pairs))

counter = 0


# Performing 4 rounds of Sypher004
for m1, m2 in m_pairs:

    # Initializing the state with the message pairs
    sypher004_1.set_state(m1)
    sypher004_2.set_state(m2)

    # Round 1
    c1 = sypher004_1.ENC(k0)
    c2 = sypher004_2.ENC(k0)
    c_diff = tuple([(int(c1[i], 2)^int(c2[i], 2)) for i in range(4)])
    # Verifying the difference
    if (c_diff != diff):
        continue
    
    c1 = sypher004_1.ENC(k1)
    c2 = sypher004_2.ENC(k1)
    c_diff = tuple([(int(c1[i], 2)^int(c2[i], 2)) for i in range(4)])
    if (c_diff != diff):
        continue
    
    c1 = sypher004_1.ENC(k2)
    c2 = sypher004_2.ENC(k2)
    c_diff = tuple([(int(c1[i], 2)^int(c2[i], 2)) for i in range(4)])
    if (c_diff != diff):
        continue
    
    c1 = sypher004_1.ENC(k3)
    c2 = sypher004_2.ENC(k3)
    c_diff = tuple([(int(c1[i], 2)^int(c2[i], 2)) for i in range(4)])
    if (c_diff != diff):
        continue
    else:
        counter+=1
    
    
print(f'Conforming message pairs for difference {diff}: {counter}')

print(f'The probablity of the difference {diff} is {counter/65536}')

