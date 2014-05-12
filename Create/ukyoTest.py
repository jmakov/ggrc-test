import time
import unittest

from helperRecip.Elements import Elements
from helperRecip.Helpers import Helpers
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.testcase import *


class ukyoTest(WebDriverTestCase):


    def test1(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080")  #("http://yahoo.com")
        time.sleep(5)
        driver.quit()

        
if __name__ == "__main__":
        unittest.main()

