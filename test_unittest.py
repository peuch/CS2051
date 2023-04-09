import random
import string
import galois
import unittest
import encryption
import decryption
import unittest 
import keyExpansion
from auxiliary_functions import createState

class TestGaloisField(unittest.TestCase):
    def test_add(self):
        self.assertEqual(galois.gAdd(0x57, 0x83), 0xd4)

    def test_mult(self):
        self.assertEqual(galois.gMult(0x02, 0x87), 0x15)
        self.assertEqual(galois.gMult(0x57, 0x13), 0xfe)
        self.assertEqual(galois.gMult(0x57, 0x83), 0xc1)

class TestShiftRows(unittest.TestCase):
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

class Test_CreateState(unittest.TestCase):
    def test_shortPlaintext(self):
        string = "abcdef"
        expected = [
            [
                [0x61, 0x65, 0, 0],
                [0x62, 0x66, 0, 0],
                [0x63, 0, 0, 0],
                [0x64, 0, 0, 0]
            ]
        ]
        self.assertEqual(createState(string), expected)
        
class TestDecypher(unittest.TestCase):
    def test_individual(self):
        key = 0x2b7e151628aed2a6abf7158809cf4f3c
        w = keyExpansion.keyExpasion(key)
        expected_w = [
            0x2b7e151628aed2a6abf7158809cf4f3c,
            0xa0fafe1788542cb123a339392a6c7605,
            0xf2c295f27a96b9435935807a7359f67f,
            0x3d80477d4716fe3e1e237e446d7a883b,
            0xef44a541a8525b7fb671253bdb0bad00,
            0xd4d1c6f87c839d87caf2b8bc11f915bc,
            0x6d88a37a110b3efddbf98641ca0093fd,
            0x4e54f70e5f5fc9f384a64fb24ea6dc4f,
            0xead27321b58dbad2312bf5607f8d292f,
            0xac7766f319fadc2128d12941575c006e,
            0xd014f9a8c9ee2589e13f0cc8b6630ca6
        ]
        
        self.assertEqual(w, expected_w)

        state = [   
            [0xa4, 0x68, 0x6b, 0x02],        
            [0x9c, 0x9f, 0x5b, 0x6a],
            [0x7f, 0x35, 0xea, 0x50],
            [0xf2, 0x2b, 0x43, 0x49]
        ]

        expected_round = [ 
            [0x04, 0xe0, 0x48, 0x28],
            [0x66, 0xcb, 0xf8, 0x06],
            [0x81, 0x19, 0xd3, 0x26],
            [0xe5, 0x9a, 0x7a, 0x4c]
        ]
        
        state = decryption.Decryption.InvAddRoundKeys(state, w[1])

        self.assertEqual(state, expected_round)

        expected_mix = [ 
            [0xd4, 0xe0, 0xb8, 0x1e],
            [0xbf, 0xb4, 0x41, 0x27],
            [0x5d, 0x52, 0x11, 0x98],
            [0x30, 0xae, 0xf1, 0xe5]
        ]
        
        state = decryption.Decryption.InvMixColumns(state)

        self.assertEqual(state, expected_mix)
        
        expected_shift = [ 
            [0xd4,0xe0,0xb8,0x1e],
            [0x27,0xbf,0xb4,0x41],
            [0x11,0x98,0x5d,0x52],
            [0xae,0xf1,0xe5,0x30],
        ]
        
        state = decryption.Decryption.InvShiftRows(state)

        self.assertEqual(state, expected_shift)
        
        expected_sub = [ 
            [0x19,0xa0,0x9a,0xe9],
            [0x3d,0xf4,0xc6,0xf8],
            [0xe3,0xe2,0x8d,0x48],
            [0xbe,0x2b,0x2a,0x08]
        ]
        
        state = decryption.Decryption.InvSubBytes(state)

        self.assertEqual(state, expected_sub)

    def test_decypher1(self):
        key = 0x2b7e151628aed2a6abf7158809cf4f3c
        cyphertext = [
            [0x39, 0x02, 0xdc, 0x19],
            [0x25, 0xdc, 0x11, 0x6a],
            [0x84, 0x09, 0x85, 0x0b],
            [0x1d, 0xfb, 0x97, 0x32]    
        ]
        expected = [
            [0x32, 0x88, 0x31, 0xe0],
            [0x43, 0x5a, 0x31, 0x37],
            [0xf6, 0x30, 0x98, 0x07],
            [0xa8, 0x8d, 0xa2, 0x34]
        ]
        plaintext = decryption.Decryption.decypher(cyphertext=cyphertext, key=key)
        self.assertEqual(plaintext, expected)

class TestCypher(unittest.TestCase):
    def test_cypher1(self):
        key = 0x2b7e151628aed2a6abf7158809cf4f3c
        plaintext = [
            [0x32, 0x88, 0x31, 0xe0],
            [0x43, 0x5a, 0x31, 0x37],
            [0xf6, 0x30, 0x98, 0x07],
            [0xa8, 0x8d, 0xa2, 0x34]
        ] 
        expected = [
            [0x39, 0x02, 0xdc, 0x19],
            [0x25, 0xdc, 0x11, 0x6a],
            [0x84, 0x09, 0x85, 0x0b],
            [0x1d, 0xfb, 0x97, 0x32]    
        ]
        cyphertext = encryption.Encryption.cypher(plaintext, key)
        self.assertEqual(cyphertext, expected)


class TestUsage(unittest.TestCase):
    def test_1(self):
        key = ""
        text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        cyphertext = encryption.Encryption.encrypt(text, key)
        plaintext = decryption.Decryption.decrypt(cyphertext, key)
        self.assertEqual(plaintext, text)

    def test_rand(self):
        for _ in range(100):
            keyLen = random.randint(1, 64)
            key = ""
            for _ in range(keyLen):
                key += random.choices(string.ascii_lowercase)[0]
            textLen = random.randint(1, 1024)
            text = ""
            for _ in range(textLen):
                text += random.choices(string.ascii_lowercase)[0]
            cyphertext = encryption.Encryption.encrypt(text, key)
            plaintext = decryption.Decryption.decrypt(cyphertext, key)
            self.assertEqual(plaintext, text)

if __name__ == '__main__':
    unittest.main()