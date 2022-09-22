from sypher004 import Sypher004, generate_random_key, CharactericticSypher004, mySypher004, myCharacteristicSypher004
# k0, k1, k2, k3, k4, k5 = generate_random_key()
# print(k0, k1, k2, k3, k4, k5)
# sypher004 = Sypher004(k0, k1, k2, k3, k4, k5)

# print(sypher004.encrypt(('1010', '1011', '1111', '1011')))

# # from base_conversions import dec2bin, bin2dec

# # sbox = {
# # 	'6':'0',
# # 	'4':'1',
# # 	'12':'2',
# # 	'5':'3',
# # 	'0':'4',
# # 	'7':'5',
# # 	'2':'6',
# # 	'14':'7',
# # 	'1':'8',
# # 	'15':'9',
# # 	'3':'10',
# # 	'13':'11',
# # 	'8':'12',
# # 	'10':'13',
# # 	'9':'14',
# # 	'11':'15'
# #     }

# # new_sb = dict()
# # for i in range(16):
# #     new_sb[dec2bin(str(i))] = dec2bin(sbox[str(i)])

# # print(new_sb)

# from math import perm


# # premap = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# premap = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# def permute(premap, m):
#     permuted = []
#     for i in range(0,16,4):
#         j0 = premap[i]
#         j1 = premap[i+1]
#         j2 = premap[i+2]
#         j3 = premap[i+3]
#         permuted.append(m[j0//4][j0%4]+m[j1//4][j1%4]+m[j2//4][j2%4]+m[j3//4][j3%4])
#     return permuted

# permute(premap, ['0000','0001','0010','0011'])



#Question 7 Test Cases
# k0, k1, k2, k3, k4, k5 = ('0101101011010110','1101101101010111', '0110110111000010', '0100011011010111','1101010010000011', '0100111111000101')

# sypher004 = Sypher004(k0, k1, k2, k3, k4, k5)
# # mysypher004 = mySypher004(k0, k1, k2, k3, k4, k5)
# print(k0, k1, k2, k3, k4, k5)
# tpl = ('1010', '1011', '1111', '1011')
# print(f'Plaintext:{tpl}')
# ct = sypher004.encrypt(tpl)
# print(f'Encrypted:{ct}')
# print(f'Decrypted:{sypher004.decrypt(ct)}')


# Permutation Test
# def permute(premap, m):
#         permuted = []
#         for i in range(0,16,4):
#             j0 = premap[i]
#             j1 = premap[i+1]
#             j2 = premap[i+2]
#             j3 = premap[i+3]
#             permuted.append(m[j0//4][j0%4]+m[j1//4][j1%4]+m[j2//4][j2%4]+m[j3//4][j3%4])
#         return tuple(permuted)
# premap = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# m = ['0000','0001','0010','1011']
# print(permute(premap, m))


#Ques 5 Test cases

# init_state = ['0000','0000','0000','1111']
# # char_sypher004 = CharactericticSypher004(init_state)

# # print(char_sypher004.round())
# # print(char_sypher004.round())
# # print(char_sypher004.probablity)

# d = myCharacteristicSypher004(init_state)
# print(d.round())
premap = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
premap_i = [0]*16
for i in range(0,16):
    premap_i[premap[i]] = i

print(premap_i)
print(premap)