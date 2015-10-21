

from selenium.webdriver.common.by import By
from lib.constants import selector
from lib.base import Page, Locator


class NewProgramPage(Page):
    _cls_selector = selector.PageHeader.LhnMenu.CreateNewProgram
    TITLE = Locator(By.CSS_SELECTOR, _cls_selector.TITLE)
    DESCRIPTION = Locator(By.CSS_SELECTOR, _cls_selector.DESCRIPTION)
    NOTES = Locator(By.CSS_SELECTOR, _cls_selector.NOTES)
    CODE = Locator(By.CSS_SELECTOR, _cls_selector.CODE)
    PRIVATE_CHECKBOX = Locator(By.CSS_SELECTOR, _cls_selector.PRIVATE_CHECKBOX)
    PRIMARY_CONTACTS = Locator(By.CSS_SELECTOR, _cls_selector.PRIMARY_CONTACT)
    SECONDARY_CONTACTS = Locator(By.CSS_SELECTOR,
                                 _cls_selector.SECONDARY_CONTACT)
    PROGRAM_URL = Locator(By.CSS_SELECTOR, _cls_selector.PROGRAM_URL)
    REFERENCE_URL = Locator(By.CSS_SELECTOR, _cls_selector.REFERENCE_URL)
    DATE_PICKER = Locator(By.CSS_SELECTOR, _cls_selector.DATE_PICKER)
    EFFECTIVE_DATE = Locator(By.CSS_SELECTOR, _cls_selector.EFFECTIVE_DATE)
    STOP_DATE = Locator(By.CSS_SELECTOR, _cls_selector.STOP_DATE)
    BUTTON_SAVE_AND_CLOSE = Locator(By.CSS_SELECTOR,
                                    _cls_selector.BUTTON_SAVE_AND_CLOSE)

    def enter_title(self, title):
        self._find_field_and_enter_data(self.TITLE, title)

    def enter_description(self, description):
        self._find_iframe_and_enter_data(self.DESCRIPTION, description)

    def enter_notes(self, notes):
        self._find_iframe_and_enter_data(self.NOTES, notes)

    def enter_code(self, code):
        self._find_field_and_enter_data(self.CODE, code)

    def select_state(self, state):
        pass

    def hide_all_optional_fields(self):
        pass

    def checkbox_check_private_program(self):
        self.click_and_wait(self.PRIVATE_CHECKBOX)

    def enter_primary_contact(self, contact):
        self._find_field_and_enter_data(self.PRIMARY_CONTACTS, contact)

    def enter_secondary_contact(self, contact):
        self._find_field_and_enter_data(self.SECONDARY_CONTACTS, contact)

    def enter_program_url(self, url):
        self._find_field_and_enter_data(self.PROGRAM_URL, url)

    def enter_reference_url(self, url):
        self._find_field_and_enter_data(self.REFERENCE_URL, url)

    def enter_effective_date_start_month(self):
        self._datepicker_month_start(self.DATE_PICKER, self.EFFECTIVE_DATE)

    def enter_stop_date_end_month(self):
        self._datepicker_month_end(self.DATE_PICKER, self.STOP_DATE)

    def save_and_add_other(self):
        pass

    def save_and_close(self):
        self.click_and_wait(self.BUTTON_SAVE_AND_CLOSE)
