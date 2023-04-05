class Encryption:
    def __init__(self):
        return
    def SubBytes(self):
        return 1
    def ShiftRows(self):
        return 1
    def MixColumns(self):
        return 1
    def AddRoundKeys(state, key):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            auxKey = (key // (256**i)) % 256

            a = state[0][i]
            b = state[1][i]
            c = state[2][i]
            d = state[3][i]

            aux = a * 256**3 + b * 256**2 + c * 256 + d

            aux ^= auxKey

            ret[3][i] = aux % 256
            aux //= 256
            ret[2][i] = aux % 256
            aux //= 256
            ret[1][i] = aux % 256
            aux //= 256
            ret[0][i] = aux % 256

        return ret