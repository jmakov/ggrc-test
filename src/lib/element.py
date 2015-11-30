# header6ff05843-c222-461f-8226-36a7abe6806e

from lib import base


class Text(base.Element):
    pass


class TextInputField(base.Element):
    def enter_text(self, text):
        self._element.clear()
        self._element.send_keys(text)


class Iframe(base.Element):
    pass


class DatePicker(base.Element):
    def select_month_start(self):
        pass

    def _datepicker_month_end(self, date_picker_locator, field_locator):
        """
        Args:
            date_picker_locator (Locator)
            field_locator (Locator): locator of the field we have to click on to
            activate the datepicker
        """
        elements = self._get_datepicker_elements_for_current_month(
            self.locator, field_locator)
        elements[-1].click()
        self._wait_until_invisible(date_picker_locator)


class Button(base.Element):
    def click(self):
        self._element.click()


class Checkbox(base.Element):
    def __init__(self, driver, locator, is_checked=False):
        super(Checkbox, self).__init__(driver, locator)
        self.is_checked = is_checked

    def click(self):
        self._element.click()
        self.is_checked = not self.is_checked


class Toggle(base.Element):
    def __init__(self, driver, locator, is_activated=False):
        super(Toggle, self).__init__(driver, locator)
        self.is_activated = is_activated

    def click(self):
        self._element.click()
        self.is_activated = not self.is_activated


class Dropdown(base.Element):
    def select(self, option):
        self._element.click()
        # todo sel. relevant option from dropdown
