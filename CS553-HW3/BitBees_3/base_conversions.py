def bin2hex(bin):
    """
    Convert binary to hexadecimal.
    """
    bin = str(bin)
    return str(hex(int(bin, 2)))[2:]

def hex2bin(hex, length=16):
    """
    Convert hexadecimal to binary.
    """
    hex = str(hex)
    return '0'*(length - len(str(bin(int(hex, 16))[2:]))) + str(bin(int(hex, 16))[2:])

def dec2bin(dec, length=4):
    """
    Convert decimal to binary.
    """
    dec = str(dec)
    return '0'*(length - len(str(bin(int(dec))[2:]))) +str(bin(int(dec))[2:])

def bin2dec(bin):
    """
    Convert binary to decimal.
    """
    bin = str(bin)
    return str(int(bin, 2))

def hex2dec(hex):
    """
    Convert hexadecimal to decimal.
    """
    hex = str(hex)
    return str(int(hex, 16))

def dec2hex(dec):
    """
    Convert decimal to hexadecimal.
    """
    dec = str(dec)
    return str(hex(int(dec))[2:])

