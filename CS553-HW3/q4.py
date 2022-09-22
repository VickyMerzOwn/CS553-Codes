from sypher002 import Sypher002, generate_random_key
from base_conversions import *

k0, k1, k2 = generate_random_key()
print("Key: ", end="")
print(f"K0: {k0}, K1: {k1}, K2: {k2}\n")
sypher002 = Sypher002(k0, k1, k2)

mc_pairs = []

# We generate all the message,ciphertext pairs in which message difference is 15
for i in range(16):
    mc_pairs.append((i, i ^ 15, sypher002.encrypt(i), sypher002.encrypt(i ^ 15)))

counter = [0] * 16
matrix = [[0] * 16] * 16
i = 0
for m0, m1, c0, c1 in mc_pairs:
    for k2 in range(16):
        x0 = k2 ^ c0
        x1 = k2 ^ c1
        w0 = sypher002.sbox[x0]
        w1 = sypher002.sbox[x1]
        v0v1 = w0 ^ w1
        if v0v1 == 13:
            counter[k2] += 1
            matrix[i][k2] = 1
        else:
            matrix[i][k2] = 0
    i += 1

print("The counter table for each K2 is: \n")
for row in matrix:
    print(row)
print()

max_occurance = max(counter)
k2_lst = []
for i in range(len(counter)):
    if counter[i] == max(counter):
        k2_lst.append(i)

print(f"Now we look at the highest count for each K2\n")
print(f"The possible values of K2 are {k2_lst}")
