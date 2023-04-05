import random
import galois
import encryption
import decryption
import unittest 

class TestGaloisField(unittest.TestCase):
    def test_add(self):
        self.assertEqual(galois.gAdd(0x57, 0x83), 0xd4)

    def test_mult(self):
        self.assertEqual(galois.gMult(0x02, 0x87), 0x15)
        self.assertEqual(galois.gMult(0x57, 0x13), 0xfe)
        self.assertEqual(galois.gMult(0x57, 0x83), 0xc1)
    
class TestMixColumns(unittest.TestCase):
    def test_MixColumns_WikipediaTest(self):
        state = [
            [0xdb, 0xf2, 0x01, 0xc6],
            [0x13, 0x0a, 0x01, 0xc6],
            [0x53, 0x22, 0x01, 0xc6],
            [0x45, 0x5c, 0x01, 0xc6]
        ]
        expected = [
            [0x8e, 0x9f, 0x01, 0xc6],
            [0x4d, 0xdc, 0x01, 0xc6],
            [0xa1, 0x58, 0x01, 0xc6],
            [0xbc, 0x9d, 0x01, 0xc6]
        ]
        self.assertEqual(encryption.Encryption.MixColumns(state), expected)

    def test_InvMixColumns_WikipediaTest(self):
        state = [
            [0x8e, 0x9f, 0x01, 0xc6],
            [0x4d, 0xdc, 0x01, 0xc6],
            [0xa1, 0x58, 0x01, 0xc6],
            [0xbc, 0x9d, 0x01, 0xc6]
        ]
        expected = [
            [0xdb, 0xf2, 0x01, 0xc6],
            [0x13, 0x0a, 0x01, 0xc6],
            [0x53, 0x22, 0x01, 0xc6],
            [0x45, 0x5c, 0x01, 0xc6]
        ]
        self.assertEqual(decryption.Decryption.InvMixColumns(state), expected)
    
    def test_both_with_random(self):
        for _ in range(1000):
            state = [[random.randint(0, 255) for _ in range(4)] for _ in range(4)]
            encrypted = encryption.Encryption.MixColumns(state)
            decrypted = decryption.Decryption.InvMixColumns(encrypted)
            self.assertEqual(decrypted, state)


if __name__ == '__main__':
    unittest.main()