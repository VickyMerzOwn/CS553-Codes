import pprint
# from sbox import sbox

# sbox = sbox()
# inverse_sbox = {}
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

inverse_sbox = {
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
for a in sbox:
	inverse_sbox[sbox[a]] = a

ddt = []

for input_difference in range(16):
	u1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]
	u2 = [i^input_difference for i in u1]

	v1 = [sbox[u] for u in u1]
	v2 = [sbox[u] for u in u2]

	output_difference_list = [0] * 16
	# print(output_difference_list)
	for i in range(16):
		output_difference_list[v1[i]^v2[i]] += 1

	ddt.append(output_difference_list)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(ddt)