import galois

class Encryption:
    def __init__(self):
        return
    
    def createState(text):
        all_states = []
        #hex_message = text.encode("utf-8").hex()
        i=0
        finished=False
        while (i<len(text) and not finished):
            #finished filling previous array, still more left to message
            state = [[0 for _ in range(4)] for _ in range(4)]
            for col in range(4):
                for row in range(4):
                    if (i+1<=len(text)):
                        #we haven't reached end of string yet
                        state[row][col] = hex(ord(text[i:i+1])) #gives hex value
                        i=i+1
                    else:
                        finished=True
                        break
            all_states.append(state)
        return all_states
    
    def cipher(input, word):
        output = []
        for state in input:
            state = Encryption.AddRoundKeys(state, word[0, 3])
            for round in range(1, 10-1):
                state = Encryption.SubBytes(state)
                state = Encryption.ShiftRows(state)
                state = Encryption.MixColumns(state)
                state = Encryption.AddRoundKeys(state, word[round*4, (round+1)*4-1])
            
            state = Encryption.SubBytes(state)
            state = Encryption.ShiftRows(state)
            state = Encryption.AddRoundKeys(state, word[10*4, (10+1)*4-1])
            output.append(state)
        return output

        

    def ShiftRows(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            thisrow=state[i].copy()
            for j in range(4):
                ret[i][j]=thisrow[(j+i)%4]
        return ret

    def SubBytes(state, mapping):
        for r in range(mapping):
            for c in range(mapping[r]):
                item: int = mapping[r][c]
                cipher_row: int = item / 16
                cipher_col: int = item % 16
                mapping[r][c] = state[cipher_row][cipher_col]
        return mapping
    
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
    
