# header6ff05843-c222-461f-8226-36a7abe6806e

from lib.constants import locator
from lib import base, element


class ProgramInfoWidget(base.Widget):
    locators = locator.Widget

    def __init__(self, driver):
        """
        Args:
            driver (base._CustomDriver)
        """
        super(ProgramInfoWidget, self).__init__(driver)
        self.button_settings = element.Dropdown(driver,
                                                self.locators.BUTTON_SETTINGS)

    def delete_object(self):
        self.navigate_to(self.url_info_widget)
        self.button_settings.select(self.locators.DROPDOWN_DELETE)


class WidgetBarPage(base.Page):
    locators = locator.WidgetBar

    def __init__(self, driver):
        super(WidgetBarPage, self).__init__(driver)
#         self.button_add_widget = element.Dropdown(driver,
#                                                   self.locators.BUTTON_ADD)

    def add_widget(self, option_locator):
        """Adds a new widget to the bar.

        Args:
            option_locator (tuple)
        """
        self.button_add_widget.select(option_locator)

    def get_active_tab_name(self):
        """In general multiple tabs are open. Here we get the name of the active
        one.

        Returns:
             str
        """
        active_widget = element.Button(self._driver, self.locators.TAB_ACTIVE)
        return active_widget.text
