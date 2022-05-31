'''
Created on Oct 5, 2020

@author: johnwood
'''
import unittest
import RCube.info as info


class InfoTest(unittest.TestCase):


    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user' : 'jdw0091'}
        parms = {'op' : 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)
