

from lib.page.login import LoginPage
from lib.base import Test
from lib.constants import selector


class TestLoginPage(Test):
    def login_as_admin_test(self):
        login_page = LoginPage(self.driver)
        login_page.login()

        self.driver.find_element_by_css_selector(
            selector.PageHeader.DropdownToggle.PEOPLE_LIST_WIDGET
        )
