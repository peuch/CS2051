import galois

class Decryption:
    def __init__(self):
        return
    def InvSubBytes():
        return 1
    def InvShiftRows():
        return 1
    
    def InvMixColumns(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            a = state[0][i]
            b = state[1][i]
            c = state[2][i]
            d = state[3][i]
            ret[0][i] = galois.gAdd(galois.gMult(a, 0x0e), galois.gAdd(galois.gMult(b, 0x0b), galois.gAdd(galois.gMult(c, 0x0d), galois.gMult(d, 0x09))))
            ret[1][i] = galois.gAdd(galois.gMult(a, 0x09), galois.gAdd(galois.gMult(b, 0x0e), galois.gAdd(galois.gMult(c, 0x0b), galois.gMult(d, 0x0d))))
            ret[2][i] = galois.gAdd(galois.gMult(a, 0x0d), galois.gAdd(galois.gMult(b, 0x09), galois.gAdd(galois.gMult(c, 0x0e), galois.gMult(d, 0x0b))))
            ret[3][i] = galois.gAdd(galois.gMult(a, 0x0b), galois.gAdd(galois.gMult(b, 0x0d), galois.gAdd(galois.gMult(c, 0x09), galois.gMult(d, 0x0e))))
        return ret
    
    def InvAddRoundKeys():
        return 1