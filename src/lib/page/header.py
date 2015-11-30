
from selenium.webdriver.common.by import By
from lib import base
from lib.page.modal import new_program
from lib.page.modal import create_object
from lib.page import user_email_menu
from lib.page import lhn_menu
from lib.page import hor_nav_bar
from lib.constants import locator

# class ProgramDropdown(base.Page):
#     _cls_selector = selector.PageHeader.LhnMenu
#     ITEMS_COUNT = base.Locator(By.CSS_SELECTOR, _cls_selector.PROGRAMS_COUNT)
#     CREATE_NEW_PROGRAM = base.Locator(By.CSS_SELECTOR,
#                                       _cls_selector.PROGRAM_CREATE_NEW)
#
#     def get_items_count(self):
#         """
#         Counts programs in LHN
#         :return: int
#         """
#         element = self._get_element_when_visible(self.ITEMS_COUNT)
#         return int(element.text)
#
#     def open_create_new_program(self):
#         """
#         Clicks in LHN under Programs on create new button.
#         :rtype: new_program.NewProgramPage
#         """
#         self._click_when_visible(self.CREATE_NEW_PROGRAM)
#         return new_program.NewProgramPage(self._driver)
#
#
#
# class LhnMenu(base.Page):
#     _cls_selector = selector.PageHeader.LhnMenu
#     MY_OBJECTS = base.Locator(By.CSS_SELECTOR, _cls_selector.MY_OBJECTS)
#     ALL_OBJECTS = base.Locator(By.CSS_SELECTOR, _cls_selector.ALL_OBJECTS)
#     PROGRAMS = base.Locator(By.CSS_SELECTOR, _cls_selector.PROGRAMS)
#
#     def select_my_objects(self):
#         """
#         In LHN selects the tab "My Objects"
#         """
#         self._driver\
#             .find_element_by_css_selector(self.MY_OBJECTS)\
#             .click()
#
#     def select_all_objects(self):
#         """
#         In LHN selects the tab "All Objects"
#         """
#         self._click_when_visible(self.ALL_OBJECTS)
#
#     def enter_search_query(self):
#         """
#         Enters and executes a search query in LHN.
#         """
#         pass
#
#     def open_programs(self):
#         """
#         Opens the Programs dropdown in LHN.
#         :rtype: ProgramDropdown
#         """
#         self._click_when_visible(self.PROGRAMS)
#         return ProgramDropdown(self._driver)



class HeaderPage(base.Page):
#     _cls_selector = selector.PageHeader
#     LHN_MENU = base.Locator(By.CSS_SELECTOR, _cls_selector.TRIGGER)
#     USER_MENU = base.Locator(By.CSS_SELECTOR, _cls_selector.USER_MENU)
#     ADMIN_DASHBOARD = base.Locator(By.CSS_SELECTOR,
#                                 _cls_selector.DropdownToggle.ADMIN_MENU_OPTION)

    def open_lhn_menu_new(self):
        return create_object.NewObject(self._driver)
#         return lhn_menu.LhnMenu(self._driver)

#     def open_lhn_menu(self):
#         """
#         Opens LHN on the Dasboard
#         :rtype: LhnMenu
#         """
#         self._click_when_visible(self.LHN_MENU)
#         return LhnMenu(self._driver)

    def open_dashboard(self):
        return hor_nav_bar.HorNavBar(self._driver)

    def enter_search_query(self, query):
        pass

    def open_my_tasks(self):
        pass

    def open_all_objects(self):
        pass

    def open_user_dropdown_new(self):
        self._click_when_visible(locator.PageHeader.USER_MENU)
        return user_email_menu.UserEmailMenu(self._driver)

    def open_menu_dropdown(self):
        pass

    def open_help(self):
        pass

#     def open_user_dropdown(self):
#         """
#         Open user dropdown menu
#         """
#         self._click_when_visible(self.USER_MENU)
#
#     def click_on_admin_menu_item(self):
#         """
#         Click on admin menu option in user dropdown menu
#         """
#         self._click_when_visible(self.ADMIN_DASHBOARD)
