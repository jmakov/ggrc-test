from lib.constants import locator
from lib import helper_methods
from lib.page.modal.object_data import obj_create
import uuid
import time


class NewObject(helper_methods.Helper):
    def lhn_create_objects_setup(self, *args):
        """
        Opens LHN menu and clicks on an object to create a new one.

        Navigates to the correct +Create New element. If the object is in the
        OBJECTS submenu (DIRECTIVES, CONTROLS/OBJECTIVES ...), two clicks are
        needed for navigation (two arguments).

        Args:
            *args (strings): point to locators in object_data
        """
        # If LHN menu isn't open, open it and wait while its moving
        self.check_if_lhn_open(self._driver)
        self.wait_while_moving(self._driver, locator.LhnMenu.LHN_PIN)

        # Click on the arrow of an object (ex: PROGRAMS (NUM))
        for obj_link in args:
            self.lhn_click_and_wait(obj_link)

    def lhn_create_objects(self, create_obj, obj_num, *args):
        """
        Creates an object in LHN menu.

        Note: Locators in src.lib.page.lhn_menu

        Args:
            create_obj (string): Locator for click +Create New in object_data
            # enter_title (string): Locator for enter title (email for people)
            obj_num (int): the number of objects to create
            obj_id (string): if used when calling - UUID string, else None
        """
        # If LHN menu isn't open, open it and wait while its moving
        self.check_if_lhn_open(self._driver)
        self.wait_while_moving(self._driver, locator.LhnMenu.LHN_PIN)

        select_obj = {
            'create_audit': 'program_checkbox',
            'create_section': 'policy_checkbox',
            # 'create_risk': 'risk_owner'
        }

        self.lhn_click_and_wait(create_obj)

        # self._click_when_visible(locator.LhnMenu.HIDE_OPTIONAL)

        # The identifier stores UUIDs for lhn_delete_objects method
        identifier = []

        # For loop creates the number of objects specified by obj_num
        for i in xrange(obj_num):
            _identifier = str(uuid.uuid4())

            # If creating audits, sections or risks
            if create_obj in select_obj.keys():
