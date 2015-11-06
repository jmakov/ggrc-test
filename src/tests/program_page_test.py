# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

import uuid
from lib.page import dashboard
from lib import base
from lib.constants.test import create_new_program
from lib.constants import selector, element


class ProgramPage(base.Test):
    def setup(self):
        self._set_driver()
        self.new_program_page = None
        self.dashboard_page = dashboard.DashboardPage(self.driver)
        self.dashboard_page.navigate_to()
        self.lhn_menu = self.dashboard_page.open_lhn_menu()
        self.lhn_menu.select_all_objects()
        self.program_dropdown = self.lhn_menu.open_programs()
        self.new_program_page = self.program_dropdown.open_create_new_program()


class TestProgramPage(ProgramPage):
    def start_test(self):
        program_items_at_the_beginning = \
            self.program_dropdown.get_items_count()
        self.program_identifier = str(uuid.uuid4())
        self.program_title = create_new_program.TEST_TITLE\
            + self.program_identifier
        self.program_code = create_new_program.TEST_CODE \
            + self.program_identifier

        self.new_program_page.enter_title(self.program_title)
        self.new_program_page.enter_description(
            create_new_program.TEST_DESCRIPTION_SHORT)
        self.new_program_page.enter_notes(create_new_program.TEST_NOTES_SHORT)
        self.new_program_page.enter_code(self.program_identifier)
        self.new_program_page.checkbox_check_private_program()
        self.new_program_page.enter_primary_contact(
            create_new_program.TEST_PRIMARY_CONTACT)
        self.new_program_page.enter_secondary_contact(
            create_new_program.TEST_SECONDARY_CONTACT)
        self.new_program_page.enter_program_url(
            create_new_program.TEST_PROGRAM_URL)
        self.new_program_page.enter_reference_url(
            create_new_program.TEST_REFERENCE_URL)
        self.new_program_page.enter_effective_date_start_month()
        self.new_program_page.enter_stop_date_end_month()
        self.new_program_page.save_and_close()

        self.wait_for_redirect()

        active_tab_name = self.dashboard_page.get_active_tab_name()
        assert active_tab_name == element.LandingPage.PROGRAM_INFO_TAB, \
            "The name of the active tab is not %s" \
            % element.LandingPage.PROGRAM_INFO_TAB

        self.dashboard_page.open_lhn_menu()
        program_items_at_the_end = self.program_dropdown.get_items_count()
        assert program_items_at_the_beginning < program_items_at_the_end, \
            "Programs count in LHN was not updated after adding a new program"

        contents = self.driver.find_elements_by_css_selector(
            selector.WidgetBar.ProgramInfo.TITLES)
        title, state, manager, primary_contact, program_url, reference_url = \
            contents

        descriptions = self.driver.find_elements_by_css_selector(
            selector.WidgetBar.ProgramInfo.DESCRIPTIONS)
        description = descriptions[4]
        notes = descriptions[5]

        advanced_contents = self.driver.find_element_by_css_selector(
            selector.WidgetBar.ProgramInfo.ADVANCED)

    def info_panel_test(self):
        pass

    def mapping_via_lhn_test(self):
        pass

    def mapping_asset_business_object_via_tab_test(self):
        pass

    def mapping_directives_control_objective_tab_test(self):
        pass

    def mapping_via_regulation_contract_policy_tab_test(self):
        pass
