from sbox import SBOX
from galois import gMult

def keyExpasion(key):
    w = [0 for _ in range(11)]  # 10 rounds -> 11 expansions

    w[0] = key

    rcon = 1

    for i in range(1, 11):
        temp = w[i - 1] % (1 << 0x20)

        if i != 1: rcon = gMult(rcon, 0x02)

        # RotWord

        a2 = temp % (1 << (0x08))
        temp //= (1 << (0x08))
        a1 = temp % (1 << (0x08))
        temp //= (1 << (0x08))
        a0 = temp % (1 << (0x08))
        temp //= (1 << (0x08))
        a3 = temp % (1 << (0x08))
    
        a0 = SBOX[a0]
        a1 = SBOX[a1]
        a2 = SBOX[a2]
        a3 = SBOX[a3]
        
        temp = w[i - 1]
        
        aux1 = ((temp >> 0x60) % (1 << 0x20))
        aux2 = (((a0 << 0x18) | (a1 << 0x10)  | (a2 << 0x08) | a3) ^ (rcon << 0x18))
        
        w0 = ((temp >> 0x60) % (1 << 0x20)) ^ (((a0 << 0x18) | (a1 << 0x10)  | (a2 << 0x08) | a3) ^ (rcon << 0x18))
        w1 = ((temp >> 0x40) % (1 << 0x20)) ^ w0
        w2 = ((temp >> 0x20) % (1 << 0x20)) ^ w1
        w3 = ((temp >> 0x00) % (1 << 0x20)) ^ w2

        w[i] = (w0 << 0x60) + (w1 << 0x40) + (w2 << 0x20) + w3

    return w
