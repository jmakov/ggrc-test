import sys
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../"
sys.path.append(PROJECT_ROOT_PATH)
PROJECT_SRC_PATH = PROJECT_ROOT_PATH + "src/"
sys.path.append(PROJECT_SRC_PATH)

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib.constants import locator
from lib.constants import url
from lib import environment
from lib import base
from lib.page import admin_dashboard as adb_page
from lib.page import dashboard
from lib.page import header
from lib.constants.test import admin_dashboard as adb_const
from selenium.webdriver.support.ui import Select
import uuid
import time
import os
from os.path import expanduser
from datetime import datetime


@pytest.yield_fixture(scope="class", autouse=False)
def dashboard_setup():
    test = base.Test()
    test.init_resources()
    db = dashboard.DashboardPage(test.driver)
    yield db

    test.close_resources()

@pytest.fixture(scope="module", autouse=False)
def need_very_first_person():
    test = base.Test()
    test.init_resources()
    adb = adb_page.AdminDashboardPage(test.driver)
    adb.navigate_to()

    adb.click_add_new_person()
    adb.enter_add_person_data_and_save(
        adb_const.People.PeopleList.FIRST_USERNAME,
        adb_const.People.PeopleList.FIRST_EMAIL,
        adb_const.People.PeopleList.FIRST_COMPANY)
    adb.close_modal()

    adb.reload_page()

    test.close_resources()

@pytest.yield_fixture(scope="class", autouse=False)
def admin_dashboard_setup():
    test = base.Test()
    test.init_resources()
    adb = adb_page.AdminDashboardPage(test.driver)
    adb.navigate_to()

    yield adb

    test.close_resources()

#@pytest.yield_fixture(scope="class", autouse=False)
#def header_setup():
    #test = base.Test()
    #test.init_resources()
    #hdr = header.HeaderPage(test.driver)
    #hdr.navigate_to(environment.APP_URL + constants.url.ADMIN_DASHBOARD)
    #yield hdr

    #test.close_resources()


@pytest.yield_fixture(scope="class", autouse=False)
def import_export_setup():
    test = base.Test()
    test.init_resources()
    ei = adb_page.ExportImportPage(test.driver)
    #ei.navigate_to()
    yield ei

    test.close_resources()


class TestAdminDashboardOpen(base.Test):
    """
    Class for testing opening admin dashboard with click on dropdown menu.
    """

    def test_click_on_admin_menu_item(self, dashboard_setup):
        """
        Test if Admin Dasboard opens after login, click on user menu and
        admin dashbooard menu item.
        """
        dashboard_setup.navigate_to(dashboard_setup.URL)

        base_url = environment.APP_URL

        dd = dashboard_setup.open_user_dropdown_new()
        dd.click_on_admin_menu_item()

        expected_url = base_url + url.ADMIN_DASHBOARD
        assert dashboard_setup._driver.current_url == expected_url

    def test_open_user_dropdown(self, dashboard_setup):
        """
        Test opening user dropdown.
        """
        dashboard_setup.navigate_to(dashboard_setup.URL)
        dashboard_setup.open_user_dropdown_new()


class AdminDashboardTestsBase(base.Test):
    """
    Base class for admin dashboard tests.
    """

    def open_dropdown_in_second_tier(self, adb):
        """
        Open dropdown in second tier
        """

        adb.navigate_to()
        adb.open_people_list()
        adb.click_arrow_in_first_tier()
        adb._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.GEAR_BUTTON)
        adb._get_element_when_clickable(
            locator.AdminDashboardPage.PeopleList.GEAR_BUTTON)
        adb._get_element_when_clickable(
            locator.AdminDashboardPage.PeopleList.GEAR_BUTTON).click()

        #adb._click_when_visible(
            #locator.AdminDashboardPage.PeopleList.GEAR_BUTTON)
        return adb

