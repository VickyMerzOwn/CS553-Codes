import random
import json
import os.path
from base_conversions import dec2bin


# This function generates a random S-Box if it does not exist in the current directory
# If it does exist, it loads the S-Box from the file
# The S-Box is stored in sbox.json
# The function returns the S-Box and its inverse
# The function also returns the S-Box as a list if the output_type is set to 'list'
# The function returns the S-Box as a dictionary if the output_type is set to 'dict'


# This function generates a random S-Box if it does not exist in the current directory
# If it does exist, it loads the S-Box from the file
# The S-Box is stored in sbox.json
# The function returns the S-Box and its inverse
# The function also returns the S-Box as a list if the output_type is set to 'list'
# The function returns the S-Box as a dictionary if the output_type is set to 'dict'


def sbox_generate(output_type="dict"):
    lst = [dec2bin(x) for x in range(16)]
    random.shuffle(lst)
    if output_type == "list":
        return lst
    sbox = dict()
    sbox_i = dict()
    for i in range(16):
        sbox[dec2bin(i)] = lst[i]
    if not os.path.isfile("sbox.json"):
        with open("sbox.json", "w+") as outfile:
            data = {}
            data["sbox"] = sbox
            data["sbox_i"] = {v: k for k, v in sbox.items()}
            outfile.seek(0)
            json.dump(data, outfile)
    else:
        with open("sbox.json", "r") as infile:
            data = json.load(infile)
            sbox = data["sbox"]
            sbox_i = data["sbox_i"]
    return sbox, sbox_i
