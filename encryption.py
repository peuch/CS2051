class Encryption:
    def __init__(self):
        return
    def SubBytes(state: [int][int], mapping: [int][int]):
        for r in range(key):
            for c in range(key[r]):
                item: int = key[r][c]
                cipher_row: int = item / 16
                cipher_col: int = item % 16
                key[r][c] = ciphertext[cipher_row][cipher_col]
        return key
    def ShiftRows(self):
        return 1
    def MixColumns(self):
        return 1
    def AddRoundKeys(self):
        return 1