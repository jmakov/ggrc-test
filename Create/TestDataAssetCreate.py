'''
Created on Jul 24, 2013

@author: diana.tzinov
'''



import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers


class TestDataAssetCreate(WebDriverTestCase):
    
    
    def testDataAssetCreate(self):
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers()
        do.setUtils(util)
        do.Login()
        do.CreateObject("DataAsset")

        
        
if __name__ == "__main__":
    unittest.main()