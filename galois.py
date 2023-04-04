
def gAdd(a : bytes, b : bytes):
    return a ^ b

def gMult(a : bytes, b : bytes):
    p = bytes(0)

    for _ in range(8):
        if (b & 1) != 0:
            p ^= a

        hi_bit_set = (a & 0x80) != 0
        a <<= 1
        if hi_bit_set:
            a ^= 0x1B
        b >>= 1

    return p