class TestAdminDashboardGeneral(AdminDashboardTestsBase):
    """
    Run general tests
    """

    def test_numbers_etc_are_correct(self, admin_dashboard_setup):
        """
        Check if numbers of roles, people, events, custom attributes
        are correct.
        """
        adb = admin_dashboard_setup
        adb.navigate_to()

        # Check number of people
        adb.open_people_list()

        num_people_menu = adb.get_menu_num_items(
            locator.AdminDashboardPage.HorizontalMenu.PEOPLE_ITEM)
        num_people_real = adb.get_list_length_multipage(
            locator.AdminDashboardPage.PeopleList.LIST_ELEMENT)
        assert num_people_menu <= num_people_real

        # Check number of roles
        adb.open_roles()
        num_roles_menu = adb.get_menu_num_items(
            locator.AdminDashboardPage.HorizontalMenu.ROLES_ITEM)
        num_roles_real = adb.get_num_elements(
            locator.AdminDashboardPage.Roles.LIST_ELEMENT)
        assert num_roles_menu <= num_roles_real

        # Check number of events
        adb.open_event_log()
        num_events_menu = adb.get_menu_num_items(
            locator.AdminDashboardPage.HorizontalMenu.EVENTS_ITEM)
        num_events_real = adb.get_list_length_multipage(
            locator.AdminDashboardPage.Events.LIST_ELEMENT)
        assert num_events_menu <= num_events_real

        # Check number of custom attributes
        adb.open_custom_attributes()
        num_custom_attributes_menu = adb.get_menu_num_items(
            locator.AdminDashboardPage.HorizontalMenu.CUSTOM_ATTRIBUTES_ITEM)
        num_custom_attributes_real = adb.get_num_elements(
            locator.AdminDashboardPage.CustomAttributes.LIST_ELEMENT)
        assert num_custom_attributes_menu == num_custom_attributes_real


