import subprocess
from base_conversions import hex2bin, bin2hex, dec2bin, bin2dec, hex2dec, dec2hex
from ddt import DDT
from sbox import sbox_generate
import random
import json
import os.path

class Sypher004:
    def __init__(self, k0, k1, k2, k3, k4, k5):
        self.k0 = k0
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.state = (None, None, None, None)
    

    sbox = {'0000': '0110', '0001': '0100', '0010': '1100', '0011': '0101', '0100': '0000', '0101': '0111', '0110': '0010', '0111': '1110', '1000': '0001', '1001': '1111', '1010': '0011', '1011': '1101', '1100': '1000', '1101': '1010', '1110': '1001', '1111': '1011'}
    sbox_i = {'0000': '0100', '0001': '1000', '0010': '0110', '0011': '1010', '0100': '0001', '0101': '0011', '0110': '0000', '0111': '0101', '1000': '1100', '1001': '1110', '1010': '1101', '1011': '1111', '1100': '0010', '1101': '1011', '1110': '0111', '1111': '1001'}
    premap = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
    premap_i = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
    def permute(premap, m):
        """
        m is a 4-tuple of 4-bit binaries as strings
        """
        permuted = []
        for i in range(0,16,4):
            j0 = premap[i]
            j1 = premap[i+1]
            j2 = premap[i+2]
            j3 = premap[i+3]
            permuted.append(m[j0//4][j0%4]+m[j1//4][j1%4]+m[j2//4][j2%4]+m[j3//4][j3%4])
        return tuple(permuted)

    def set_state(self, state):
        self.state = state

    def ENC(self, k):
        m = self.state
        u = [dec2bin(int(char,2) ^ int(k[i*4:i*4+4], 2)) for i, char in enumerate(m)]
        v = (Sypher004.sbox[u[0]], Sypher004.sbox[u[1]], Sypher004.sbox[u[2]], Sypher004.sbox[u[3]])
        w = Sypher004.permute(Sypher004.premap, v)
        self.state = w
        return w

    def ENCLAST(self, k):
        m = self.state
        u = [dec2bin(int(char,2) ^ int(k[i*4:i*4+4], 2)) for i, char in enumerate(m)]
        v = (Sypher004.sbox[u[0]], Sypher004.sbox[u[1]], Sypher004.sbox[u[2]], Sypher004.sbox[u[3]])
        self.state = v

    def XOR(self, k):
        m = self.state
        u = [dec2bin(int(char,2) ^ int(k[i*4:i*4+4], 2)) for i, char in enumerate(m)]
        self.state = tuple(u)

    def DEC(self, k):
        c = self.state
        u = [dec2bin(int(char,2) ^ int(k[i*4:i*4+4], 2)) for i, char in enumerate(c)]
        w = Sypher004.permute(Sypher004.premap_i, u)
        v = (Sypher004.sbox_i[w[0]], Sypher004.sbox_i[w[1]], Sypher004.sbox_i[w[2]], Sypher004.sbox_i[w[3]])
        self.state = v

    def DECFIRST(self, k):
        c = self.state
        w = [dec2bin(int(char,2) ^ int(k[i*4:i*4+4], 2)) for i, char in enumerate(c)]
        v = (Sypher004.sbox_i[w[0]], Sypher004.sbox_i[w[1]], Sypher004.sbox_i[w[2]], Sypher004.sbox_i[w[3]])
        self.state = v

    # def DECLAST(self, k):
    #     c = self.state
    #     w = [dec2bin(int(char,2) ^ int(k[i*4:i*4+4], 2)) for i, char in enumerate(c)]
    #     self.state = tuple(w)

    def encrypt(self, m):
        self.state = m
        self.ENC(self.k0)
        self.ENC(self.k1)
        self.ENC(self.k2)
        self.ENC(self.k3)
        self.ENCLAST(self.k4)
        self.XOR(self.k5)
        return self.state

    def decrypt(self, c):
        self.state = c
        self.DECFIRST(self.k5)
        self.DEC(self.k4)
        self.DEC(self.k3)
        self.DEC(self.k2)
        self.DEC(self.k1)
        self.XOR(self.k0)
        return self.state

class mySypher004(Sypher004):
    premap = None
    sbox = None
    sbox_i = None
    if (not os.path.isfile('premap.json')):
        premap = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        random.shuffle(premap)
        premap_i = [0]*16
        for i in range(0,16):
            premap_i[premap[i]] = i
        with open('premap.json', 'w+') as outfile:
            data = {}
            data['premap'] = premap
            data['premap_i'] = premap_i
            outfile.seek(0)
            json.dump(data, outfile)
        # print(premap)
    else:
        with open('premap.json', 'r') as infile:
            data = json.load(infile)
            premap = data['premap']
            # print(premap)
    
    if (not os.path.isfile('sbox.json')):
        sbox, sbox_i = sbox_generate()
        with open('sbox.json', 'w+') as outfile:
            data = {}
            data['sbox'] = sbox
            data['sbox_i'] = sbox_i
            outfile.seek(0)
            json.dump(data, outfile)
    else:
        with open('sbox.json', 'r') as infile:
            data = json.load(infile)
            sbox = data['sbox']
            sbox_i = data['sbox_i']

class CharactericticSypher004():
    def __init__(self, d):
        self.state = d
        CharactericticSypher004.DDT = DDT(mySypher004.sbox)
        self.probablity = 1

    def get_probablity(self):
        return self.probablity

    def round(self):
        for i in range(4):
            if (self.state[i] != '0000'):
                in_diff = int(self.state[i], 2)
                max_val = 0
                for j in CharactericticSypher004.DDT[in_diff]:
                    if (j > max_val):
                        max_val = j
                out_diff = CharactericticSypher004.DDT[in_diff].index(max_val)
                self.probablity = self.probablity * (max_val/16)
                self.state[i] = dec2bin(out_diff)
        
        self.state = list(Sypher004.permute(Sypher004.premap, self.state))
        return self.state
    
                    
class myCharacteristicSypher004(CharactericticSypher004):
    def __init__(self, d):
        self.state = d
        myCharacteristicSypher004.DDT = DDT(mySypher004.sbox)
        self.probablity = 1
        self.round_count = 1

    def round(self):
        prev = self.state
        for i in range(4):
            if (self.state[i] != '0000'):
                in_diff = int(self.state[i], 2)
                max_val = 0
                for j in myCharacteristicSypher004.DDT[in_diff]:
                    if (j > max_val):
                        max_val = j
                out_diff = myCharacteristicSypher004.DDT[in_diff].index(max_val)
                self.probablity = self.probablity * (max_val/16)
                self.state[i] = dec2bin(out_diff)
        print(f"Round: {self.round_count}")
        print(f"{prev} -> {self.state} with probablity {self.get_probablity()} (Substitution Layer)")
        prev = self.state
        self.state = list(mySypher004.permute(mySypher004.premap, self.state))
        print(f"{prev} -> {self.state} with probablity 1 (Permutation Layer)")
        print()
        self.round_count += 1
        return self.state



def generate_random_key():
    out = subprocess.Popen(['openssl', 'rand', '-hex', '12'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    rand_num = hex(int(stdout[:-1], 16))[2:]
    k0 = hex2bin(rand_num[0:4])
    k1 = hex2bin(rand_num[4:8])
    k2 = hex2bin(rand_num[8:12])
    k3 = hex2bin(rand_num[12:16])
    k4 = hex2bin(rand_num[16:20])
    k5 = hex2bin(rand_num[20:24])
    return k0, k1, k2, k3, k4, k5