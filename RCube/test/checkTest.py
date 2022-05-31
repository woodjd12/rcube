'''
Created on Oct 25, 2020

@author: johnwood
'''
import unittest
import RCube.check as check

class CheckTest(unittest.TestCase):


#     def test900_010TestForMissingCubeValue(self):
#         expectedResult = {'status' : 'error: missing cube value'}
#         parms = {'op' : 'check', 'cube' : ''}
#         actualResult = check._check(parms)
#         self.assertDictEqual(expectedResult, actualResult)
        
    def test900_020TestForMissingCubeKey(self):
        integrity = 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'
        expectedResult = {'status' : 'error: missing cube key'}
        parms = {'op' : 'check', 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test900_030TestForMissingintegrityValue(self):
        cube = '111111111222222222333333333444444444555555555666666666'
        expectedResult = {'status' : 'error: missing integrity value'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : ''}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test900_040TestForMissingIntegrityKey(self):
        cube = '111111111222222222333333333444444444555555555666666666'
        expectedResult = {'status' : 'error: missing integrity key'}
        parms = {'op' : 'check', 'cube' : cube}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test900_050TestForUnmathedCubeAndIntegrity(self):
        cube = '111111111222222222333333333444444444555555555666666666'
        integrity = '18d897bd22e132d21a538745e63995b07d7c52ce9617a0979520545753ee0ded'
        expectedResult = {'status' : 'error: cube does not match integrity value'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test900_060TestForNumberOfElements(self):
        cube = '11111111122222222233333333344444444455555555566666666'
        integrity = '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'
        expectedResult = {'status' : 'error: incorrect number of elements'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test900_070TestForSixDistinctElements(self):
        cube = '111111111222222222333333333444444444555555555111111111'
        integrity = '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'
        expectedResult = {'status' : 'error: incorrect number of distinct elements'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test900_080TestForNineofEachElement(self):
        cube = '111111111222222222333333333444444444555555555666666665'
        integrity = 'FFFA07BE4BF1438C0C660DE9E9C0624640DC23856E875F6730F6195CEAF2AB61'
        expectedResult = {'status' : 'error: incorrect number of a element designator'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test900_090TestForDistinctMiddleValues(self):
        cube = '111141111222222222333333333144444444555555555666666666'
        integrity = 'FC8DA764A87163BF7CE3606E1F76D6DE7B4EA994B1D463DF02211C936A0D6898'
        expectedResult = {'status' : 'error: middle value are not distinct'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test900_200TestForImpossibleCorners(self):
        cube = 'bbgbbbbbbwoooooooogogggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy'
        integrity = '573D39853F85AFD6E55A0760EFA1EBE8A7EACA41753055D9B41D0B3FC5C2E986'
        expectedResult = {'status' : 'error: impossible corners'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)   
         
    def test900_100TestForImpossibleEdges(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbybooooooooowwwwwwwwwybyyyyyyy'
        integrity = '96DDC169F9D847DC098BA3805C1AD55B088293F0138D7D1603C03543F7D5589E'
        expectedResult = {'status' : 'error: impossible edges'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)    
        
    def test100_010TestNominalValueofFullCube(self):
        cube = 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'
        integrity = '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'
        expectedResult = {'status' : 'full'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_020TestNominalValueofSpotsCube(self):
        cube = 'rrrrbrrrryyyyryyyyoooogoooowwwwowwwwbbbbybbbbggggwgggg'
        integrity = '8BE0EEDF13B2B464A2C7A120E6104AC7039B758E93D6F65651616FBBEED9A1EF'
        expectedResult = {'status' : 'spots'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_030TestNominalValueofCrossesCube(self):
        cube = 'ybybbbybybrbrrrbrbwgwgggwgwgogooogogryryyyryrowowwwowo'
        integrity = '3A2CA2368EDAB67D1EAB30A5DCA67757FC389AC2924E3EDAB522BAABF8403202'
        expectedResult = {'status' : 'crosses'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
  
    