from unittest import TestCase
import rubik.rotate as rotate

class RotateTest(TestCase):
        
    def test_Rotate_010_BDD(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'abc'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['cube'] = 'abc'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        