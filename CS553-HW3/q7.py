from sypher004 import myCharacteristicSypher004

sypher = myCharacteristicSypher004(['0000','0000','0000','0010'])

sypher.round()
sypher.round()
sypher.round()
sypher.round()
print(f"Final Probablity: {sypher.get_probablity()}")