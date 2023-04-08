import galois
import keyExpansion
from inv_sbox import INV_SBOX

class Decryption:
    def __init__(self):
        return
    
    def InvSubBytes(state):        
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                ret[i][j] = INV_SBOX[state[i][j]]
        return ret
    
    def InvShiftRows(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            thisrow=state[i].copy()
            shift = 4-i
            for j in range(4):
                ret[i][j]=thisrow[(j+shift)%4]
        return ret
    
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

        
    def InvAddRoundKeys(state, key):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            auxKey = (key // ((1 << 32)**(3 - i))) % (1 << 32)
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

    def decypher(cyphertext, key):
        state = cyphertext
        w = keyExpansion.keyExpasion(key)
        state = Decryption.InvAddRoundKeys(state, w[10])
        for round in range(9, 0, -1):
            state = Decryption.InvShiftRows(state)
            state = Decryption.InvSubBytes(state)
            state = Decryption.InvAddRoundKeys(state, w[round])
            state = Decryption.InvMixColumns(state)

        state = Decryption.InvShiftRows(state)
        state = Decryption.InvSubBytes(state)
        state = Decryption.InvAddRoundKeys(state, w[0])

        return state