from sbox import sbox_generate

sbox, sbox_i = sbox_generate()
print(f'S-Box: {sbox}\n')
print(f'S-Box inverse: {sbox_i}\n')