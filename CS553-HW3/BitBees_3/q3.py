from base_conversions import bin2dec
from sbox import sbox_generate
from ddt import DDT
from base_conversions import bin2dec, dec2bin, bin2hex, hex2bin, hex2dec, dec2hex

sbox, sbox_i = sbox_generate()

print(f'S-Box: {sbox}\n')


ddt = DDT(sbox)
for row in ddt:
    print(row)

print()
max_count = 0
for i in range(16):
    for j in range(16):
        if (i != 0 and j != 0):
            if (ddt[i][j] > max_count):
                max_count = ddt[i][j]

print(f'The maximum count is {max_count} and the maximum differntial probablity is {max_count}/16 = {max_count/16}')
print('Here are the possible transistions: ')
for i in range(16):
    for j in range(16):
        if (i != 0 and j != 0):
            if (ddt[i][j] == max_count):
                print(f'{dec2hex(i)} --> {dec2hex(j)}')


