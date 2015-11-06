# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

from selenium.webdriver.common.by import By
from lib.base import Page, Locator
from lib.constants import selector


class WidgetBarPage(Page):
    _cls_selector = selector.WidgetBar
    BUTTON_ADD = Locator(By.CSS_SELECTOR, _cls_selector.BUTTON_ADD)
    DROPDOWN = Locator(By.CSS_SELECTOR, _cls_selector.DROPDOWN)
    TAB = Locator(By.CSS_SELECTOR, _cls_selector.TAB)

    def add_widget(self, name):
        self.click_and_wait(self.BUTTON_ADD)
        elements = self._driver.find_elements(
            self.DROPDOWN.type, self.DROPDOWN.value)

        for element in elements:
            if name == element.text:
                element.click()
                break

    def get_active_tab_name(self):
        element = self._get_element_when_visible(self.TAB)
        return element.text