#                 if create_obj == 'create_risk':
#                     self._find_iframe_and_enter_data(
#                         locator.ModalCreateNewRisk.RISK_DESCRIPTION,
#                         _identifier)
                j = 0
                while_not_false = True
                while while_not_false:
                    self._click_when_visible(
                        obj_create[select_obj[create_obj]])

                    # Find all elements in dropdown list
                    self._get_element_when_visible(
                        locator.ModalCreateNewAudit.SELECT_PROGRAM)
                    elements = self._driver.find_elements_by_css_selector(
                        locator.ModalCreateNewAudit.SELECT_PROGRAM[1])

                    while True:
                        try:
                            element = elements[j]
                            break

                        except:
                            element = self._get_element_when_present(
                                locator.ModalCreateNewObject.LAST_MODAL_OBJECT)
                            self._driver.execute_script(
                                "arguments[0].scrollIntoView();", element)
                            time.sleep(2)
                            j = -1

                    e = element.text

                    # If creating risks, just select the firs Owner in list
                    if create_obj == 'create_risk':
                        element.click()
                        while_not_false = False

                    # Click on the element by secific UUID
                    # Exemple: If creating audits, a program UUID is used
                    for arg in args:
                        if e in arg:
                            element.click()
                            while_not_false = False
                            break
                    j += 1

            # If creating a person, append @example.com, else just use UUID
            if create_obj == 'create_person':
                self._find_field_and_enter_data(
                    obj_create['person_email'], _identifier + '@example.com')
                self._find_field_and_enter_data(
                    obj_create['person_name'], _identifier)

            elif create_obj == 'create_threat_actor':
                self._find_field_and_enter_data(
                    obj_create['threat_actor_title'], _identifier)

            elif create_obj == 'create_risk':
                self._find_field_and_enter_data(
                    obj_create['risk_title'], _identifier)
                self._find_iframe_and_enter_data(
                    locator.ModalCreateNewRisk.RISK_DESCRIPTION,
                    _identifier)

            elif create_obj == 'create_audit':
                element = self._get_element_when_visible(obj_create['title'])
                time.sleep(0.1)
                element.clear()
                self._get_element_when_visible(obj_create['title']
                                               ).send_keys(_identifier)

            elif create_obj == 'create_program':
                self._find_field_and_enter_data(
                    locator.ModalCreateNewProgram.TITLE_UI, _identifier)
            else:
                self._find_field_and_enter_data(
                    obj_create['title'], _identifier)

            # Control assessments NOT working
            if create_obj == 'create_ctrl_asses':
                ctrl_asses_key = ('audit_checkbox', 'control_checkbox')

                for j in xrange(2):
                    k = 0
                    self._click_when_visible(obj_create[ctrl_asses_key[j]])

                    if ctrl_asses_key[j] == 'control_checkbox':
                        self._get_element_when_visible(
                            locator.ModalCreateNewControlAsses.SELECT_OTHER)
                        elements = self._driver.find_elements_by_css_selector(
                            locator.ModalCreateNewControlAsses
                            .SELECT_OTHER[1])

                    else:
                        self._get_element_when_visible(
                            locator.ModalCreateNewAudit.SELECT_PROGRAM)
                        elements = self._driver.find_elements_by_css_selector(
                            locator.ModalCreateNewAudit.SELECT_PROGRAM[1])

                    while True:
                        element = elements[k]
                        e = element.text

                        if ctrl_asses_key[j] == 'control_checkbox':
                            if args[0] in e:
                                element.click()
                                break
                        else:
                            if args[1] in e:
                                element.click()
                                break
                        k += 1
            # Save & Add Another - as long as range isn't on the last index
            if i != xrange(obj_num)[-1]:
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

            time.sleep(2)
            # The identifier stores UUIDs for lhn_delete_objects method
            identifier.append(_identifier)

        return identifier

    def lhn_count_objects(self, obj):
        """
        Counts elements in LHN menu and compares that number
        to the number in brackets.
        Args:
            obj (string): Selector in object_data for elements in brackets
        """
        time.sleep(2)
        # Click the gGRC Icon (right from LHN menu)
        self._click_when_visible(locator.HorNavBar.GGRC_ICON)

        # If LHN menu isn't open, open it and wait while its moving
        self.check_if_lhn_open(self._driver)
        self.wait_while_moving(self._driver, locator.LhnMenu.LHN_PIN)

        # If counting workflows, click on draft first
        if obj == 'workflows_count':
            self._click_when_visible(locator.ModalCreateNewWorkflow.WF_DRAFT)

        # If counting control assessments, expand LHN menu
        if obj == 'ctrl_asses_count':
            self.expand_lhn(self._driver)

        time.sleep(2)

        # Element in bracket
        element = self._driver.find_elements_by_css_selector(
            obj_create[obj])[0].text

        # Get the list of all elements in LHN menu
