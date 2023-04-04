
def gAdd(a : int, b : int):
    return a ^ b

def gMult(a : int, b : int):
    p = 0
    for _ in range(8):
        if (b & 1) != 0:
            p = gAdd(p, a)

        hi_bit_set = (a & (1 << 7)) != 0
        a <<= 1
        if hi_bit_set:
            a ^= 0x011B
        b >>= 1

    return p