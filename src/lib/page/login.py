# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

from selenium.webdriver.common.by import By
from lib.constants import selector, uri
from lib.base import Page, Locator


class LoginPage(Page):
    _cls_selector = selector.LandingPage
    LOGIN_BUTTON = Locator(By.CSS_SELECTOR, _cls_selector.BUTTON_LOGIN)
    
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self._driver.get(uri.BASE)

    def login(self, username=None, password=None):
        self.click_and_wait(self.LOGIN_BUTTON)

