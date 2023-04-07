class Encryption:
    def __init__(self):
        return
    def SubBytes(state: [int][int], mapping: [int][int]):
        for r in range(mapping):
            for c in range(mapping[r]):
                item: int = mapping[r][c]
                cipher_row: int = item / 16
                cipher_col: int = item % 16
                mapping[r][c] = state[cipher_row][cipher_col]
        return mapping
    def ShiftRows(self):
        return 1
    def MixColumns(self):
        return 1
    def AddRoundKeys(self):
        return 1