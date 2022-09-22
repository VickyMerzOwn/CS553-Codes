import os
# Queries that oracle returned for the range 0-15
dict_oracle = {
	0:10,
	1:4,
	2:11,
	3:2,
	4:5,
	5:0,
	6:12,
	7:14,
	8:1,
	9:3,
	10:6,
	11:15,
	12:8,
	13:7,
	14:9,
	15:13
}

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

suitable_mc = []
for i in range(0, 16):
	suitable_mc.append((i, i^15,dict_oracle[i],dict_oracle[i^15]))

counter = [0]*16

for m0,m1,c0,c1 in suitable_mc:
	for k2 in range(16):
		x0 = k2^c0
		x1 = k2^c1
		w0 = sbox_i[x0]
		w1 = sbox_i[x1]
		v0v1 = w0^w1
		if (v0v1 == 13):
			counter[k2] += 1


max_occurance = max(counter)
k2_lst = []
for i in range(len(counter)):
	if (counter[i] == max(counter)):
		print(f'The value of k2 is most likely {i} with total of {counter[i]} occurances of v0, v1 difference of 13')
		k2_lst.append(i)

k2 = k2_lst[0]


mc2_pairs = []
for k2 in range(16):
	for m0,m1,c0,c1 in suitable_mc:
		x0 = k2^c0
		x1 = k2^c1
		w0 = sbox_i[x0]
		w1 = sbox_i[x1]

k2 = 1
# print(k2)
# print(k2)
for m0 in range(16):
	for m1 in range(16):
		if (m0 ^ m1 != 15):
			continue
		for k1 in range(16):
			x0 = k2^dict_oracle[m0]
			x1 = k2^dict_oracle[m1]
			w0 = sbox_i[x0]
			w1 = sbox_i[x1]
			v0 = k1^w0
			v1 = k1^w1
			u0 = sbox_i[v0]
			u1 = sbox_i[v1]
			if (m0^m1 == u0^u1):
				print(k1, end = ' ')
		print('')
print('-----------------------------')
k1 = 13 #in all possible keys, 13 was common

for m0 in range(16):
	for m1 in range(16):
		if (m0 ^ m1 != 15):
			continue
		for k0 in range(16):
			x0 = k2^dict_oracle[m0]
			x1 = k2^dict_oracle[m1]
			w0 = sbox_i[x0]
			w1 = sbox_i[x1]
			v0 = k1^w0
			v1 = k1^w1
			u0 = sbox_i[v0]
			u1 = sbox_i[v1]
			m0_guess = k0^u0
			m1_guess = k0^u1
			if (m0_guess == m0 and m1_guess == m1):
				print(k0, end = ' ')
		print('')


#k2 = 1, k1 = 13, k0 = 6
k0 = 6
k1 = 13
k2 = 1
ct = 'c1e5e5eae226bdbdc5ebc3ecc0b9cecdcdcec8c0b9c2cdc7bdccc3c8c0bdc5bd24e50e54e2ecee565420e02be2215c2020c85e552acc2a02c6e456e1c85b2b5d51bdecc3c0ee2de0e2ea27e2c1c4ebc3c9ce'

message = ''
for char in ct:
	c = int(char, 16)
	x = k2^c
	w = sbox_i[x]
	v = k1^w
	u = sbox_i[v]
	m = k0^u
	message += (str(hex(m))[-1])

print(f"The plaintext in hex encoded is: {message}")

print(f"The plaintext in ASCII is {bytearray.fromhex(message).decode()}")