class TestAdminDashboardPeople(AdminDashboardTestsBase):
    """
    Tests for people tab
    """

    def add_people(self, adb, num):
        """
        Add number of people for admin dashboard page tests
        """
        adb.click_add_new_person()
        cls_base = adb_const.People.PeopleList
        for i in range(num + 1):
            str_i = str(uuid.uuid4())
            name = cls_base.GEN_USERNAME + str_i
            email = cls_base.GEN_EMAIL_NAME + str_i \
                    + "@" + cls_base.GEN_EMAIL_DOMAIN
            company = cls_base.GEN_COMPANY + str_i

            adb.enter_add_person_data_and_save(name, email, company)
            time.sleep(1)

        adb.close_modal()


    def test_people_list_entries(self,
                                 admin_dashboard_setup,
                                 need_very_first_person):
        """
        Check if username and email on list are correct.
        TODO: Enable asserts, when defined how this should work
        """
        adb = admin_dashboard_setup
        adb.open_people_list()
        username = adb._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.FirstItem.USERNAME).text
        assert username == adb_const.People.PeopleList.FIRST_USERNAME

        email = adb._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.FirstItem.EMAIL).text
        assert email == adb_const.People.PeopleList.FIRST_EMAIL

    def test_people_next_prev_link(self, admin_dashboard_setup):
        """
        Implement next and previous link test
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()

        num_people = adb.get_menu_num_items(
            locator.AdminDashboardPage.HorizontalMenu.PEOPLE_ITEM)

        num_needed = adb_const.People.PeopleList.NUM_NEEDED_FOR_MULTIPAGE
        if num_people < num_needed:
            self.add_people(adb, num_needed - num_people)

        adb.navigate_to()
        adb.open_people_list()

        adb.click_next_page()
        adb.click_previous_page()

    def test_people_show_additional_data(self, admin_dashboard_setup):
        """
        Clicking on left arrow must show additional data.
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()

        adb._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.FirstItem.LEFT_ARROW)

        #adb.click_next_page()
        adb.click_arrow_in_first_tier()

        # -- the second tier of the tree view is opening

        items = adb.get_all_items(
            locator.AdminDashboardPage.PeopleList.FirstItem.AdditionalContent.CONTAINER,
            locator.AdminDashboardPage.PeopleList.FirstItem.AdditionalContent.ELT,
            locator.AdminDashboardPage.PeopleList.FirstItem.AdditionalContent.ELT_LABEL)

        # check for items that must be present
        for item in adb_const.People.AdditionalContent.ITEMS_IN_LIST:
            assert item in items

    def test_click_add_new_person(self, admin_dashboard_setup):
        """
        Click  Add person at the bottom of people list -- "New Person" modal
        window appears
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()
        adb.click_add_new_person()
        adb.close_modal()

    def test_click_gear_button_in_second_tier(self, admin_dashboard_setup):
        """
        Click gear icon in the 2nd tier -- The dropdown list appears
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()

        adb = self.open_dropdown_in_second_tier(adb)
        adb._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.DROPDOWN_MENU)

    def test_check_content_of_dropdown_in_second_tier(self, admin_dashboard_setup):
        """
        The items of the dropdown list are:
        - View Profile Page
        - Edit Authorizations
        - Edit Person
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()

        adb = self.open_dropdown_in_second_tier(adb)

        items = adb.get_all_items(
            locator.AdminDashboardPage.PeopleList.AdditionalContent.Dropdown.UL,
            locator.AdminDashboardPage.PeopleList.AdditionalContent.Dropdown.LI,
            locator.AdminDashboardPage.PeopleList.AdditionalContent.Dropdown.LI_SUB)

        # check for items that must be present
        for item in adb_const.People.AdditionalContent.Dropdown.ITEMS_IN_LIST:
            assert item in items

    def test_edit_person(self, admin_dashboard_setup):
        """
        Click Edit Person item -- edit person modal apears
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()

        adb = self.open_dropdown_in_second_tier(adb)
        adb._click_when_visible(
            locator.AdminDashboardPage.PeopleList.AdditionalContent.Dropdown.EDIT)

        title = adb.get_modal_title()
        adb.close_modal()

        assert title == adb_const.People.AdditionalContent.Dropdown.EDIT_TITLE

    def test_edit_person_authorizations(self, admin_dashboard_setup):
        """
        Click edit Authorizations item -- User Role Assignments modal apears
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()

        adb = self.open_dropdown_in_second_tier(adb)
        adb._click_when_visible(
            locator.AdminDashboardPage.PeopleList.AdditionalContent.Dropdown.AUTHORIZATIONS)

        title = adb.get_modal_title()
        adb.close_modal()

        assert title == adb_const.People.AdditionalContent.Dropdown.AUTHORIZATIONS_TITLE

    def test_check_if_filter_and_search_work(self, admin_dashboard_setup):
        """
        Quick check if Filter and Search work
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_people_list()

        adb._find_field_and_enter_data(
            locator.AdminDashboardPage.PeopleList.SEARCH,
            adb_const.People.PeopleList.SEARCH)
        adb._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.SEARCH).send_keys(Keys.TAB)
        num = adb.get_num_elements(
            locator.AdminDashboardPage.PeopleList.LIST_ELEMENT)
        assert num == 1

        user_role_elt = adb._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.USER_ROLE)
        Select(user_role_elt).select_by_visible_text(
            adb_const.People.PeopleList.USER_ROLE)
        time.sleep(1)
        num = adb.get_menu_num_items(
            locator.AdminDashboardPage.HorizontalMenu.PEOPLE_ITEM)
        assert num == 0


