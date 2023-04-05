class Encryption:
    def __init__(self):
        return
    def SubBytes(self):
        return 1
    def ShiftRows(state):
        ret = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            thisrow=state[i].copy()
            for j in range(4):
                ret[i][j]=thisrow[(j+i)%4]
        return ret
    def MixColumns(self):
        return 1
    def AddRoundKeys(self):
        return 1