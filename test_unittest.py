import random
import galois
import unittest
import encryption
import decryption
import unittest 
import keyExpansion

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
    def test_invshiftrows(self):
        shifted=[
            [0,1,2,3],
            [5,6,7,4],
            [10,11,8,9],
            [15,12,13,14]
        ]
        expected=[
            [0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,15]
        ]
        self.assertEqual(decryption.Decryption.InvShiftRows(shifted), expected)

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
        
class TestKeyExpansion(unittest.TestCase):
    def test_keyExpansion_1(self):
        key = 0x5468617473206D79204B756E67204675

        w = keyExpansion.keyExpasion(key)
        expected = [
            0x5468617473206D79204B756E67204675,
            0xE232FCF191129188B159E4E6D679A293,
            0x56082007C71AB18F76435569A03AF7FA,
            0xD2600DE7157ABC686339E901C3031EFB,
            0xA11202C9B468BEA1D75157A01452495B,
            0xB1293B3305418592D210D232C6429B69,
            0xBD3DC287B87C47156A6C9527AC2E0E4E,
            0xCC96ED1674EAAA031E863F24B2A8316A,
            0x8E51EF21FABB4522E43D7A0656954B6C,
            0xBFE2BF904559FAB2A16480B4F7F1CBD8,
            0x28FDDEF86DA4244ACCC0A4FE3B316F26,
        ]

        self.assertEqual(w, expected)

    def test_keyExpansion_2(self):
        key = 0x00000000000000000000000000000000

        w = keyExpansion.keyExpasion(key)
        expected = [
            0x00000000000000000000000000000000,
            0x62636363626363636263636362636363,
            0x9b9898c9f9fbfbaa9b9898c9f9fbfbaa,
            0x90973450696ccffaf2f457330b0fac99,
            0xee06da7b876a1581759e42b27e91ee2b,
            0x7f2e2b88f8443e098dda7cbbf34b9290,
            0xec614b851425758c99ff09376ab49ba7,
            0x217517873550620bacaf6b3cc61bf09b,
            0x0ef903333ba9613897060a04511dfa9f,
            0xb1d4d8e28a7db9da1d7bb3de4c664941,
            0xb4ef5bcb3e92e21123e951cf6f8f188e
        ]

    def test_keyExpansion_3(self):
        key = 0x706564726f7265657365646176646920

        w = keyExpansion.keyExpasion(key)
        expected = [
            0x706564726f7265657365646176646920,
            0x329cd34a5deeb62f2e8bd24e58efbb6e,
            0xef764c20b298fa0f9c132841c4fc932f,
            0x5baa593ce932a33375218b72b1dd185d,
            0x920715f47b35b6c70e143db5bfc925e8,
            0x5f388efc240d383b2a19058e95d02066,
            0x0f8fbdd62b8285ed019b8063944ba005,
            0xfc6fd6f4d7ed5319d676d37a423d737f,
            0x5be004d88c0d57c15a7b84bb1846f7c4,
            0x1a88187596854fb4ccfecb0fd4b83ccb,
            0x4063073dd6e648891a188386cea0bf4d
        ]

        self.assertEqual(w, expected)
        
if __name__ == '__main__':
    unittest.main()