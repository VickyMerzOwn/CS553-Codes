from sypher004 import myCharacteristicSypher004


init = ['0000','0000','0000','0010']
print(f"Initial Difference: {init}")
sypher = myCharacteristicSypher004(init)

sypher.round()
sypher.round()
sypher.round()
sypher.round()
print(f"Final Probablity: {sypher.get_probablity()}")