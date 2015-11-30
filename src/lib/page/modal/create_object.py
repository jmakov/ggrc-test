from lib.constants import locator
from lib import base
from lib.page.modal import object_data
import uuid
import time


class NewObject(base.Page, object_data.ObjectData):
    def open_lhn_menu(self):
        self._click_when_visible(locator.PageHeader.TRIGGER)

    def click_object(self, obj):
        self._click_when_visible(self.obj_create[obj])

    def click_create_new_object(self, obj):
        self._click_when_visible(self.obj_create[obj])

    def enter_title(self, obj, title):
        self._find_field_and_enter_data(self.obj_create[obj], title)

    def save_and_add_other(self):
        self._click_when_visible(
            locator.ModalCreateNewProgram.BUTTON_SAVE_AND_ADD)

    def save_and_close(self):
        self._click_when_visible(
            locator.ModalCreateNewProgram.BUTTON_SAVE_AND_CLOSE_UI)

    def click_gear_icon(self):
        self._click_when_visible(locator.ModalCreateNewProgram.GEAR_ICON)

    def click_delete_gear_icon(self):
        self._click_when_visible(locator.ModalCreateNewProgram.DELETE_IN_GEAR)

    def click_delete(self):
        self._click_when_visible(locator.ModalCreateNewProgram.DELETE)

    def click_workflows_draft(self):
        self._click_when_visible(locator.ModalCreateNewWorkflow.WF_DRAFT)

    def element_in_bracket(self, obj):
        return self._driver.find_elements_by_css_selector(self.obj_create[obj])

    def enter_data(self, data):
        self._find_iframe_and_enter_data(
            locator.ModalCreateNewRisk.RISK_DESCRIPTION, data)

    def wait_while_lhn_moving(self, obj):
        # return self._get_element_when_visible(self.obj_create[obj])
        return self._driver.find_elements_by_css_selector(self.obj_create[obj])

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
        self.click_object(obj)

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
        # new_location = self.wait_while_lhn_moving(obj)[0].location
        # # new_location = self.driver.find_elements_by_css_selector ...
        #
        # while old_location != new_location:
        #     temp_location = new_location
        #     time.sleep(0.1) # Pass time between old and new location
        #     new_location = self.wait_while_lhn_moving(
        #         obj)[0].location
        #     old_location = temp_location
        # self.click_object(obj)

    def lhn_create_objects_setup(self, *args):
        """
        Opens LHN menu and clicks on an object to create a new one.

        Navigates to the correct +Create New element. If the object is in the
        OBJECTS submenu (DIRECTIVES, CONTROLS/OBJECTIVES ...), two clicks are
        needed for navigation (two arguments).

        Args:
            *args (strings): point to locators in object_data
        """
        # lhn (variable): if LHN menu isn't open, open it
        lhn = self._driver.find_elements_by_css_selector(
            locator.PageHeader.TRIGGER[1]
            )[0].get_attribute("outerHTML").split('>')[0]
        if 'active' not in lhn:
            self.open_lhn_menu()

        # Click on the arrow of an object (ex: PROGRAMS (NUM))
        for obj_link in args:
            self.lhn_click_and_wait(obj_link)

    def lhn_create_objects(
            self, create_obj, enter_title, obj_num, obj_id=None):
        """
        Creates an object in LHN menu.

        Note: Locators in src.lib.page.lhn_menu

        Args:
            create_obj (string): Locator for click +Create New in object_data
            enter_title (string): Locator for enter title (email for people)
            obj_num (int): the number of objects to create
            obj_id (string): if used when calling - UUID string, else None
        """
        select_obj = {
            'create_audit': 'program_checkbox',
            'create_section': 'policy_checkbox',
            'create_risk': 'risk_owner'
        }

        self.lhn_click_and_wait(create_obj)

        # The identifier stores UUIDs for lhn_delete_objects method
        self.identifier = []

        # For loop creates the number of objects specified by obj_num
        for i in xrange(obj_num):
            _identifier = str(uuid.uuid4())

            # If creating audits, sections or risks
            if create_obj in select_obj.keys():
                if create_obj == 'create_risk':
                    self.enter_data(_identifier)
                j = 0
                while True:
                    self.click_object(select_obj[create_obj])

                    # Find all elements in dropdown list
                    self._get_element_when_visible(
                        locator.ModalCreateNewAudit.SELECT_PROGRAM)
                    elements = self._driver.find_elements_by_css_selector(
                        locator.ModalCreateNewAudit.SELECT_PROGRAM[1])

                    element = elements[j]
                    e = element.text

                    # If creating risks, just select the firs Owner in list
                    if create_obj == 'create_risk':
                        element.click()
                        break

                    # Click on the element by secific UUID
                    # Exemple: If creating audits, a program UUID is used
                    elif e in obj_id:
                        element.click()
                        break
                    j += 1

            # If creating a person, append @example.com, else just use UUID
            if enter_title != 'person_email':
                self.enter_title(enter_title, _identifier)
            else:
                self.enter_title(
                    enter_title, _identifier + '@example.com')

            # Control assessments NOT working
            if create_obj == 'create_ctrl_asses':
                ctrl_asses_key = ('control_checkbox', 'audit_checkbox')

                old_elements = []
                for j in xrange(2):
                    k = 0
                    self.click_object(ctrl_asses_key[j])
                    self._get_element_when_visible(
                        locator.ModalCreateNewAudit.SELECT_PROGRAM)
                    # time.sleep(2)
                    elements = self._driver.find_elements_by_css_selector(
                        locator.ModalCreateNewAudit.SELECT_PROGRAM[1])
                    while True:
                        element = elements[k]
                        e = element.text
