import galois
import keyExpansion
from sbox import SBOX
from auxiliary_functions import createState
from auxiliary_functions import createText

class Encryption:
    def __init__(self):
        return
    
    def cypher(plaintext, key):
        state = plaintext.copy()
        w = keyExpansion.keyExpasion(key)
        state = Encryption.AddRoundKeys(state, w[0])
        for round in range(1, 10):
            state = Encryption.SubBytes(state)
            state = Encryption.ShiftRows(state)
            state = Encryption.MixColumns(state)
            state = Encryption.AddRoundKeys(state, w[round])
        
        state = Encryption.SubBytes(state)
        state = Encryption.ShiftRows(state)
        state = Encryption.AddRoundKeys(state, w[10])
        return state

    def ShiftRows(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            thisrow=state[i].copy()
            for j in range(4):
                ret[i][j]=thisrow[(j+i)%4]
        return ret

    def SubBytes(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for r in range(4):
            for c in range(4):
                ret[r][c] = SBOX[state[r][c]]
        return ret
    
    def MixColumns(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            a = state[0][i]
            b = state[1][i]
            c = state[2][i]
            d = state[3][i]
            ret[0][i] = galois.gAdd(galois.gMult(a, 0x02), galois.gAdd(galois.gMult(b, 0x03), galois.gAdd(c, d)))
            ret[1][i] = galois.gAdd(galois.gMult(b, 0x02), galois.gAdd(galois.gMult(c, 0x03), galois.gAdd(a, d)))
            ret[2][i] = galois.gAdd(galois.gMult(c, 0x02), galois.gAdd(galois.gMult(d, 0x03), galois.gAdd(a, b)))
            ret[3][i] = galois.gAdd(galois.gMult(d, 0x02), galois.gAdd(galois.gMult(a, 0x03), galois.gAdd(b, c)))
        return ret

    def AddRoundKeys(state, key):
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

    def encrypt(text, key):
        all_states = createState(text)
        all_encrypted = []
        for state in all_states:
            all_encrypted.append(Encryption.cypher(state, key))
        cyphertext = createText(all_encrypted)
        return cyphertext
        
            