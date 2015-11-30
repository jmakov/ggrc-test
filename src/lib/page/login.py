# header6ff05843-c222-461f-8226-36a7abe6806e

from lib.constants import locator
from lib.page import dashboard
from lib import environment, base, element


class LoginPage(base.Page):
    URL = environment.APP_URL
    
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.navigate_to(self.URL)

        self.button_login = element.Button(driver, locator.Login.BUTTON_LOGIN)

    def login(self):
        """Clicks on the login button on the login page

        Returns:
             dashboard.DashboardPage
        """
        self.button_login.click()
        self.wait_for_redirect()
        return dashboard.DashboardPage(self._driver)
