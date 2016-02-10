# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

import pytest
from lib import base
from lib.constants import element, url
from lib.page import dashboard
from lib.page import widget_bar


class TestProgramPage(base.Test):
  """A part of smoke tests, section 4."""

  @pytest.mark.smoke_tests
  def test_object_count_updates(self, selenium, new_program):
    """Checks if the count updates in LHN after creating a new program
    object."""
    _, program_object = new_program
    lhn_menu = dashboard.DashboardPage(selenium.driver) \
        .open_lhn_menu() \
        .select_my_objects()

    assert lhn_menu.button_programs.members_count \
        >= int(program_object.object_id)

  @pytest.mark.smoke_tests
  def test_app_redirects_to_new_program_page(self, selenium, new_program):
    """Tests if after saving and closing the lhn_modal the app redirects to
    the object page.

    Generally we start at a random url. Here we verify that after saving
    and closing the lhn_modal we're redirected to an url that contains an
    object id.
    """
    _, program_info_page = new_program
    assert url.PROGRAMS + "/" + program_info_page.object_id in \
        program_info_page.url

  @pytest.mark.smoke_tests
  def test_info_tab_is_active_by_default(self, selenium, new_program):
    """Tests if after the lhn_modal is saved we're redirected and the info
    tab is activated.

    Because the app uses url arguments to remember the state of the page
    (which widget is active), we can simply use the url of the created
    object.
    """
    _, program_info_page = new_program
    program_info_page.navigate_to()
    horizontal_bar = widget_bar.DashboardWidgetBarPage(selenium.driver)

    assert horizontal_bar.get_active_widget_name() == \
        element.LandingPage.PROGRAM_INFO_TAB

  @pytest.mark.smoke_tests
  def test_info_tab_contains_entered_data(self, selenium, new_program):
    """Verify that the created object contains the data we've entered
    into the modal."""
    modal, program_object = new_program

    assert modal.ui_title.text == program_object.title_entered.text
    assert modal.ui_description.text == \
        program_object.description_entered.text
    assert modal.ui_notes.text == program_object.notes_entered.text

    assert modal.ui_code.text == program_object.code_entered.text
    assert program_object.primary_contact_entered.text in \
        modal.ui_primary_contact.text
    assert program_object.secondary_contact_entered.text in \
        modal.ui_secondary_contact.text
    assert modal.ui_program_url.text == \
        program_object.program_url_entered.text
    assert modal.ui_reference_url.text == \
        program_object.reference_url_entered.text
    assert modal.ui_effective_date.text == \
        program_object.effective_date_entered.text
    assert modal.ui_stop_date.text == program_object.stop_date_entered.text
