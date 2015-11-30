# header6ff05843-c222-461f-8226-36a7abe6806e

import uuid
from lib import base
from lib.constants.test import create_new_program


class ModalNewProgramPage(base.Test):
    """Methods for simulating common user actions"""

    def __init__(self, page):
        """
        Args:
            page (lib.page.modal.new_program.NewProgramPage): modal page
        """
        super(ModalNewProgramPage, self).__init__()
        self.page = page
        self.program_identifier = str(uuid.uuid4())

    def enter_test_data(self):
        """Fills out the entire form"""
        self.page.enter_title(create_new_program.TITLE +
                              self.program_identifier)
        self.page.enter_description(
            create_new_program.DESCRIPTION_SHORT)
        self.page.enter_notes(
            create_new_program.NOTES_SHORT)
        self.page.enter_code(create_new_program.CODE +
                             self.program_identifier)
        self.page.toggle_private_program()
        self.page.enter_primary_contact(
            create_new_program.PRIMARY_CONTACT)
        self.page.enter_secondary_contact(
            create_new_program.SECONDARY_CONTACT)
        self.page.enter_program_url(
            create_new_program.PROGRAM_URL)
        self.page.enter_reference_url(
            create_new_program.REFERENCE_URL)
        self.page.enter_effective_date_start_month()
        self.page.enter_stop_date_end_month()