class TestAdminDashboardRoles(AdminDashboardTestsBase):
    """
    Tests for roles tab
    """

    def test_check_items_presence(self, admin_dashboard_setup):
        """
        Click Roles tab in Horiz Nav bar -- confirm that you see:
        -- gGRC Admin role
        -- 3 system roles: Reader, Editor, Creator
        -- 2 WF roles: WorkflowMember, WorkflowManager

        -- Auditor role shouldn't be shown
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_roles()

        items = adb.get_all_items(
            locator.AdminDashboardPage.Roles.LIST,
            locator.AdminDashboardPage.Roles.LIST_ELEMENT,
            locator.AdminDashboardPage.Roles.LIST_ELEMENT_NAME)

        # check for items that must be present
        for item in adb_const.Roles.ITEMS_IN_LIST:
            assert item in items

        # check : -- Auditor role shouldn't be shown
        for item in adb_const.Roles.ITEMS_NOT_IN_LIST:
            assert not item in items

    def test_check_roles_are_not_editable(self):
        """
        You cannot edit the roles
        TODO
        """
        pass


class TestAdminDashboardEventLog(AdminDashboardTestsBase):
    """
    Tests for event log tab
    TODO: All tests
    """
    #from lib.page.modal import object_data

    def test_event_log(self, admin_dashboard_setup):
        """
        Create a program via accordion in LHN and map 4-5 objs to it,
        then delete the program. After that go back to admin dashboard
        and check the event log
        """
        return True
        adb = admin_dashboard_setup
        #hdr = header_setup
        adb.navigate_to()

        # Check number of events at beginning
        num_events_menu_start = adb.get_num_events_menu()

        # define test workflow
        _llhn = locator.LhnMenu
        map_flow = [
            [['issues'],
                _llhn.ISSUES_CONTAINER,
                _llhn.ISSUES_FIRST],
            [['assets', 'systems'],
                _llhn.ASSETS_BUSINESS_SYSTEMS_CONTAINER,
                _llhn.ASSETS_BUSINESS_SYSTEMS_FIRST],
            [['ppl_grp', 'people'],
                _llhn.PEOPLE_GROUPS_PEOPLE_CONTAINER,
                _llhn.PEOPLE_GROUPS_PEOPLE_FIRST],
            [['ctrl_obj', 'controls'],
                _llhn.CONTROLS_OBJECTIVES_CONTROLS_CONTAINER,
                _llhn.CONTROLS_OBJECTIVES_CONTROLS_FIRST]
        ]

        # prepare new program
        hdr = header.HeaderPage(adb._driver)
        self.lhn_menu = hdr.open_lhn_menu_new()
        self.lhn_menu._click_when_visible(locator.PageHeader.TRIGGER)

        self.lhn_menu.lhn_create_objects_setup('programs')
        identifier = self.lhn_menu.lhn_create_objects(
            'create_program', 'title', 1)
        prog_id = str(identifier[0])

        # store used ids of elements
        eids = []

        # map 4 items to program
        for elt in map_flow:
            if (len(elt[0]) == 1):
                self.lhn_menu.lhn_click_and_wait(elt[0][0])
            else:
                grp = str(elt[0][0])
                subgrp = str(elt[0][1])
                self.lhn_menu.lhn_create_objects_setup(grp, subgrp)

            time.sleep(1)

            #hover over first listed elt
            self.lhn_menu._get_element_when_visible(elt[1])
            self.lhn_menu._hover_when_present(elt[2])

            time.sleep(1)

            # get id of of element
            eid = hdr._get_element_when_visible(
                locator.LhnMenu.EXTENDED_INFO_TITLE).text
            eids.append(str(eid))

            # click on map to program
            hdr._get_element_when_visible(
                locator.LhnMenu.MAP_TO_PROGRAM_LINK).click()

            # hover somewhere out of hover window
            self.lhn_menu._hover_when_visible(locator.LhnMenu.ASSETS)

        self.lhn_menu.lhn_create_objects_setup('programs')
        self.lhn_menu.lhn_delete_objects(identifier)

        # Check number of events at end

        num_events_menu_end = adb.get_num_events_menu()

        ### - event log shows number of items in it

        assert num_events_menu_end >= num_events_menu_start + 6

        ### - items appear in chronological sequence
        ### - event log item should show what was done, by who and when
        # TODO: check "when"

        latest_events = adb.get_latest_events()

        # filter only events used by this test, still in cronological order
        prg_events = []
        for evt in latest_events:
            if (prog_id in str(evt)):
                prg_events.append(evt)


        assert len(prg_events) == 6

        # TODO: get username and usermail from site
        username = "Example User"
        usermail = "user@example.com"

        # check log line for program creation
        assert (prog_id                       in str(prg_events[5]))
        assert ("ProgramOwner in "            in str(prg_events[5]))
        assert ("mapped to " + usermail       in str(prg_events[5]))
        assert ("by " + username              in str(prg_events[5]))

        # check log line for event mappings
        assert (str(eids[0] + " mapped to " + prog_id + " by " + username)
                in str(prg_events[4]))
        assert (str(eids[1] + " mapped to " + prog_id + " by " + username)
                in str(prg_events[3]))
        assert (str(usermail + " mapped to " + prog_id + " by " + username)
                in str(prg_events[2]))
        assert (str(eids[3] + " mapped to " + prog_id + " by " + username)
                in str(prg_events[1]))

        # check log line for program deletion
        assert str(eids[0]) in str(prg_events[0])
        assert str(eids[1]) in str(prg_events[0])
        assert str(eids[2]) in str(prg_events[0])
        assert str(eids[3]) in str(prg_events[0])


    def test_events_next_prev_link(self, admin_dashboard_setup):
        """
        - Next page link is displayed at the bottom of the page
        - Click Next page
        -- the list of events is changing showing earlier records
        -- 'Previous page' link appears
        """
        adb = admin_dashboard_setup
        adb.navigate_to()

        ### UNREASONABLE BUT OTHERWISE click/next doesnt work on Chrome
        adb.open_people_list()
        num_people_real = adb.get_list_length_multipage(
            locator.AdminDashboardPage.PeopleList.LIST_ELEMENT)
        ###

        date_format = adb_const.EventLog.DATE_FORMATTING

        adb.open_event_log()

        date1 = adb._get_element_when_visible(
            locator.AdminDashboardPage.Events.FIRST_LIST_ELEMENT_DATE).text
        dt1 = datetime.strptime(date1[3:][:-4], date_format)

        adb.click_next_page_no_wait()

        date2 = adb._get_element_when_visible(
            locator.AdminDashboardPage.Events.FIRST_LIST_ELEMENT_DATE).text
        dt2 = datetime.strptime(date2[3:][:-4], date_format)

        assert dt1 > dt2

        adb._get_element_when_present(
          locator.AdminDashboardPage.PREVIOUS_PAGE)

class TestAdminDashboardCustomAttributes(AdminDashboardTestsBase):
    """
    Tests for custom attributes tab
    """

    def test_check_filter_presence_on_top(self, admin_dashboard_setup):
        """
        -- confirm you see the Filter at the top of the content are on this tab
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_custom_attributes()

        val = adb._get_element_when_visible(
            locator.AdminDashboardPage.CustomAttributes.FILTER).text
        assert val == adb_const.CustomAttributes.FILTER

    def test_check_items_presence(self, admin_dashboard_setup):
        """
        -- click custom attributes tab in Horiz Nav bar
        -- confirm that you see specified custom attributes
        -- Auditor role shouldn't be shown
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_custom_attributes()

        # make whole list fit
        for i in range(5):
            adb._get_element_when_visible(
                locator.Page.BODY).send_keys(Keys.CONTROL + '-')
        adb.reload_page()

        items = adb.get_all_items(
            locator.AdminDashboardPage.CustomAttributes.LIST,
            locator.AdminDashboardPage.CustomAttributes.LIST_ELEMENT,
            locator.AdminDashboardPage.CustomAttributes.LIST_ELEMENT_NAME)

        # check for items that must be present
        for item in adb_const.CustomAttributes.ITEMS_IN_LIST:
            assert item in items

        # check : -- Auditor role shouldn't be shown
        for item in adb_const.CustomAttributes.ITEMS_NOT_IN_LIST:
            assert not item in items

        for i in range(5):
            adb._get_element_when_visible(
                locator.Page.BODY).send_keys(Keys.CONTROL + '+')
        adb.navigate_to()


    def test_check_show_additional_data(self, admin_dashboard_setup):
        """
        Click ">" sign next to the item list title -- confirm the 2nd tier opens
        - confirm the second tier contains the table with the next headers
        -- Attribute name
        -- Attribute type
        -- Mandatory
        -- Edit
        :return:
        """
        adb = admin_dashboard_setup
        adb.navigate_to()
        adb.open_custom_attributes()
        adb._click_when_visible(
            locator.AdminDashboardPage.CustomAttributes.LEFT_ARROW)

        # -- the second tier of the tree view is opening

        adb._get_element_when_visible(
            locator.AdminDashboardPage.CustomAttributes.AdditionalContent.ADDITIONAL_DATA)

        items = adb.get_all_items(
            locator.AdminDashboardPage.CustomAttributes.AdditionalContent.LIST,
            locator.AdminDashboardPage.CustomAttributes.AdditionalContent.LIST_ELEMENT,
            locator.AdminDashboardPage.CustomAttributes.AdditionalContent.LIST_ELEMENT_NAME)

        # check for items that must be present
        for item in adb_const.CustomAttributes.AdditionalContent.ITEMS_IN_LIST:
            assert item in items

        #        """
        #        - TODO: the table contains the list of the custom attributes that were
        #        created (if any)
        #        - TODO: confirm the general look of the table isn't broken
        #        :return:
        #        """

        # - clicking (+) buttons opens "Add Attribute to type <object_title>" modal window

        adb._click_when_visible(
            locator.AdminDashboardPage.CustomAttributes.AdditionalContent.ADD_BUTTON)
        title = adb.get_modal_title()
        expected_title = adb_const.CustomAttributes.AdditionalContent.MODAL_ADD_TITLE
        assert title == expected_title
        adb.close_modal()

        # click edit button
        # TODO : fix if edit button is not present (add more data at init)

        #        adb._click_when_visible(
        #            locator.AdminDashboardPage.CustomAttributes.AdditionalContent.EDIT_BUTTON)
        #        title = adb.get_modal_title()
        #        expected_title = adb_const.CustomAttributes.AdditionalContent.MODAL_EDIT_TITLE
        #        assert title == expected_title
        #        adb.close_modal()


