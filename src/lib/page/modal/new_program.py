# header6ff05843-c222-461f-8226-36a7abe6806e

from lib.constants import locator
from lib.page import widget_bar
from lib import base, date, element


class NewProgramPage(base.Page):
    # todo: add elements for static fields
    title = ""
    description = ""
    notes = ""
    code = ""
    state = ""
    privacy = ""
    manager = ""
    secondary_contact = ""
    program_url = ""
    reference_url = ""
    effective_date = ""
    stop_date = ""
    button_save_and_add_another = ""
    button_save_and_close = ""

    def __init__(self, driver):
        super(NewProgramPage, self).__init__(driver)
        self.title_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.TITLE_UI)
        self.description_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.DESCRIPTION_UI)
        self.notes_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.NOTES_UI)
        self.code_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.CODE_UI)
        self.state_ui = element.Dropdown(
            driver, locator.ModalCreateNewProgram.STATE_UI)
        self.show_optional_fields_ui = element.Toggle(
            driver,
            locator.ModalCreateNewProgram.BUTTON_SHOW_ALL_OPTIONAL_FIELDS)
        self.is_private_program_ui = element.Checkbox(
            driver, locator.ModalCreateNewProgram.PRIVATE_CHECKBOX_UI)
        self.primary_contact_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.PRIMARY_CONTACT_UI)
        self.secondary_contact_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.SECONDARY_CONTACT_UI)
        self.program_url_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.PROGRAM_URL_UI)
        self.reference_url_ui = element.TextInputField(
            driver, locator.ModalCreateNewProgram.REFERENCE_URL_UI)
        self.effective_date_ui = element.DatePicker(
            driver, locator.ModalCreateNewProgram.EFFECTIVE_DATE_UI)
        self.stop_date_ui = element.DatePicker(
            driver, locator.ModalCreateNewProgram.STOP_DATE_UI)

    def enter_title(self, text):
        """Enters the text into the title element."""
        self.title_ui.enter_text(text)

    def enter_description(self, description):
        """Enters the text into the description element"""
        self.description_ui.enter_text(description)

    def enter_notes(self, notes):
        """Enters the text into the notes element"""
        self.notes_ui.enter_text(notes)

    def enter_code(self, code):
        """Enters the text into the code element"""
        self.code_ui.enter_text(code)

    def select_state(self, state):
        """Selects a state from the dropdown"""
        pass

    def toggle_optional_fields(self):
        """Shows or hides optional fields"""
        pass

    def toggle_private_program(self):
        """Marks or unmarks the newly created program as private by (un)
        checking a checkbox"""
        self.is_private_program_ui.click()

    def enter_primary_contact(self, contact):
        """Enters the text into the primary contact element"""
        self.primary_contact_ui.enter_text(contact)

    def enter_secondary_contact(self, contact):
        """Enters the text into the secondary contact element"""
        self.secondary_contact_ui.enter_text(contact)

    def enter_program_url(self, url):
        """Enters the program url for this program object"""
        self.program_url_ui.enter_text(url)

    def enter_reference_url(self, url):
        """Enters the reference url for this program object"""
        self.reference_url_ui.enter_text(url)

    def enter_effective_date_start_month(self):
        """Selects from datepicker the start date"""
        self.effective_date_ui.select_month_start()

    def enter_stop_date_end_month(self):
        """Selects from datepicker the end date"""
        # todo
        self.stop_date = date.get_month_end(date.get_current())
        self._datepicker_month_end(self.DATE_PICKER, self.STOP_DATE)

    def save_and_add_other(self):
        """Saves this objects and opens a new form"""
        # todo
        pass

    def save_and_close(self):
        """Saves this object.

        Note that at least the title must be entered and it must be unique.
        """
        # todo
        self._click_when_visible(self.BUTTON_SAVE_AND_CLOSE)
        self.wait_for_redirect()

        # get this program's number from the url
        self.url_redirect = self._driver.current_url
        return widget_bar.ProgramInfoWidget(self._driver, self.url_redirect)
