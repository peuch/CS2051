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
    def InvAddRoundKeys():
        return 1