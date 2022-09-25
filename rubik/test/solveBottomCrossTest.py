'''
Created on Sep 25, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve


class solveBottomCrossTest(unittest.TestCase):
    
    
    #Passing in a solved cube and returning an empty string
    #Passing in a cube with same color sides on bottom, unaligned and checking initial to top rotation
    #Passing in a cube  same color sides and checking the count variable
    
    
    
    
    
    #Passing in no cube
    #Passing in an invalid cube

    def test_solve_010_ShouldReturnEmptyStringOnSolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
        
        expectedResult = {}       
        expectedResult['cube'] = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
        expectedResult['solution'] = ''
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    
    def test_solve_020_ShouldRotateToDaisyFromUnalignedBottomCross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wybobrobywrrgryorygogggbrowwboyoyrgbogyoybbrrywgwwwgwb'
    
        expectedResult = {}       
        expectedResult['cube'] = 'oowbbyyrbbrrrryrrygogggbrowwbyyowrggogyoybbyoogwwwwgwb'
        expectedResult['solution'] = 'F'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        