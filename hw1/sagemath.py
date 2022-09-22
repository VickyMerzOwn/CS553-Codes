import math


M = 1225
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

candidate_keys_a = []

for i in range(0, M):
    if (math.gcd(i, M) == 1):
        candidate_keys_a.append(i)

print(f'Candidate keys after GCD condition {candidate_keys_a}')

candidate_keys_a_2 = []

for a in candidate_keys_a:
    if (modInverse(a, M)%M == a):   # a^-1 mod M = a mod M, Here a is modular inverse
        candidate_keys_a_2.append(a)

print(f'Candidate keys after inverse condition {candidate_keys_a_2}')

final_keys = []

for b in range(0, M):
    for a in candidate_keys_a_2:
        if (((a+1)*b)%M == 0):
            final_keys.append((a, b))

# for key in final_keys:
#     print(f'{key}')

x = len(final_keys)
print(f"Total number of keys for m = {M} is {x}")
# from sage.all import *

# @interact
# def shift_cipher(message = input_box(default='"secrets"', label="Message:"), shift=slider(0,25,1,3, label="Shift by:")):
#     A = AlphabeticStrings()
#     S = ShiftCryptosystem(A)
#     message = S.encoding(message)
#     C = S.enciphering(shift, message)
#     print("This is your encrypted text shifted by",shift,":")
#     print(C)


# import math


# M = 15
# def modInverse(a, m):
     
#     for x in range(1, m):
#         if (((a%m) * (x%m)) % m == 1):
#             return x
#     return -1

# candidate_keys_a = []

# for i in range(0, M):
#     if (math.gcd(i, M) == 1):
#         candidate_keys_a.append(i)

# print(f'Candidate keys after GCD condition {candidate_keys_a}')

# candidate_keys_a_2 = []

# for a in candidate_keys_a:
#     if (modInverse(a, M)%M == a):   # a^-1 mod M = a mod M, Here a is modular inverse
#         candidate_keys_a_2.append(a)

# print(f'Candidate keys after inverse condition {candidate_keys_a_2}')

# final_keys = []

# for b in range(0, M):
#     for a in candidate_keys_a_2:
#         if (((a+1)*b)%M == 0):
#             final_keys.append((a, b))

# for key in final_keys:
#     print(f'Key is {key}')