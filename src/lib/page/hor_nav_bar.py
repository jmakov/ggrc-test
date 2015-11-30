from lib import helper_methods
from lib.constants import locator
import uuid
import time


class HorNavBar(helper_methods.Helper):
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
            self._find_field_and_enter_data(
                locator.ModalCreateNewProgram.TITLE_UI, _identifier)

            if i != xrange(num_of_programs)[-1]:
                self._click_when_visible(
                    locator.ModalCreateNewObject.BUTTON_SAVE_AND_ADD)

                # Wait while "Save & Add Another" button is not clickabe
                self.wait_while_pending(
                    self._driver,
                    locator.ModalCreateNewObject.BUTTON_SAVE_AND_ADD[1],
                    'pending-ajax', 'in')

            # Save & Close
            else:
                self._click_when_visible(
                    locator.ModalCreateNewObject.BUTTON_SAVE_AND_CLOSE)
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
        self._click_when_visible(locator.HorNavBar.GGRC_ICON)
        self._click_when_visible(locator.HorNavBar.PROGRAMS)

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
                    self._driver, locator.ModalCreateNewObject.GEAR_ICON[1])

                self._click_when_visible(
                    locator.ModalCreateNewObject.GEAR_ICON)
                self._click_when_visible(
                    locator.ModalCreateNewObject.DELETE_IN_GEAR)
                self._click_when_visible(locator.ModalCreateNewObject.DELETE)

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
        time.sleep(2)
        self._click_when_visible(locator.HorNavBar.GGRC_ICON)
        self._click_when_visible(locator.HorNavBar.PROGRAMS)

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

    def hor_nav_bar_delete_objects(self):
        while True:
            self._get_element_when_visible(locator.HorNavBar.OBJECT_TITLE)
            elements = self._find_element_by_css(
                locator.HorNavBar.OBJECT_TITLE)
            elements[0].click()
            self.wait_while_moving(
                self._driver, locator.ModalCreateNewObject.GEAR_ICON[1])
            self._click_when_visible(locator.HorNavBar.OBJECT_TITLE)
            self._click_when_visible(locator.ModalCreateNewObject.GEAR_ICON)
            self._click_when_visible(
                locator.ModalCreateNewObject.DELETE_IN_GEAR)
            self._click_when_visible(locator.ModalCreateNewObject.DELETE)
            time.sleep(2)
