from lib.constants import locator
from lib import base
from lib.page.modal.object_data import obj_create
import time


class Helper(base.Page):
    def expand_lhn(self, driver, xoffset=150):
        """
        Expands the LHN menu by xoffset.

        Usable when some elements are hidden, like the number of elements
        in the bracket of control assessments.

        Args:
            driver (webdriver): Selenium webdriver
            xoffset (int): X offset to move to
        """
        from selenium.webdriver.common.action_chains import ActionChains

        element = driver.find_elements_by_css_selector(
            locator.LhnMenu.BAR_V[1])[0]

        ActionChains(driver).drag_and_drop_by_offset(
            element, xoffset, 0).perform()

    def check_if_lhn_open(self, driver):
        """
        Checks if the LHN menu is opend. If it's not, open it.

        Args:
            driver (webdriver): Selenium webdriver
        """
        lhn = driver.find_elements_by_css_selector(
            locator.PageHeader.TRIGGER[1]
            )[0].get_attribute("class")

        if 'active' not in lhn:
            self._get_element_when_clickable(
                locator.PageHeader.TRIGGER).click()

    def wait_while_moving(self, driver, string):
        """
        Wait until an element is moving.

        Find out a location of an element. If it changes, wait 0.1 seconds
        and try again.

        Args:
            string (string): Selector or locator
        """
        from selenium.common.exceptions import InvalidSelectorException

        old_location = {}
        try:
            new_location = driver.find_elements_by_css_selector(
                string)[0].location
        except InvalidSelectorException:
            new_location = driver.find_elements_by_css_selector(
                string[1])[0].location

        while old_location != new_location:
            temp_location = new_location
            time.sleep(0.1)  # Pass time between old and new location
            try:
                new_location = driver.find_elements_by_css_selector(
                    string)[0].location
            except InvalidSelectorException:
                new_location = driver.find_elements_by_css_selector(
                    string[1])[0].location
            old_location = temp_location
        # self.click_object(locator)

    def wait_while_pending(self, driver, selector, keyword, IN, attr='class'):
        """
        Wait while connecting to database.

        Args:
            driver (webdriver): Selenium webdriver
            selector (string): selector == locator[1]
            keyword (string): The keyword to search for in the attribute
            IN (string): if IN == 'in' -> keyword: in, else -> keyword: not in
            attr (string): The attribute in which to search
        """
        wait_for = driver.find_elements_by_css_selector(
            selector)[0].get_attribute(attr)

        if IN == 'in':
            while keyword in wait_for:
                time.sleep(0.1)
                wait_for = driver.find_elements_by_css_selector(
                    selector)[0].get_attribute(attr)
        else:
            while keyword not in wait_for:
                time.sleep(0.1)
                wait_for = driver.find_elements_by_css_selector(
                    selector)[0].get_attribute(attr)

    def lhn_click_and_wait(self, obj):
        """
        This is a helper method for object creation in LHN menu.

        Method waits for the LHN menu to complete an action.
        Example: opens the LHN menu, opens a dropdown menu (+ create new).

        Note: Method should NOT use time.sleep.

        Args:
            obj (locator): src.lib.page.lhn_menu
        """
        time.sleep(3)
        self._click_when_visible(obj_create[obj])
        # self.click_object(obj)

        # ALTERNATIVE:
        # Web driver exception: element not clicable at point (chrome driver).
        # Errors: Constantly clicks on random elements.
        #
        # while True:
        #     try:
        #         self.click_create_new_object(obj)
        #         break
        #     except:
        #         pass # or time.sleep(0.1)

        # ALTERNATIVE #2:
        # The code below waits for the element (in LHN menu) to stop moving.
        # (Possible) Errors: Clicks on random objects are possible while the
        # LHN waits for objects to fully load before clicking on +Create New.
        #
        # old_location = {}
        # new_location = self.wait_while_moving(obj)[0].location
        # # new_location = self.driver.find_elements_by_css_selector ...
        #
        # while old_location != new_location:
        #     temp_location = new_location
        #     time.sleep(0.1) # Pass time between old and new location
        #     new_location = self.wait_while_moving(
        #         obj)[0].location
        #     old_location = temp_location
        # self.click_object(obj)

    def lhn_elements_count(self, driver):
        from selenium.common.exceptions import StaleElementReferenceException
        count = 0
        while True:
            old_count = count

            # selector = locator.LhnMenu.LHS_CONTENT[1]
            # driver.execute_script(
            #     "$(\"" + selector +
            #     "\").animate({ scrollTop: \"1000000px\" })")

            element = self._get_element_when_present(
                locator.LhnMenu.LAST_LHN_OBJECT)
            driver.execute_script("arguments[0].scrollIntoView();", element)

            while True:
                try:
                    self.wait_while_moving(
                        driver, locator.ModalCreateNewObject.LHS_ITEM)
                    break
                except StaleElementReferenceException:
                    time.sleep(0.1)

            try:
                driver.find_elements_by_css_selector(
                    locator.LhnMenu.WAIT_FOR_ITEMS[1])[0].is_displayed()
                time.sleep(0.1)
                count += 1
            except:
                elements_count = driver.find_elements_by_css_selector(
                    locator.ModalCreateNewObject.LHS_ITEM[1])
                if old_count == count:
                    break

        return elements_count
