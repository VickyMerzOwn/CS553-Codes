import subprocess
class Sypher002:
    def __init__(self, k0, k1, k2):
        self.k0 = int(k0, 16)
        self.k1 = int(k1, 16)
        self.k2 = int(k2, 16)

    sbox = {
    0:6,
    1:4, 
    2:12,
    3:5,
    4:0,
    5:7,
    6:2,
    7:14,
    8:1,
    9:15,
    10:3,
    11:13,
    12:8,
    13:10,
    14:9,
    15:11
    }
    sbox_i = {
    6:0,
    4:1,
    12:2,
    5:3,
    0:4,
    7:5,
    2:6,
    14:7,
    1:8,
    15:9,
    3:10,
    13:11,
    8:12,
    10:13,
    9:14,
    11:15
    }

    def encrypt(self, m):
        u = m ^ self.k0
        v = self.sbox[u]
        w = v ^ self.k1
        x = self.sbox[w]
        c = x ^ self.k2
        return c
    
    def decrypt(self, c):
        x = c ^ self.k2
        w = self.sbox_i[x]
        v = w ^ self.k1
        u = self.sbox_i[v]
        m = u ^ self.k0
        return m
    
def generate_random_key():
    k0, k1, k2 = 0, 0, 0
    while (k0 == 0 or k1 == 0 or k2 == 0):
        out = subprocess.Popen(['openssl', 'rand', '-hex', '2'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        rand_num = hex(int(stdout[:-1], 16))[2:]
        k0 = rand_num[0:1]
        k1 = rand_num[2:3]
        k2 = rand_num[3:4]
    return k0, k1, k2
        


