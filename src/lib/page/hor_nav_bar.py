from lib import base
from lib.constants import locator
from lib.page.modal import create_object
import uuid
import time


class HorNavBar(create_object.NewObject):
    def click_ggrc_icon(self):
        self._click_when_visible(locator.HorNavBar.GGRC_ICON)

    def click_programs(self):
        self._click_when_visible(locator.HorNavBar.PROGRAMS)

    def click_program_title(self):
        self._click_when_visible(locator.HorNavBar.OBJECT_TITLE)

    def click_edit_program(self):
        self._click_when_visible(locator.HorNavBar.EDIT_PROGRAM)

    def enter_title(self, title):
        self._find_field_and_enter_data(
            locator.ModalCreateNewProgram.TITLE_UI, title)

    def click_close(self):
        self._click_when_visible(locator.HorNavBar.CLOSE_X)

    def wait_while_moving(self, selector):
        """
        Wait until an element is moving.

        Find out a location of an element. If it changes, wait 0.1 seconds
        and try again.

        Args:
            selector (string): If a locator is passed, use the second element
                               in the tuple - [1]
        """
        old_location = {}
        new_location = self._driver.find_elements_by_css_selector(
            selector)[0].location

        while old_location != new_location:
            temp_location = new_location
            time.sleep(0.1)  # Pass time between old and new location
            new_location = self._driver.find_elements_by_css_selector(
                selector)[0].location
            old_location = temp_location
        # self.click_object(locator)

    def start_new_program(self, num_of_programs):
        """
        Creates a new program in Hor Nav Bar.

        Args:
            num_of_programs (integer): The number of programs to create
        """
        self._click_when_visible(locator.HorNavBar.START_NEW_PROGRAM)
        identifier = []

        for i in xrange(num_of_programs):
            _identifier = str(uuid.uuid4())
            self.enter_title(_identifier)

            if i != xrange(num_of_programs)[-1]:
                self.save_and_add_other()
                save_and_add = self._driver.find_elements_by_css_selector(
                    locator.ModalCreateNewProgram.BUTTON_SAVE_AND_ADD[1]
                    )[0].get_attribute("outerHTML")

                while 'pending-ajax' in save_and_add:
                    time.sleep(0.1)
                    save_and_add = self._driver.find_elements_by_css_selector(
                        locator.ModalCreateNewProgram.BUTTON_SAVE_AND_ADD[1]
                        )[0].get_attribute("outerHTML")
            else:
                self.save_and_close()
                self.wait_for_redirect()

            # The identifier stores UUIDs for lhn_delete_objects method
            identifier.append(_identifier)
        return identifier

    def hor_nav_bar_delete(self, ident):
        """
        Delets the desired programs in Hor Nav Bar.

        Args:
            ident (list): list of UUID identifiers to delete
        """
        self.click_ggrc_icon()
        self.click_programs()

        self._get_element_when_visible(locator.HorNavBar.OBJECT_TITLE)
        elements = self._driver.find_elements_by_css_selector(
            locator.HorNavBar.OBJECT_TITLE[1])

        i = 0
        while len(ident) > 0:
            element = elements[i]
            if element.text in ident:
                element.click()

                # Waits while the gear icon is still moving.
                self.wait_while_moving(
                    locator.ModalCreateNewProgram.GEAR_ICON[1])

                self.click_gear_icon()
                self.click_delete_gear_icon()
                self.click_delete()

                ident.remove(element.text)

                time.sleep(2)

                if len(ident) != 0:
                    self._get_element_when_visible(
                        locator.HorNavBar.OBJECT_TITLE)
                    elements = self._driver.find_elements_by_css_selector(
                        locator.HorNavBar.OBJECT_TITLE[1])
                i = -1
            i += 1

    def confirm_deletion(self, ident):
        """
        Confirms that programs have been deleted in Hor Nav Bar.

        Args:
            ident (list): list of UUID identifiers to check
        """
        self.click_ggrc_icon()
        self.click_programs()

        self._get_element_when_visible(locator.HorNavBar.OBJECT_TITLE)
        elements = self._driver.find_elements_by_css_selector(
            locator.HorNavBar.OBJECT_TITLE[1])
        i = 0
        while True:
            try:
                element = elements[i]
            except IndexError:
                break

            # If an ident's UUID is still in the elements list,
            # it wasn't deleted.
            assert element not in ident, 'Element was not deleted.'
            i += 1
