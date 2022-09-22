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

