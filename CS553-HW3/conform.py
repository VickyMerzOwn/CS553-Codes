from base_conversions import bin2dec, bin2hex, dec2bin, hex2bin
from sypher004 import Sypher004


k0 = hex2bin("5b92")
k1 = hex2bin("064b")
k2 = hex2bin("1e03")
k3 = hex2bin("a55f")
k4 = hex2bin("ecbd")
k5 = hex2bin("7ca5")

#print("hello")
# print(type(k0))

sypher_m0 = Sypher004(k0, k1, k2, k3, k4, k5)
sypher_m1 = Sypher004(k0, k1, k2, k3, k4, k5)
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
conforming = 0

for i in range(16):
    for j in range(16):
        for k in range(16):
            for l in range(16):
                m0 = (dec2bin(i), dec2bin(j), dec2bin(k), dec2bin(l))
                m1 = (dec2bin(i), dec2bin(j), dec2bin(k ^ 2), dec2bin(l))
                # print(m0, m1)
                sypher_m0.state = m0
                sypher_m1.state = m1

                sypher_m0.ENC(k0)
                sypher_m1.ENC(k0)

                layer0_m0 = int(
                    bin2dec(
                        sypher_m0.state[0]
                        + sypher_m0.state[1]
                        + sypher_m0.state[2]
                        + sypher_m0.state[3]
                    )
                )
                layer0_m1 = int(
                    bin2dec(
                        sypher_m1.state[0]
                        + sypher_m1.state[1]
                        + sypher_m1.state[2]
                        + sypher_m1.state[3]
                    )
                )

                if layer0_m0 ^ layer0_m1 == 2:
                    c1 += 1
                    sypher_m0.ENC(k1)
                    sypher_m1.ENC(k1)

                    layer1_m0 = int(
                        bin2dec(
                            sypher_m0.state[0]
                            + sypher_m0.state[1]
                            + sypher_m0.state[2]
                            + sypher_m0.state[3]
                        )
                    )
                    layer1_m1 = int(
                        bin2dec(
                            sypher_m1.state[0]
                            + sypher_m1.state[1]
                            + sypher_m1.state[2]
                            + sypher_m1.state[3]
                        )
                    )

                    if layer1_m0 ^ layer1_m1 == 2:
                        c2 += 1
                        sypher_m0.ENC(k2)
                        sypher_m1.ENC(k2)

                        layer2_m0 = int(
                            bin2dec(
                                sypher_m0.state[0]
                                + sypher_m0.state[1]
                                + sypher_m0.state[2]
                                + sypher_m0.state[3]
                            )
                        )
                        layer2_m1 = int(
                            bin2dec(
                                sypher_m1.state[0]
                                + sypher_m1.state[1]
                                + sypher_m1.state[2]
                                + sypher_m1.state[3]
                            )
                        )

                        if layer2_m0 ^ layer2_m1 == 2:
                            c3 += 1
                            sypher_m0.ENC(k3)
                            sypher_m1.ENC(k3)

                            layer3_m0 = int(
                                bin2dec(
                                    sypher_m0.state[0]
                                    + sypher_m0.state[1]
                                    + sypher_m0.state[2]
                                    + sypher_m0.state[3]
                                )
                            )
                            layer3_m1 = int(
                                bin2dec(
                                    sypher_m1.state[0]
                                    + sypher_m1.state[1]
                                    + sypher_m1.state[2]
                                    + sypher_m1.state[3]
                                )
                            )

                            if layer3_m0 ^ layer3_m1 == 2:
                                c4 += 1
                                sypher_m0.ENC(k4)
                                sypher_m1.ENC(k4)

                                layer4_m0 = int(
                                    bin2dec(
                                        sypher_m0.state[0]
                                        + sypher_m0.state[1]
                                        + sypher_m0.state[2]
                                        + sypher_m0.state[3]
                                    )
                                )
                                layer4_m1 = int(
                                    bin2dec(
                                        sypher_m1.state[0]
                                        + sypher_m1.state[1]
                                        + sypher_m1.state[2]
                                        + sypher_m1.state[3]
                                    )
                                )

                                if layer4_m0 ^ layer4_m1 == 2:
                                    c5 += 1
                                    sypher_m0.XOR(k5)
                                    sypher_m1.XOR(k5)

                                    layer5_m0 = int(
                                        bin2dec(
                                            sypher_m0.state[0]
                                            + sypher_m0.state[1]
                                            + sypher_m0.state[2]
                                            + sypher_m0.state[3]
                                        )
                                    )
                                    layer5_m1 = int(
                                        bin2dec(
                                            sypher_m1.state[0]
                                            + sypher_m1.state[1]
                                            + sypher_m1.state[2]
                                            + sypher_m1.state[3]
                                        )
                                    )

                                    if layer5_m0 ^ layer5_m1 == 2:
                                        conforming += 1

print(conforming)
print(c1, c2, c3, c4, c5)
