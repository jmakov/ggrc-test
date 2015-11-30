# from selenium.webdriver.common.by import By
from lib import base
from lib.constants import locator


class UserEmailMenu(base.Page):

    def click_on_admin_menu_item(self):
        """
        Click on admin menu option in user dropdown menu
        """
        self._click_when_visible(locator.DropdownToggle.ADMIN_MENU_OPTION)
