'''
Created on Nov 29, 2020

@author: johnwood
'''
import unittest
import RCube.rotate as rotate
from hashlib import sha256

class Test(unittest.TestCase):


    def test100_910IncorrectDictionaryInput(self):
        cube = '111111111222222222333333333444444444555555555666666665'
        integrity = 'FFFA07BE4BF1438C0C660DE9E9C0624640DC23856E875F6730F6195CEAF2AB61'
        expectedResult = {'status' : 'error: incorrect number of a element designator'}
        parms = {'op' : 'check', 'side' : 'f', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_920MissingSidekey(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedResult = {'status' : 'error: missing side key'}
        parms = {'op' : 'check', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_930MissingSideValue(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedResult = {'status' : 'error: missing side value'}
        parms = {'op' : 'check', 'side' : '', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_010TestfRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'f', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_020TestFRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'F', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_030TestrRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'r', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)        
        
    def test100_040TestRRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'R', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)     
    
    def test100_050TestbRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'b', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)   
    
    def test100_060TestBRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'gggggggggrrwrrwrrwbbbbbbbbbyooyooyooooowwwwwwyyyyyyrrr'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'B', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)  
    
    def test100_070TestlRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'l', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)  
    
    def test100_080TestLRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'yggyggyggrrrrrrrrrbbwbbwbbwooooooooogwwgwwgwwbyybyybyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'L', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test100_090TesttRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 't', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test100_100TestTRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'T', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_110TestuRotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'ggggggooorrrrrrgggbbbbbbrrroooooobbbwwwwwwwwwyyyyyyyyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'u', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test100_120TestURotation(self):
        cube='gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        integrity='546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
        expectedCube = 'ggggggrrrrrrrrrbbbbbbbbbooooooooogggwwwwwwwwwyyyyyyyyy'
        expectedIntegrity = sha256(expectedCube.encode('utf-8')).hexdigest().upper()
        expectedResult = {'status':'rotated', 'cube': expectedCube, 'integrity': expectedIntegrity}
        parms = {'op' : 'check', 'side' : 'U', 'cube' : cube, 'integrity' : integrity}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)   