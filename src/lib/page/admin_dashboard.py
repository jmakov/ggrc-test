from lib import constants, environment
from lib.constants import locator
from lib.page import widget_bar, header, dashboard
from lib import base
from lib import exception
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.common import string_utils

stru = string_utils()


class AdminDashboardPage(base.Page):
    """
    Admin dashboard page class
    """

    def navigate_to(self):
        """
        Open page
        """
        self._driver.get(environment.APP_URL + constants.url.ADMIN_DASHBOARD)

    def click_add_new_person(self):
        """
        Click on add new person element
        """
        self._click_when_visible(
            locator.AdminDashboardPage.PeopleList.ADD_PERSON)

    def enter_add_person_data_and_save(self, name, email, company):
        """
        Add person and data
        To use it, you first need to call
            self.adb_page.click_add_new_person()
        """
        self._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.AddPerson.NAME)
        self._find_field_and_enter_data(
            locator.AdminDashboardPage.PeopleList.AddPerson.NAME, name)
        self._find_field_and_enter_data(
            locator.AdminDashboardPage.PeopleList.AddPerson.EMAIL, email)
        self._get_element_when_visible(
            locator.AdminDashboardPage.PeopleList.AddPerson.EMAIL).send_keys(
                Keys.TAB)
        self._find_field_and_enter_data(
            locator.AdminDashboardPage.PeopleList.AddPerson.COMPANY, company)
        self._click_when_visible(
            locator.AdminDashboardPage.PeopleList.AddPerson.ADDMORE)

    def close_modal(self):
        """
        Close modal window
        """
        self._click_when_visible(locator.Modal.CLOSE)

    def get_modal_title(self):
        """
        Get title of modal window
        """
        self._get_element_when_visible(locator.Modal.BUTTON_SUCCESS)
        text = self._get_element_when_visible(locator.Modal.TITLE).text
        return text

    def click_arrow_in_first_tier(self):
        """
        - click > in the first tier
        """
        self._click_when_visible(
            locator.AdminDashboardPage.PeopleList.FirstItem.LEFT_ARROW)

    def click_next_page_no_wait(self):
        """
        Click next page in list
        """
        loc = locator.AdminDashboardPage.NEXT_PAGE
        self.scroll_to_bottom()
        elts = []
        try:
            elts = self._driver.find_elements(loc[0], loc[1])
        except NoSuchElementException:
            raise exception.ElementNotFound(loc)
            return

        if len(elts) > 0 :
            self._click_when_visible(loc)
        else:
            raise exception.ElementNotFound(loc)

    def click_next_page(self):
        """
        Click next page in list
        """
        self._click_when_present(locator.AdminDashboardPage.NEXT_PAGE)

    def click_previous_page(self):
        """
        Click previous page in list
        """
        self._click_when_present(locator.AdminDashboardPage.PREVIOUS_PAGE)

    def get_menu_num_items(self, locator):
        """
        Get number of menu items from number in brackets of menu link
        """
        num = stru.get_num_in_brackets(self._get_element_when_clickable(
            locator).text)
        return num

    def get_list_length_multipage(self, locator):
        """
        Get length of a list by opening all next page links on bottom of page
        """
        num_real = 0
        while True:
            pg_num_real = self.get_num_elements(locator)
            num_real += pg_num_real
            try:
                self.click_next_page_no_wait()
            except exception.ElementNotFound:
                break
            except NoSuchElementException:
                break

        return num_real

    def open_people_list(self):
        """
        Open people list
        """
        self._click_when_visible(
            locator.AdminDashboardPage.HorizontalMenu.PEOPLE_ITEM)

    def open_roles(self):
        """
        Open roles list
        """
        self._click_when_visible(
            locator.AdminDashboardPage.HorizontalMenu.ROLES_ITEM)

    def open_event_log(self):
        """
        Open event log tab
        """
        self._click_when_visible(
            locator.AdminDashboardPage.HorizontalMenu.EVENTS_ITEM)

    def get_num_events_menu(self):
        """
        Get number of events from event menu
        """
        self.navigate_to()
        self._get_element_when_clickable(
            locator.AdminDashboardPage.HorizontalMenu.EVENTS_ITEM)
        return self.get_menu_num_items(
            locator.AdminDashboardPage.HorizontalMenu.EVENTS_ITEM)

    def get_latest_events(self):
        """
        Get first page of event list
        """
        self.navigate_to()
        self.open_event_log()
        return self.get_all_items(locator.AdminDashboardPage.Events.LIST,
            locator.AdminDashboardPage.Events.LIST_ELEMENT,
            locator.AdminDashboardPage.Events.LIST_ELEMENT_NAME)

    def open_custom_attributes(self):
        """
        Open custom attributes list
        """
        self.navigate_to()
        self._click_when_visible(
            locator.AdminDashboardPage.HorizontalMenu.CUSTOM_ATTRIBUTES_ITEM)

    def get_num_elements(self, locator):
        """
        Get number of elements for locator
        """
        # wait for the element to show up
        try:
            self._get_element_when_visible(locator)
        except TimeoutException:
            return 0
        elements = self._driver.find_elements(locator[0], locator[1])
        num_elements = len(elements)
        return num_elements

    def get_all_items(self, ul_locator, li_locator, sub_li_locator):
        """
        Get all items in list
        """
        # wait until ul_selector is visible
        self._get_element_when_visible(ul_locator)

        ## wait until li_selector is visible
        self._get_element_when_visible(li_locator)

        # get number of all elements in list
        elements = self._driver.find_elements(sub_li_locator[0],
                                              sub_li_locator[1])
        num_elements = len(elements)

        elements_str_arr = []
        for idx in xrange(0, num_elements):
            val = elements[idx].text
            elements_str_arr.append(val)

        return elements_str_arr

class ExportImportPage(dashboard.DashboardPage):
    """
    Export and Import page class
    """

    def navigate_to_dashboard_page(self):
        """
        Open dashboard
        """
        self.navigate_to(self.URL)

    def click_on_data_export_menu_item(self):
        """
        Click on user menu item for data export
        """
        self._get_element_when_visible(
            locator.DropdownToggle.DATA_EXPORT).click()

    def click_on_data_import_menu_item(self):
        """
        Click on user menu item for data export
        """
        self._get_element_when_visible(
            locator.DropdownToggle.DATA_IMPORT).click()

    def click_add_another_object_type(self):
        """
        Click on add another object type button
        """
        #self._click_when_visible(self.ADD_ANOTHER)
        self._get_element_when_visible(locator.Export.ADD_ANOTHER).click()

    def click_export_objects(self):
        """
        Click export objects button
        """
        self._get_element_when_visible(locator.Export.EXPORT_OBJECTS).click()

    def click_import_objects(self):
        """
        Click import objects button
        """
        self._get_element_when_visible(locator.Import.IMPORT_OBJECTS).click()
