from sypher004 import Sypher004, generate_random_key
from sbox import sbox_generate
import random
import json
import os.path
class mySypher004(Sypher004):
    premap = None
    sbox = None
    sbox_i = None
    if (not os.path.isfile('premap.json')):
        premap = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        random.shuffle(premap)
        with open('premap.json', 'w+') as outfile:
            data = {}
            data['premap'] = premap
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

    # with open('config.json') as f:
    #     config = json.load(f)


    # premap = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # random.shuffle(premap)


# k0, k1, k2, k3, k4, k5 = generate_random_key()
# # print(k0, k1, k2, k3, k4, k5)
# sypher004 = Sypher004(k0, k1, k2, k3, k4, k5)
# mysypher004 = mySypher004(k0, k1, k2, k3, k4, k5)
# # sypher0042 = Sypher004(k0, k1, k2, k3, k4, k5)

# print(sypher004.encrypt(('1010', '1011', '1111', '1011')))
# print(mysypher004.encrypt(('1010', '1011', '1111', '1011')))