\ Model MILP_Sypher004_cryptANALysis
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  a00 + a01 + a02 + a03 + a10 + a11 + a12 + a13 + a20 + a21 + a22 + a23
   + a30 + a31 + a32 + a33 + a40 + a41 + a42 + a43
Subject To
 R0: x00 - a00 <= 0
 R1: x01 - a00 <= 0
 R2: x02 - a00 <= 0
 R3: x03 - a00 <= 0
 R4: x04 - a01 <= 0
 R5: x05 - a01 <= 0
 R6: x06 - a01 <= 0
 R7: x07 - a01 <= 0
 R8: x08 - a02 <= 0
 R9: x09 - a02 <= 0
 R10: x0a - a02 <= 0
 R11: x0b - a02 <= 0
 R12: x0c - a03 <= 0
 R13: x0d - a03 <= 0
 R14: x0e - a03 <= 0
 R15: x0f - a03 <= 0
 R16: x1e - a10 <= 0
 R17: x18 - a10 <= 0
 R18: x1b - a10 <= 0
 R19: x1c - a10 <= 0
 R20: x1f - a11 <= 0
 R21: x1d - a11 <= 0
 R22: x12 - a11 <= 0
 R23: x10 - a11 <= 0
 R24: x11 - a12 <= 0
 R25: x14 - a12 <= 0
 R26: x15 - a12 <= 0
 R27: x17 - a12 <= 0
 R28: x13 - a13 <= 0
 R29: x16 - a13 <= 0
 R30: x1a - a13 <= 0
 R31: x19 - a13 <= 0
 R32: x2e - a20 <= 0
 R33: x28 - a20 <= 0
 R34: x2b - a20 <= 0
 R35: x2c - a20 <= 0
 R36: x2f - a21 <= 0
 R37: x2d - a21 <= 0
 R38: x22 - a21 <= 0
 R39: x20 - a21 <= 0
 R40: x21 - a22 <= 0
 R41: x24 - a22 <= 0
 R42: x25 - a22 <= 0
 R43: x27 - a22 <= 0
 R44: x23 - a23 <= 0
 R45: x26 - a23 <= 0
 R46: x2a - a23 <= 0
 R47: x29 - a23 <= 0
 R48: x3e - a30 <= 0
 R49: x38 - a30 <= 0
 R50: x3b - a30 <= 0
 R51: x3c - a30 <= 0
 R52: x3f - a31 <= 0
 R53: x3d - a31 <= 0
 R54: x32 - a31 <= 0
 R55: x30 - a31 <= 0
 R56: x31 - a32 <= 0
 R57: x34 - a32 <= 0
 R58: x35 - a32 <= 0
 R59: x37 - a32 <= 0
 R60: x33 - a33 <= 0
 R61: x36 - a33 <= 0
 R62: x3a - a33 <= 0
 R63: x39 - a33 <= 0
 R64: x4e - a40 <= 0
 R65: x48 - a40 <= 0
 R66: x4b - a40 <= 0
 R67: x4c - a40 <= 0
 R68: x4f - a41 <= 0
 R69: x4d - a41 <= 0
 R70: x42 - a41 <= 0
 R71: x40 - a41 <= 0
 R72: x41 - a42 <= 0
 R73: x44 - a42 <= 0
 R74: x45 - a42 <= 0
 R75: x47 - a42 <= 0
 R76: x43 - a43 <= 0
 R77: x46 - a43 <= 0
 R78: x4a - a43 <= 0
 R79: x49 - a43 <= 0
 R80: x00 + x01 + x02 + x03 - a00 >= 0
 R81: x04 + x05 + x06 + x07 - a01 >= 0
 R82: x08 + x09 + x0a + x0b - a02 >= 0
 R83: x0c + x0d + x0e + x0f - a03 >= 0
 R84: x18 + x1b + x1c + x1e - a10 >= 0
 R85: x10 + x12 + x1d + x1f - a11 >= 0
 R86: x11 + x14 + x15 + x17 - a12 >= 0
 R87: x13 + x16 + x19 + x1a - a13 >= 0
 R88: x28 + x2b + x2c + x2e - a20 >= 0
 R89: x20 + x22 + x2d + x2f - a21 >= 0
 R90: x21 + x24 + x25 + x27 - a22 >= 0
 R91: x23 + x26 + x29 + x2a - a23 >= 0
 R92: x38 + x3b + x3c + x3e - a30 >= 0
 R93: x30 + x32 + x3d + x3f - a31 >= 0
 R94: x31 + x34 + x35 + x37 - a32 >= 0
 R95: x33 + x36 + x39 + x3a - a33 >= 0
 R96: x48 + x4b + x4c + x4e - a40 >= 0
 R97: x40 + x42 + x4d + x4f - a41 >= 0
 R98: x41 + x44 + x45 + x47 - a42 >= 0
 R99: x43 + x46 + x49 + x4a - a43 >= 0
 R100: 4 x00 + 4 x01 + 4 x02 + 4 x03 - x10 - x11 - x12 - x13 >= 0
 R101: - x00 - x01 - x02 - x03 + 4 x10 + 4 x11 + 4 x12 + 4 x13 >= 0
 R102: 4 x04 + 4 x05 + 4 x06 + 4 x07 - x14 - x15 - x16 - x17 >= 0
 R103: - x04 - x05 - x06 - x07 + 4 x14 + 4 x15 + 4 x16 + 4 x17 >= 0
 R104: 4 x08 + 4 x09 + 4 x0a + 4 x0b - x18 - x19 - x1a - x1b >= 0
 R105: - x08 - x09 - x0a - x0b + 4 x18 + 4 x19 + 4 x1a + 4 x1b >= 0
 R106: 4 x0c + 4 x0d + 4 x0e + 4 x0f - x1c - x1d - x1e - x1f >= 0
 R107: - x0c - x0d - x0e - x0f + 4 x1c + 4 x1d + 4 x1e + 4 x1f >= 0
 R108: 4 x18 + 4 x1b + 4 x1c + 4 x1e - x20 - x21 - x22 - x23 >= 0
 R109: - x18 - x1b - x1c - x1e + 4 x20 + 4 x21 + 4 x22 + 4 x23 >= 0
 R110: 4 x10 + 4 x12 + 4 x1d + 4 x1f - x24 - x25 - x26 - x27 >= 0
 R111: - x10 - x12 - x1d - x1f + 4 x24 + 4 x25 + 4 x26 + 4 x27 >= 0
 R112: 4 x11 + 4 x14 + 4 x15 + 4 x17 - x28 - x29 - x2a - x2b >= 0
 R113: - x11 - x14 - x15 - x17 + 4 x28 + 4 x29 + 4 x2a + 4 x2b >= 0
 R114: 4 x13 + 4 x16 + 4 x19 + 4 x1a - x2c - x2d - x2e - x2f >= 0
 R115: - x13 - x16 - x19 - x1a + 4 x2c + 4 x2d + 4 x2e + 4 x2f >= 0
 R116: 4 x28 + 4 x2b + 4 x2c + 4 x2e - x30 - x31 - x32 - x33 >= 0
 R117: - x28 - x2b - x2c - x2e + 4 x30 + 4 x31 + 4 x32 + 4 x33 >= 0
 R118: 4 x20 + 4 x22 + 4 x2d + 4 x2f - x34 - x35 - x36 - x37 >= 0
 R119: - x20 - x22 - x2d - x2f + 4 x34 + 4 x35 + 4 x36 + 4 x37 >= 0
 R120: 4 x21 + 4 x24 + 4 x25 + 4 x27 - x38 - x39 - x3a - x3b >= 0
 R121: - x21 - x24 - x25 - x27 + 4 x38 + 4 x39 + 4 x3a + 4 x3b >= 0
 R122: 4 x23 + 4 x26 + 4 x29 + 4 x2a - x3c - x3d - x3e - x3f >= 0
 R123: - x23 - x26 - x29 - x2a + 4 x3c + 4 x3d + 4 x3e + 4 x3f >= 0
 R124: 4 x38 + 4 x3b + 4 x3c + 4 x3e - x40 - x41 - x42 - x43 >= 0
 R125: - x38 - x3b - x3c - x3e + 4 x40 + 4 x41 + 4 x42 + 4 x43 >= 0
 R126: 4 x30 + 4 x32 + 4 x3d + 4 x3f - x44 - x45 - x46 - x47 >= 0
 R127: - x30 - x32 - x3d - x3f + 4 x44 + 4 x45 + 4 x46 + 4 x47 >= 0
 R128: 4 x31 + 4 x34 + 4 x35 + 4 x37 - x48 - x49 - x4a - x4b >= 0
 R129: - x31 - x34 - x35 - x37 + 4 x48 + 4 x49 + 4 x4a + 4 x4b >= 0
 R130: 4 x33 + 4 x36 + 4 x39 + 4 x3a - x4c - x4d - x4e - x4f >= 0
 R131: - x33 - x36 - x39 - x3a + 4 x4c + 4 x4d + 4 x4e + 4 x4f >= 0
 R132: 4 x48 + 4 x4b + 4 x4c + 4 x4e - x50 - x51 - x52 - x53 >= 0
 R133: - x48 - x4b - x4c - x4e + 4 x50 + 4 x51 + 4 x52 + 4 x53 >= 0
 R134: 4 x40 + 4 x42 + 4 x4d + 4 x4f - x54 - x55 - x56 - x57 >= 0
 R135: - x40 - x42 - x4d - x4f + 4 x54 + 4 x55 + 4 x56 + 4 x57 >= 0
 R136: 4 x41 + 4 x44 + 4 x45 + 4 x47 - x58 - x59 - x5a - x5b >= 0
 R137: - x41 - x44 - x45 - x47 + 4 x58 + 4 x59 + 4 x5a + 4 x5b >= 0
 R138: 4 x43 + 4 x46 + 4 x49 + 4 x4a - x5c - x5d - x5e - x5f >= 0
 R139: - x43 - x46 - x49 - x4a + 4 x5c + 4 x5d + 4 x5e + 4 x5f >= 0
 R140: a00 + a01 + a02 + a03 + a10 + a11 + a12 + a13 + a20 + a21 + a22
   + a23 + a30 + a31 + a32 + a33 + a40 + a41 + a42 + a43 >= 1
Bounds
Binaries
 x00 x01 x02 x03 x04 x05 x06 x07 x08 x09 x0a x0b x0c x0d x0e x0f x10 x11
 x12 x13 x14 x15 x16 x17 x18 x19 x1a x1b x1c x1d x1e x1f x20 x21 x22 x23
 x24 x25 x26 x27 x28 x29 x2a x2b x2c x2d x2e x2f x30 x31 x32 x33 x34 x35
 x36 x37 x38 x39 x3a x3b x3c x3d x3e x3f x40 x41 x42 x43 x44 x45 x46 x47
 x48 x49 x4a x4b x4c x4d x4e x4f x50 x51 x52 x53 x54 x55 x56 x57 x58 x59
 x5a x5b x5c x5d x5e x5f a00 a01 a02 a03 a10 a11 a12 a13 a20 a21 a22 a23
 a30 a31 a32 a33 a40 a41 a42 a43
End
