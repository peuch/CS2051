class Decryption:
    def __init__(self):
        return
    def InvSubBytes():
        return 1
    def InvShiftRows(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            thisrow=state[i].copy()
            shift = 4-i
            for j in range(4):
                ret[i][j]=thisrow[(j+shift)%4]
        return ret
        return 1
    def InvMixColumns():
        return 1
    def InvAddRoundKeys(state, key):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            auxKey = (key // ((1 << 32)**i)) % (1 << 32)

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