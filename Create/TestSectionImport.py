'''
Created on Oct 29, 2013

@author: silas@reciprocitylabs.com
'''


import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers


class TestSectionImport(WebDriverTestCase):

    def testSectionImport(self):
        self.testname="testSectionImport"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers()
        do.setUtils(util)
        do.login()
        object_type = "Policy"
        last_created_object_link =do.createObject(object_type)
        do.navigateToObject(object_type, last_created_object_link)
        do.navigateToWidget("Section")
        import_link = element.object_widget_import_link.replace("SECTION", object_type.lower())
        util.hoverOverAndWaitFor(
            element.object_widget_add_items.replace("SECTION", object_type.lower()),
            import_link,
        )
        util.clickOn(import_link)
        #do.deleteObject()


if __name__ == "__main__":
    unittest.main()
