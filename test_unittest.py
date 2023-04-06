import galois
import unittest 
import encryption
import decryption

class TestGaloisField(unittest.TestCase):
    def test_add(self):
        self.assertEqual(galois.gAdd(0x57, 0x83), 0xd4)

    def test_mult(self):
        self.assertEqual(galois.gMult(0x02, 0x87), 0x15)
        self.assertEqual(galois.gMult(0x57, 0x13), 0xfe)
        self.assertEqual(galois.gMult(0x57, 0x83), 0xc1)
    
class TestAddRoundKeys(unittest.TestCase):
    def test_AddRoundKeys(self):
        key = 0x62636363626363636263636362636363
        state = [
            [0x59, 0xc2, 0xca, 0x4a],
            [0x1c, 0x86, 0xdd, 0x27],
            [0xee, 0x36, 0xaf, 0xdc],
            [0xa1, 0xd1, 0x02, 0xa2],
            ]
        expected = [
            [0x3b, 0xa0, 0xa8, 0x28],
            [0x7f, 0xe5, 0xbe, 0x44],
            [0x8d, 0x55, 0xcc, 0xbf],
            [0xc2, 0xb2, 0x61, 0xc1],
            ]
        
        self.assertEqual(encryption.Encryption.AddRoundKeys(state, key), expected)
    
    def test_TestInvAddRoundKeys(self):
        key = 0x62636363626363636263636362636363
        state = [
            [0x59, 0xc2, 0xca, 0x4a],
            [0x1c, 0x86, 0xdd, 0x27],
            [0xee, 0x36, 0xaf, 0xdc],
            [0xa1, 0xd1, 0x02, 0xa2],
            ]
        expected = [
            [0x3b, 0xa0, 0xa8, 0x28],
            [0x7f, 0xe5, 0xbe, 0x44],
            [0x8d, 0x55, 0xcc, 0xbf],
            [0xc2, 0xb2, 0x61, 0xc1],
            ]
        
        self.assertEqual(decryption.Decryption.InvAddRoundKeys(state, key), expected)

if __name__ == '__main__':
    unittest.main()