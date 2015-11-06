# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

from selenium.webdriver.common.by import By
from lib.base import Page, Locator
from lib.page import new_program
from lib.constants import selector


class ProgramDropdown(Page):
    _cls_selector = selector.PageHeader.LhnMenu
    ITEMS_COUNT = Locator(By.CSS_SELECTOR, _cls_selector.PROGRAMS_COUNT)
    CREATE_NEW_PROGRAM = Locator(By.CSS_SELECTOR,
                                 _cls_selector.PROGRAM_CREATE_NEW)

    def get_items_count(self):
        element = self._get_element_when_visible(self.ITEMS_COUNT)
        return int(element.text)

    def open_create_new_program(self):
        self.click_and_wait(self.CREATE_NEW_PROGRAM)
        return new_program.NewProgramPage(self._driver)


class LhnMenu(Page):
    _cls_selector = selector.PageHeader.LhnMenu
    MY_OBJECTS = Locator(By.CSS_SELECTOR, _cls_selector.MY_OBJECTS)
    ALL_OBJECTS = Locator(By.CSS_SELECTOR, _cls_selector.ALL_OBJECTS)
    PROGRAMS = Locator(By.CSS_SELECTOR, _cls_selector.PROGRAMS)

    def select_my_objects(self):
        self._driver\
            .find_element_by_css_selector(self.MY_OBJECTS)\
            .click()

    def select_all_objects(self):
        self.click_and_wait(self.ALL_OBJECTS)

    def enter_search_query(self):
        pass

    def open_programs(self):
        self.click_and_wait(self.PROGRAMS)
        return ProgramDropdown(self._driver)


class HeaderPage(Page):
    _cls_selector = selector.PageHeader
    LHN_MENU = Locator(By.CSS_SELECTOR, _cls_selector.TRIGGER)
    
    def open_lhn_menu(self):
        self.click_and_wait(self.LHN_MENU)
        return LhnMenu(self._driver)

    def open_dashboard(self):
        pass

    def enter_search_query(self, query):
        pass

    def open_my_tasks(self):
        pass

    def open_all_objects(self):
        pass

    def open_user_dropdown(self):
        pass

    def open_menu_dropdown(self):
        pass

    def open_help(self):
        pass