#                         if ctrl_asses_key[j] == 'audit_checkbox':
#                             element.click()
#                             break
#                         if e in obj_id:
#                             element.click()
                        if element not in old_elements:
                            old_elements = elements
                            element.click()
                            break
                        k += 1

            # Save & Add Another - as long as range isn't on the last index
            if i != xrange(obj_num)[-1]:
                self.save_and_add_other()
                save_and_add = self._driver.find_elements_by_css_selector(
                    locator.ModalCreateNewProgram.BUTTON_SAVE_AND_ADD[1]
                    )[0].get_attribute("outerHTML")

                # While Save & Add Another not clickable again
                while 'pending-ajax' in save_and_add:
                    time.sleep(0.1)
                    save_and_add = self._driver.find_elements_by_css_selector(
                        locator.ModalCreateNewProgram.BUTTON_SAVE_AND_ADD[1]
                        )[0].get_attribute("outerHTML")

            # Save & Close
            else:
                self.save_and_close()
                # self.wait_for_redirect()

            # The identifier stores UUIDs for lhn_delete_objects method
            self.identifier.append(_identifier)

        time.sleep(1)
        # lhn (variable): if LHN menu isn't open, open it
        lhn = self._driver.find_elements_by_css_selector(
            locator.PageHeader.TRIGGER[1]
            )[0].get_attribute("outerHTML").split('>')[0]
        if 'active' not in lhn:
            self.open_lhn_menu()

        # Return currently broken (returns None)
        return self.identifier

    def lhn_count_objects(self, obj):
        """
        Counts elements in LHN menu and compares that number
        to the number in brackets.
        Args:
            obj (string): Selector in object_data for elements in brackets
        """
        # If countng workflows, click on draft first
        if obj == 'workflows_count':
            self.click_workflows_draft()

        time.sleep(2)

        # Get the list of all elements in LHN menu
        self._get_element_when_visible(
            locator.ModalCreateNewProgram.LHS_ITEM_NEW)
        elements_count = self._driver.find_elements_by_css_selector(
            locator.ModalCreateNewProgram.LHS_ITEM_NEW[1])

        # Element in bracket
        element = self.element_in_bracket(obj)[0].text

        assert len(elements_count) <= int(element), \
            'Elements in brackets must be higer or equal to the counted ' \
            'elements'

    def lhn_delete_objects(self, ident, obj=None):
        """
        Deletes all the objects that have been created with the
        lhn_create_objects method.

        Args:
            ident (string): UUID of the created object
            obj (string): navigate to different object to delete it (see Exapl)
        """
        # lhn (variable): if LHN menu isn't open, open it
        lhn = self._driver.find_elements_by_css_selector(
            locator.PageHeader.TRIGGER[1]
            )[0].get_attribute("outerHTML").split('>')[0]
        if 'active' not in lhn:
            self.open_lhn_menu()

        # Exapl: In audits, delete the program's UUID used to create
        #        the audits and all audits will be deleted.
        obj_link = ('programs', 'policies')
        if obj in obj_link:
            self.click_object(obj)

        time.sleep(1)

        # Get the list of all elements in LHN menu
        self._get_element_when_visible(
            locator.ModalCreateNewProgram.LHS_ITEM_NEW)
        elements_count = self._driver.find_elements_by_css_selector(
            locator.ModalCreateNewProgram.LHS_ITEM_NEW[1])

        i = 0
        while len(ident) > 0:
            # If the element in the list has the same UUID as one of the
            # ident's, delete it and remove the UUID form the ident.
            # Loop until ident is an empty list.
            element = elements_count[i]

            if element.text in ident:
                ident.remove(element.text)
                while True:
                    try:
                        element.click()
                        break
                    except:
                        time.sleep(0.1)
                self.click_gear_icon()
                self.click_delete_gear_icon()
                self.click_delete()
                self.wait_for_redirect()

                if len(ident) != 0:
                    time.sleep(1)
                    # lhn (variable): if LHN menu isn't open, open it
                    lhn = self._driver.find_elements_by_css_selector(
                        locator.PageHeader.TRIGGER[1]
                        )[0].get_attribute("outerHTML").split('>')[0]
                    if 'active' not in lhn:
                        self.open_lhn_menu()

                    # Get the list of all elements in LHN menu
                    # The list need to be recreated every time and element is
                    # deleted or an exception will accrue.
                    self._get_element_when_visible(self.LHS_ITEM_NEW)
                    elements_count = self._driver \
                        .find_elements_by_css_selector(
                            locator.ModalCreateNewProgram.LHS_ITEM_NEW[1])
                i = -1
            i += 1
