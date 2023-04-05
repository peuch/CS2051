import galois

class Encryption:
    def __init__(self):
        return
    def SubBytes(self):
        return 1
    def ShiftRows(self):
        return 1
    
    def MixColumns(state):
        for i in range(4):
            a = state[0, i]
            b = state[1, i]
            c = state[2, i]
            d = state[3, i]
            state[0, i] = galois.gAdd(galois.gMult(a, 0x02), galois.gAdd(galois.gMult(b, 0x03), galois.gAdd(c, d)))
            state[1, i] = galois.gAdd(galois.gMult(b, 0x02), galois.gAdd(galois.gMult(c, 0x03), galois.gAdd(a, d)))
            state[2, i] = galois.gAdd(galois.gMult(c, 0x02), galois.gAdd(galois.gMult(d, 0x03), galois.gAdd(a, b)))
            state[3, i] = galois.gAdd(galois.gMult(d, 0x02), galois.gAdd(galois.gMult(a, 0x03), galois.gAdd(b, c)))
        return state
    
    def AddRoundKeys(self):
        return 1