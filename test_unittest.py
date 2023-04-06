import galois
import unittest 
import keyExpansion
class TestGaloisField(unittest.TestCase):
    def test_add(self):
        self.assertEqual(galois.gAdd(0x57, 0x83), 0xd4)

    def test_mult(self):
        self.assertEqual(galois.gMult(0x02, 0x87), 0x15)
        self.assertEqual(galois.gMult(0x57, 0x13), 0xfe)
        self.assertEqual(galois.gMult(0x57, 0x83), 0xc1)
    
class TestKeyExpansion(unittest.TestCase):
    def test_keyExpansion(self):
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



if __name__ == '__main__':
    unittest.main()