import random

def sbox():
	random_sbox = {}

	for i in range(16):
		while True:
			x = random.randint(0, 15)
			if x not in random_sbox.values():
				random_sbox[i] = x
				break
	return random_sbox

# print(random_sbox)
# print(sbox())