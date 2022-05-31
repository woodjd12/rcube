'''
Created on Oct 6, 2020

@author: johnwood
'''
import unittest
import RCube.create as create
class CreateTest(unittest.TestCase):


    
#     def test100__010ShouldTestIntegrityValue(self):
#         blocks = '111111111222222222333333333444444444555555555666666666'
#         code = '88d897bd22e132d21a538745e63995b07d7c52ce9617a0979520545753ee0ded'
#         expectedResult = {'cube' : blocks, 'integrity' : code, 'status' : 'ok'}
#         parms = {'op' : 'create', 'faces' : '123456'}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)
    def test100_020ShouldTestForNoFacesValues(self):
        blocks = 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo' 
        hashedcode = '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'
        expectedResult = {'cube' : blocks, 'integrity' : hashedcode, 'status' : 'ok'}
        parms = {'op' : 'create'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
#     def test500_010ShouldTestCubeNominalValues(self):
#         expectedResult = {'cube' : '111111111222222222333333333444444444555555555666666666', \
#             'status' : 'ok'}
#         parms = {'op' : 'create', 'faces' : '123456'}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     
#     def test500_020ShouldTestForNoFacesValues(self):
#         blocks = 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo' 
#         expectedResult = {'cube' : blocks, \
#             'status' : 'ok'}
#         parms = {'op' : 'create', 'faces' : None}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     
#     def test500_030ShouldTestForEmptyFaces(self):
#         blocks = 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo' 
#         expectedResult = {'cube' : blocks, \
#             'status' : 'ok'}
#         parms = {'op' : 'create', 'faces' : ''}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)
        
    def test900_010ShouldTestIncorrectNumberFaces(self):
        expectedResult = {'status' : 'error: incorrect number of faces'}
        parms = {'op' : 'create', 'faces' : '12345'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test900_020ShouldTestForDuplicateFaces(self):
        expectedResult = {'status' : 'error: Duplicate faces'}
        parms = {'op' : 'create', 'faces' : '123455'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
    