class TestAdminDashboardImportExport(AdminDashboardTestsBase):
    """
    Tests for import export tab
    """

    def test_check_click_on_data_export(self, import_export_setup):
        """
        In drop down menu click Data Export menu item
        -- the app redirects you to the Export page
        """
        ei = import_export_setup
        ei.navigate_to_dashboard_page()

        ei.open_user_dropdown_new()
        ei.click_on_data_export_menu_item()

        expected_url = environment.APP_URL + url.EXPORT
        assert ei._driver.current_url == expected_url

    def test_verify_export_import(self, import_export_setup):
        """
        Verify export and then re-import
        -- Systems
        -- Processes (optional)
        -- People (optional)
        (full import/export is covered on the other tab)
        """
        ei = import_export_setup
        ei.navigate_to_dashboard_page()

        ei.open_user_dropdown_new()
        ei.click_on_data_export_menu_item()

        ei._get_element_when_visible(
            locator.Export.ADD_ANOTHER)

        # first object type -- Systems

        sel1 = ei._get_element_when_visible(
            locator.Export.SELECT)
        Select(sel1).select_by_value(adb_const.Export.SELECT_SYSTEMS)

        # second object type -- Processes

        ei.click_add_another_object_type()
        sel2 = ei._get_element_when_visible(
            locator.Export.SELECT2)
        Select(sel2).select_by_value(adb_const.Export.SELECT_PROCESSES)

        # third object type -- People

        ei.click_add_another_object_type()
        sel3 = ei._get_element_when_visible(
            locator.Export.SELECT3)
        Select(sel3).select_by_value(adb_const.Export.SELECT_PEOPLE)

        # remove file from system

        os.system("rm " + adb_const.Import.CSV_FILENAME)

        # export to file

        ei._get_element_when_visible(
            locator.Export.EXPORT_OBJECTS).click()

        # Import csv back

        ei.navigate_to_dashboard_page()
        ei.open_user_dropdown_new()
        ei.click_on_data_import_menu_item()

        input_file = expanduser(adb_const.Import.CSV_FILENAME)
        input_file_elt = \
            ei._driver.find_element_by_css_selector(
                locator.Import.IMPORT_FILE[1])
        input_file_elt.send_keys(input_file)

        ei._get_element_when_clickable(
            locator.Import.IMPORT_BUTTON)
        ei._click_when_visible(locator.Import.IMPORT_BUTTON)

        btn_text = ei._get_element_when_clickable(
            locator.Import.IMPORT_BUTTON).text
        assert btn_text == adb_const.Import.IMPORT_SUCCESS
