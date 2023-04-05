import galois

class Decryption:
    def __init__(self):
        return
    def InvSubBytes():
        return 1
    def InvShiftRows():
        return 1
    
    def InvMixColumns(state):
        print(state)
        for i in range(4):
            a = state[0][i]
            b = state[1][i]
            c = state[2][i]
            d = state[3][i]
            state[0][i] = galois.gAdd(galois.gMult(a, 0x0e), galois.gAdd(galois.gMult(b, 0x0b), galois.gAdd(galois.gMult(c, 0x0d), galois.gMult(d, 0x09))))
            state[1][i] = galois.gAdd(galois.gMult(a, 0x09), galois.gAdd(galois.gMult(b, 0x0e), galois.gAdd(galois.gMult(c, 0x0b), galois.gMult(d, 0x0d))))
            state[2][i] = galois.gAdd(galois.gMult(a, 0x0d), galois.gAdd(galois.gMult(b, 0x09), galois.gAdd(galois.gMult(c, 0x0e), galois.gMult(d, 0x0b))))
            state[3][i] = galois.gAdd(galois.gMult(a, 0x0b), galois.gAdd(galois.gMult(b, 0x0d), galois.gAdd(galois.gMult(c, 0x09), galois.gMult(d, 0x0e))))
        return state
    
    def InvAddRoundKeys():
        return 1