#         self._get_element_when_visible(
#             locator.ModalCreateNewObject.LHS_ITEM)
#         elements_count = self._driver.find_elements_by_css_selector(
#             locator.ModalCreateNewObject.LHS_ITEM[1])
        elements_count = self.lhn_elements_count(self._driver)

        assert len(elements_count) == int(element), \
            'Elements in brackets must be equal to the counted elements'

    def lhn_delete_objects(self, ident, *args):
        """
        Deletes all the objects that have been created with the
        lhn_create_objects method.

        Args:
            ident (string): UUID of the created object
            obj (string): navigate to different object to delete it (see Exapl)
        """
        # If LHN menu isn't open, open it and wait while its moving
        self.check_if_lhn_open(self._driver)
        self.wait_while_moving(self._driver, locator.LhnMenu.LHN_PIN)

        # Exapl: In audits, delete the program's UUID used to create
        #        the audits and all audits will be deleted.
        obj_link = ('programs', 'policies', 'ctrl_asses')
        for arg in args:
            if arg in obj_link:
                self._click_when_visible(obj_create[arg])
                time.sleep(2)
                # Click the gGRC Icon (right from LHN menu)
                self._click_when_visible(locator.HorNavBar.GGRC_ICON)
                # If LHN menu isn't open, open it and wait while its moving
                self.check_if_lhn_open(self._driver)
                self.wait_while_moving(self._driver, locator.LhnMenu.LHN_PIN)

        obj_link2 = ('ctrl_obj', 'controls')
        for arg in args:
            if arg in obj_link2:
                self._click_when_visible(obj_create[arg])
                time.sleep(2)
                if arg == 'controls':
                    # Click the gGRC Icon (right from LHN menu)
                    self._click_when_visible(locator.HorNavBar.GGRC_ICON)
                    # If LHN menu isn't open, open it and wait while its moving
                    self.check_if_lhn_open(self._driver)
                    self.wait_while_moving(
                        self._driver, locator.LhnMenu.LHN_PIN)

        time.sleep(1)

        i = 0
        while len(ident) > 0:
            # If the element in the list has the same UUID as one of the
            # ident's, delete it and remove the UUID form the ident.
            # Loop until ident is an empty list.

            # Get the list of all elements in LHN menu
            self._get_element_when_visible(
                locator.ModalCreateNewObject.LHS_ITEM)
            elements_count = self._driver.find_elements_by_css_selector(
                locator.ModalCreateNewObject.LHS_ITEM[1])
            try:
                element = elements_count[i]
            except:
                selector = locator.LhnMenu.LHS_CONTENT[1]
                self._driver.execute_script(
                    "$(\"" + selector +
                    "\").animate({ scrollTop: \"-1000000px\" })")
                # Click the gGRC Icon (right from LHN menu)
                self._click_when_visible(locator.HorNavBar.GGRC_ICON)
                # If LHN menu isn't open, open it and wait while its moving
                self.check_if_lhn_open(self._driver)
                self.wait_while_moving(self._driver, locator.LhnMenu.LHN_PIN)

                self.lhn_elements_count(self._driver)
                i = 0
                continue

#                 self._driver.execute_script(
#                     "$(\"" + selector +
#                     "\").animate({ scrollTop: \"1000000px\" })")

#                 ele = self._get_element_when_present(
#                     locator.LhnMenu.LAST_LHN_OBJECT)
#                 self._driver.execute_script(
#                     "arguments[0].scrollIntoView();", ele)
#                 time.sleep(5)
#                 self._get_element_when_visible(
#                     locator.ModalCreateNewObject.LHS_ITEM)
#                 elements_count = self._driver.find_elements_by_css_selector(
#                     locator.ModalCreateNewObject.LHS_ITEM[1])
#                 element = elements_count[i]
#                 i = -1

            if element.text in ident:
                ident.remove(element.text)
                while True:
                    try:
                        element.click()
                        break
                    except:
                        time.sleep(0.1)

                self._click_when_visible(
                    locator.ModalCreateNewObject.GEAR_ICON)
                self._click_when_visible(
                    locator.ModalCreateNewObject.DELETE_IN_GEAR)
                self._click_when_visible(locator.ModalCreateNewObject.DELETE)

                self.wait_for_redirect()

#                 if len(ident) != 0:
                    # If LHN menu isn't open, open it and wait while its moving
#                     self.check_if_lhn_open(self._driver)
#                     self.wait_while_moving(
#                         self._driver, locator.LhnMenu.LHN_PIN)

                    # Get the list of all elements in LHN menu
                    # The list need to be recreated every time and element is
                    # deleted or an exception will accrue.
#                     self._get_element_when_visible(
#                         locator.ModalCreateNewObject.LHS_ITEM)
#                     elements_count = self._driver \
#                         .find_elements_by_css_selector(
#                             locator.ModalCreateNewObject.LHS_ITEM[1])
                i = -1
            i += 1
