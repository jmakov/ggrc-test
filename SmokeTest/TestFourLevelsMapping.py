'''
Created on Jul 14, 2014

@author: uduong
'''
import time
import unittest

from helperRecip.Elements import Elements
from helperRecip.Helpers import Helpers
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.testcase import *


class TestFourLevelsMapping(WebDriverTestCase):

    def testFourLevelsMapping(self):
        self.testname="TestFourLevelsMapping"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        # mapping and un-mapping up to 3 levels: 
        # Program->Regulation->Section->Object
#         titlePol = do.getUniqueString("policy")
#         titlePrgm = do.getUniqueString("program")
#         titleSec = do.getUniqueString("section")
#         titleMkt = do.getUniqueString("policy")

        titlePol = "policy-auto-test10:24:50.749797"
        titlePrgm = "program-auto-test10:24:50.749869"
        titleSec = "section-auto-test10:24:50.749922"
        titleMkt = "market-auto-test06:57:40.975635"       
        print titlePol
        print titlePrgm
        print titleSec
        print titleMkt
        
        # playing around
        do.mapAObjectWidget("Section", titleSec)
        
        do.mapTo2ndTier("Market", titleMkt)
        
        do.createObject("Market", titleMkt)
        do.createObject("Policy", titlePol)
        do.mapAObjectWidget("Section", titleSec)
        
        do.createObject("Section", titleSec)
        do.mapAObjectWidget("Market", titleMkt)
                  
        
        do.createObject("Program", titlePrgm)
        do.mapAObjectWidget("Policy", titlePol)
              




if __name__ == "__main__":

    unittest.main()