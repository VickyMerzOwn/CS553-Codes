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
	3:1,
	13:11,
	8:12,
	10:13,
	9:14,
	11:15
}

suitable_mc = []
for i in range(16):
	if (i^dict_oracle[i] == 15):
		suitable_mc.append((i, dict_oracle[i]))


suitable_u = []
for i in range(0, 16):
	suitable_u.append((i, i^15))

suitable_v = []

for i in suitable_u:
	v0 = sbox[i[0]]
	v1 = sbox[i[1]]
	if (v0^v1 == 13):
		suitable_v.append((v0, v1))

counters = [0]*16
wk_pairs = dict()

for k2 in range(16):
	w_lst = []
	for m, c in suitable_pairs_2:
		x = k2^c
		w = sbox_i[x]
		w_lst.append(w)

	for w0 in w_lst:
		for w1 in w_lst:
			if (w0^w1 == 13):
				counters[k2] += 1

max_occurance = max(counters)
k2_lst = []
for i in range(len(counters)):
	if (counters[i] == max(counters)):
		print(f'The value of k2 is most likely {i} with total of {counters[i]} occurances of v0, v1 difference of 13')
		k2_lst.append(i)


k1_ctr = [0]*16

# for i in range(16)
