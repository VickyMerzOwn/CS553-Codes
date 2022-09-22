from base_conversions import bin2dec, dec2bin, bin2hex, hex2bin, hex2dec, dec2hex

# This function generates a DDT for the given S-Box
def DDT(sbox):
    ddt = [[0]*16 for i in range(16)]
    for o in range(16):
        for i in range(16):
            for m0 in range(16):
                m1 = m0^i
                v0 = int(bin2dec(sbox[dec2bin(m0)]))
                v1 = int(bin2dec(sbox[dec2bin(m1)]))
                if (v0^v1 == o):
                    ddt[i][o] += 1
    return ddt