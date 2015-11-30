# header6ff05843-c222-461f-8226-36a7abe6806e

from lib import constants, environment
from lib.page import widget_bar, header


# class DashboardPage(widget_bar.WidgetBarPage, header.HeaderPage):
class DashboardPage(header.HeaderPage):
    URL = environment.APP_URL + constants.url.DASHBOARD

    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)
        self.navigate_to(self.URL)
