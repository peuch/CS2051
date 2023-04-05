import galois
import unittest
import encryption

class TestGaloisField(unittest.TestCase):
    def test_add(self):
        self.assertEqual(galois.gAdd(0x57, 0x83), 0xd4)

    def test_mult(self):
        self.assertEqual(galois.gMult(0x02, 0x87), 0x15)
        self.assertEqual(galois.gMult(0x57, 0x13), 0xfe)
        self.assertEqual(galois.gMult(0x57, 0x83), 0xc1)
    def test_shiftrows(self):
        state = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                state[i][j]=i*4+j
        expected=[
            [0,1,2,3],
            [5,6,7,4],
            [10,11,8,9],
            [15,12,13,14]
        ]
        self.assertEqual(encryption.Encryption.ShiftRows(state), expected)
        
if __name__ == '__main__':
    unittest.main()